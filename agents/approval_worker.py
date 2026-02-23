#!/usr/bin/env python3
import json, os, time, urllib.request, urllib.parse, subprocess, re
from pathlib import Path
from datetime import datetime, timezone

def _load_dotenv(path: str) -> None:
    p = Path(path)
    if not p.exists():
        return
    for raw in p.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        k = k.strip()
        v = v.strip()
        if (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
            v = v[1:-1]
        os.environ.setdefault(k, v)

_load_dotenv(os.path.expanduser("~/801brain/.env"))

BRAIN_ROOT = Path(os.path.expanduser("~/801brain"))
PENDING_DIR = BRAIN_ROOT / "logs" / "pending"
PENDING_DIR.mkdir(parents=True, exist_ok=True)

REPO_DIR = Path(os.path.expanduser("~/fuzeatlas"))

TELEGRAM_BOT_TOKEN = (os.environ.get("TELEGRAM_BOT_TOKEN") or os.environ.get("TELEGRAM_TOKEN") or "").strip()
AUTO_APPROVE_CHAT_ID = (os.environ.get("AUTO_APPROVE_CHAT_ID") or "").strip()

VERCEL_TOKEN = (os.environ.get("VERCEL_TOKEN") or "").strip()
VERCEL_ORG_ID = (os.environ.get("VERCEL_ORG_ID") or os.environ.get("VERCEL_TEAM_ID") or "").strip()
VERCEL_PROJECT_ID = (os.environ.get("VERCEL_PROJECT_ID") or "").strip()

VERCEL_DEPLOY_HOOK_PROD = (os.environ.get("VERCEL_DEPLOY_HOOK_PROD") or "").strip()
VERCEL_DEPLOY_HOOK_URL = (os.environ.get("VERCEL_DEPLOY_HOOK_URL") or "").strip()

def now_iso():
    return datetime.now(timezone.utc).isoformat()

def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def save_json(path: Path, obj: dict):
    obj["updated_at"] = now_iso()
    path.write_text(json.dumps(obj, indent=2) + "\n", encoding="utf-8")

def send_telegram(chat_id, text: str):
    if not TELEGRAM_BOT_TOKEN or not chat_id:
        return None
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown", "disable_web_page_preview": True}
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    try:
        resp = urllib.request.urlopen(req, timeout=20)
        body = resp.read()
        print(f"[worker] ✅ sendMessage ok chat_id={chat_id} bytes={len(body)}")
        return body
    except Exception as e:
        try:
            err_body = getattr(e, "read", lambda: b"")()
        except Exception:
            err_body = b""
        print(f"[worker] ❌ sendMessage chat_id={chat_id} error={e} err_body={err_body!r}")
        return None

def _trigger_hook(url: str):
    req = urllib.request.Request(url, method="POST")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")

def _vercel_req(path: str, token: str, org_id: str | None = None):
    base = "https://api.vercel.com"
    url = base + path
    if org_id:
        sep = "&" if "?" in url else "?"
        url += f"{sep}teamId={urllib.parse.quote(org_id)}"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))

def _latest_deployment(token: str, project_id: str, org_id: str | None):
    q = f"/v6/deployments?projectId={urllib.parse.quote(project_id)}&limit=1"
    d = _vercel_req(q, token, org_id=org_id)
    arr = d.get("deployments") or []
    return arr[0] if arr else None

def _deployment_events(token: str, dep_id: str, org_id: str | None, limit: int = 30):
    d = _vercel_req(f"/v3/deployments/{urllib.parse.quote(dep_id)}/events", token, org_id=org_id)
    ev = d.get("events") or []
    return ev[-limit:]

def _poll_latest(token: str, project_id: str, org_id: str | None, timeout_s: int = 240):
    t0 = time.time()
    last = None
    while time.time() - t0 < timeout_s:
        dep = _latest_deployment(token, project_id, org_id)
        if dep:
            last = dep
            state = (dep.get("readyState") or dep.get("state") or "").upper()
            if state in ("READY", "ERROR", "CANCELED"):
                return dep
        time.sleep(2.0)
    return last

def _run(cmd: list[str], cwd: Path, timeout: int = 600):
    p = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True, timeout=timeout)
    out = (p.stdout or "") + (("\n" + p.stderr) if p.stderr else "")
    return p.returncode, out

def _git(cmd: list[str], timeout: int = 120):
    return _run(["git"] + cmd, cwd=REPO_DIR, timeout=timeout)

def _git_dirty():
    rc, out = _git(["status", "--porcelain"])
    return out.strip() != "" if rc == 0 else False

def _git_commit_push(msg: str):
    _git(["add", "-A"])
    rc, out = _git(["commit", "-m", msg], timeout=120)
    # commit may be "nothing to commit"
    rc2, out2 = _git(["push"], timeout=300)
    return (rc2 == 0), (out + "\n" + out2).strip()

