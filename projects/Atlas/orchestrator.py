#!/usr/bin/env python3
"""
801brain Orchestrator (approval packet engine)

This is NOT the "do everything" bot. This is the *approval packet creator*.
Telegram agent reads these packets and asks you to approve/reject.

Commands (terminal):
  python agents/orchestrator.py create --chat-id 123 --project atlas \
    --summary "Build core schema v1" \
    --files "fuzeatlas/database/core_v1.sql,fuzeatlas/scripts/build_core_dev.sh" \
    --commands "cd ~/fuzeatlas,source .venv/bin/activate,./scripts/build_core_dev.sh"

  python agents/orchestrator.py status --chat-id 123
"""

import argparse
import json
import os
import pathlib
from datetime import datetime, timezone
import uuid

BRAIN_ROOT = pathlib.Path(os.path.expanduser("~/801brain"))
LOGS_DIR = BRAIN_ROOT / "logs"
PENDING_DIR = LOGS_DIR / "pending"
PENDING_DIR.mkdir(parents=True, exist_ok=True)


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def pending_path(chat_id: int) -> pathlib.Path:
    return PENDING_DIR / f"{chat_id}.json"


def write_packet(chat_id: int, packet: dict) -> pathlib.Path:
    p = pending_path(chat_id)
    packet["updated_at"] = now_iso()
    p.write_text(json.dumps(packet, indent=2))
    return p


def create_packet(chat_id: int, project: str, summary: str, files: str, commands: str, run_script: str | None):
    packet = {
        "id": f"chg_{uuid.uuid4().hex[:10]}",
        "project": project.strip(),
        "summary": summary.strip(),
        "files": [f.strip() for f in (files or "").split(",") if f.strip()],
        "commands": [c.strip() for c in (commands or "").split(",") if c.strip()],
        "run_script": (run_script or "").strip() or None,
        "state": "pending",  # pending | approved | rejected | executed | failed
        "created_at": now_iso(),
        "updated_at": now_iso(),
    }
    p = write_packet(chat_id, packet)
    print(f"✅ Wrote pending packet:\n{p}\n\nNext: approve/reject in Telegram.")
    return 0


def status(chat_id: int):
    p = pending_path(chat_id)
    if not p.exists():
        print(f"ℹ️ No pending packet found for chat_id={chat_id} at {p}")
        return 0
    pkt = json.loads(p.read_text())
    print(json.dumps(pkt, indent=2))
    return 0


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    ap_create = sub.add_parser("create", help="Create/overwrite a pending approval packet for a chat_id")
    ap_create.add_argument("--chat-id", type=int, required=True)
    ap_create.add_argument("--project", type=str, required=True)
    ap_create.add_argument("--summary", type=str, required=True)
    ap_create.add_argument("--files", type=str, default="")
    ap_create.add_argument("--commands", type=str, default="")
    ap_create.add_argument("--run-script", type=str, default="")

    ap_status = sub.add_parser("status", help="Show current packet for a chat_id")
    ap_status.add_argument("--chat-id", type=int, required=True)

    args = ap.parse_args()

    if args.cmd == "create":
        return create_packet(
            chat_id=args.chat_id,
            project=args.project,
            summary=args.summary,
            files=args.files,
            commands=args.commands,
            run_script=args.run_script,
        )
    if args.cmd == "status":
        return status(args.chat_id)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())