# ------------------------------
# SAFE AUTO-FIX RULES
# (add more here as you hit new errors)
# ------------------------------
def _apply_autofix(build_output: str) -> tuple[bool, str]:
    """
    Returns (changed, note)
    """
    # Rule 1: TypeScript "always truthy" from nested || inside bracket key (your exact recent failure)
    m = re.search(r"\./scripts/import-atlas\.ts:(\d+):(\d+)\s*Type error: This kind of expression is always truthy\.", build_output)
    if m:
        p = REPO_DIR / "scripts" / "import-atlas.ts"
        if p.exists():
            txt = p.read_text(encoding="utf-8", errors="replace")
            before = txt
            txt = txt.replace(
                'asFloat(r["Weight (gsm)"] || r["Weight\\n(gsm) " || "") ?? null',
                'asFloat((r["Weight (gsm)"] || r["Weight\\n(gsm) "] || "")) ?? null'
            )
            # also handle variant spacing
            txt = txt.replace(
                'asFloat(r["Weight (gsm)"] || r["Weight\\n(gsm) " || "")) ?? null',
                'asFloat((r["Weight (gsm)"] || r["Weight\\n(gsm) "] || "")) ?? null'
            )
            if txt != before:
                p.write_text(txt, encoding="utf-8")
                return True, "autofix: corrected import-atlas weightGsm OR chain"
        return False, "autofix: rule matched but file/line pattern not changed"

    return False, "autofix: no rule matched"

def _ensure_deps():
    rc, out = _run(["npm", "ci"], cwd=REPO_DIR, timeout=600)
    if rc == 0:
        return True, "npm ci ok"
    rc2, out2 = _run(["npm", "install"], cwd=REPO_DIR, timeout=600)
    return (rc2 == 0), ("npm ci failed; npm install " + ("ok" if rc2 == 0 else "failed"))

def _npm_build():
    return _run(["npm", "run", "build"], cwd=REPO_DIR, timeout=900)

def _format_events(ev):
    lines = []
    for e in ev:
        t = e.get("type") or ""
        payload = e.get("payload") or {}
        msg = payload.get("text") or payload.get("message") or ""
        msg = str(msg).strip().replace("\r", "")
        if msg:
            lines.append(f"[{t}] {msg}")
    return "\n".join(lines[-30:])

def execute_packet(packet_id: str, chat_id: str | None):
    pkt_path = PENDING_DIR / f"{packet_id}.json"
    pkt = load_json(pkt_path)
    req = (pkt.get("request") or "").strip().lower()

    # STATUS: just report latest deployment + events if error
    if req == "status":
        if not (VERCEL_TOKEN and VERCEL_PROJECT_ID):
            return 1, "❌ Missing VERCEL_TOKEN or VERCEL_PROJECT_ID in ~/801brain/.env"
        dep = _latest_deployment(VERCEL_TOKEN, VERCEL_PROJECT_ID, VERCEL_ORG_ID or None)
        if not dep:
            return 1, "❌ No deployments found."
        dep_url = dep.get("url") or ""
        state = (dep.get("readyState") or dep.get("state") or "").upper()
        dep_id = dep.get("id") or ""
        out = f"Vercel: https://{dep_url} (state={state})"
        if dep_id:
            out += f"\nInspect: https://vercel.com/{dep_id}"
        if state == "ERROR" and dep_id:
            try:
                ev = _deployment_events(VERCEL_TOKEN, dep_id, VERCEL_ORG_ID or None, limit=30)
                tail = _format_events(ev)
                if tail:
                    out += "\n\n```text\n" + tail + "\n```"
            except Exception as e:
                out += f"\n\nevents fetch error: {e}"
        return 0, out

    # DEPLOY: full self-heal loop
    if req == "deploy":
        hook = VERCEL_DEPLOY_HOOK_PROD or VERCEL_DEPLOY_HOOK_URL
        if not hook:
            return 1, "❌ Missing VERCEL_DEPLOY_HOOK_PROD or VERCEL_DEPLOY_HOOK_URL in ~/801brain/.env"
        if not (VERCEL_TOKEN and VERCEL_PROJECT_ID):
            body = _trigger_hook(hook).strip() or "✅ Deploy hook triggered."
            return 0, body + "\nVercel follow-up skipped (missing VERCEL_TOKEN or VERCEL_PROJECT_ID)."

        # Make sure repo is in a sane state + deps ready
        ok_deps, dep_note = _ensure_deps()

        attempts = 0
        while attempts < 15:
            attempts += 1

            hook_body = _trigger_hook(hook).strip()
            msg = hook_body if hook_body else f"✅ Deploy hook triggered (attempt {attempts}/15)."
            dep = _poll_latest(VERCEL_TOKEN, VERCEL_PROJECT_ID, VERCEL_ORG_ID or None, timeout_s=240)
            if not dep:
                return 1, msg + "\n❌ Could not fetch deployment status."

            dep_url = dep.get("url") or ""
            state = (dep.get("readyState") or dep.get("state") or "").upper()
            dep_id = dep.get("id") or ""
            msg += f"\nVercel: https://{dep_url} (state={state})"
            if dep_id:
                msg += f"\nInspect: https://vercel.com/{dep_id}"

            if state == "READY":
                return 0, msg

            if state != "ERROR":
                # canceled/unknown — stop
                return 1, msg + f"\n❌ Deployment ended in state={state}. Stopping."

            # ERROR: grab events
            events_tail = ""
            if dep_id:
                try:
                    ev = _deployment_events(VERCEL_TOKEN, dep_id, VERCEL_ORG_ID or None, limit=30)
                    events_tail = _format_events(ev)
                except Exception as e:
                    events_tail = f"events fetch error: {e}"

            # Run local build to get actionable compiler output
            rc_build, out_build = _npm_build()

            # Apply autofix rules
            changed, note = _apply_autofix(out_build + "\n" + events_tail)

            if not changed:
                # No automatic fix available: report and stop (this prevents infinite loops)
                report = msg
                if events_tail.strip():
                    report += "\n\n```text\n" + events_tail[-3500:] + "\n```"
                report += "\n\n❌ Auto-fix could not match a known rule. Stopping."
                report += "\n(Next: add a new autofix rule for this error, or fix manually once and redeploy.)"
                return 1, report

            # Rebuild after fix
            rc_build2, out_build2 = _npm_build()
            if rc_build2 != 0:
                report = msg + f"\n\nApplied {note}, but build still fails."
                report += "\n\n```text\n" + out_build2[-3500:] + "\n```"
                return 1, report

            # Commit + push fix
            pushed, git_out = _git_commit_push(f"auto-fix deploy: {note}")
            if not pushed:
                report = msg + "\n\n✅ Build passes after autofix, but git push failed."
                report += "\n\n```text\n" + git_out[-3500:] + "\n```"
                return 1, report

            # Only retry deploy if we actually changed and pushed code
            msg2 = msg + f"\n\n✅ {note}\n✅ Build ok\n✅ Pushed fix — retrying deploy…"
            send_telegram(chat_id, msg2)

            # loop continues (attempts+1)

        return 1, "❌ Reached 15 deploy attempts. Stopping."

    return 0, "✅ Executed OK (no output)"

def main():
    print("✅ approval_worker running. Watching:", PENDING_DIR)
    print("[worker] cwd:", os.getcwd())
    print("[worker] AUTO_APPROVE_CHAT_ID:", AUTO_APPROVE_CHAT_ID)
    print("[worker] TELEGRAM_BOT_TOKEN_len:", len(TELEGRAM_BOT_TOKEN))
    print("[worker] VERCEL_TOKEN_len:", len(VERCEL_TOKEN))
    print("[worker] VERCEL_PROJECT_ID:", VERCEL_PROJECT_ID)
    print("[worker] VERCEL_ORG_ID:", VERCEL_ORG_ID)
    print("[worker] VERCEL_DEPLOY_HOOK_PROD set:", bool(VERCEL_DEPLOY_HOOK_PROD))
    print("[worker] VERCEL_DEPLOY_HOOK_URL set:", bool(VERCEL_DEPLOY_HOOK_URL))

    while True:
        try:
            for f in sorted(PENDING_DIR.glob("pkt_*.json")):
                try:
                    pkt = load_json(f)
                except Exception:
                    continue

                if pkt.get("status") not in (None, "pending"):
                    continue

                chat_id = pkt.get("chat_id")
                if not chat_id:
                    continue

                if AUTO_APPROVE_CHAT_ID and str(chat_id) != str(AUTO_APPROVE_CHAT_ID):
                    continue

                packet_id = pkt.get("id") or f.stem
                print(f"[worker] saw packet id={packet_id} status={pkt.get('status')} chat_id={chat_id}")

                pkt["status"] = "approved"
                save_json(f, pkt)
                save_json(f.with_suffix(".approved.json"), dict(pkt))

                send_telegram(chat_id, f"✅ *Auto-approved* `{packet_id}` — executing…")

                rc, output = execute_packet(packet_id, chat_id)

                pkt2 = load_json(f)
                pkt2["status"] = "ok" if rc == 0 else "failed"
                pkt2["result_rc"] = rc
                pkt2["result"] = {"rc": rc, "output": output}
                save_json(f, pkt2)

                send_telegram(chat_id, output if (output and output.strip()) else "✅ Executed (no output)")

        except Exception as e:
            print("worker error:", e)

        time.sleep(1.0)

if __name__ == "__main__":
    main()
