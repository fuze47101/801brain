#!/usr/bin/env python3
import json
import os
import re
import sys
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

BRAIN_ROOT = Path(__file__).resolve().parents[1]
PENDING_DIR = BRAIN_ROOT / "logs" / "pending"

def now_iso() -> str:
  return datetime.now(timezone.utc).isoformat()

def load_json(p: Path) -> Dict[str, Any]:
  return json.loads(p.read_text(encoding="utf-8"))

def save_json(p: Path, d: Dict[str, Any]) -> None:
  d["updated_at"] = now_iso()
  p.write_text(json.dumps(d, indent=2), encoding="utf-8")

def infer_actions_from_request(request: str) -> Tuple[List[str], Optional[str]]:
  """
  Supported:
    - "run command: <cmd>" => commands=[<cmd>]
    - "run: <cmd>" / "cmd:" / "command:" => commands=[<cmd>]
    - "run_script: <cmd>" / "run script:" => run_script=<cmd>
  """
  req = (request or "").strip()
  lower = req.lower()

  for prefix in ("run command:", "run:", "cmd:", "command:"):
    if lower.startswith(prefix):
      cmd = req[len(prefix):].strip()
      return ([cmd] if cmd else []), None

  for prefix in ("run_script:", "run script:"):
    if lower.startswith(prefix):
      cmd = req[len(prefix):].strip()
      return [], (cmd if cmd else None)

  return [], None

def run_shell(cmd: str) -> Tuple[int, str]:
  proc = subprocess.run(
    ["bash", "-lc", cmd],
    capture_output=True,
    text=True,
    env=os.environ.copy(),
  )
  out = (proc.stdout or "")
  if proc.stderr:
    out += ("\n" + proc.stderr)
  return proc.returncode, out

def main() -> None:
  if len(sys.argv) < 2:
    print("usage: run_packet.py <packet_id>", file=sys.stderr)
    sys.exit(2)

  packet_id = sys.argv[1].strip()
  pf = PENDING_DIR / f"{packet_id}.json"
  if not pf.exists():
    print(f"packet not found: {pf}", file=sys.stderr)
    sys.exit(2)

  packet = load_json(pf)

  # Ensure actions exist (fallback parse from request)
  cmds = packet.get("commands")
  run_script = packet.get("run_script") or packet.get("runScript")

  if not cmds and not run_script:
    inferred_cmds, inferred_rs = infer_actions_from_request(packet.get("request", ""))
    if inferred_cmds:
      packet["commands"] = inferred_cmds
      cmds = inferred_cmds
    if inferred_rs:
      packet["run_script"] = inferred_rs
      run_script = inferred_rs

  outputs: List[Dict[str, Any]] = []
  rc_final = 0

  # Run commands list
  if isinstance(cmds, list):
    for c in cmds:
      rc, out = run_shell(str(c))
      outputs.append({"type": "command", "command": c, "rc": rc, "output": out})
      if rc != 0:
        rc_final = rc
        break

  # Run run_script
  if run_script and rc_final == 0:
    rc, out = run_shell(str(run_script))
    outputs.append({"type": "run_script", "command": run_script, "rc": rc, "output": out})
    rc_final = rc

  packet["results"] = outputs
  packet["result"] = outputs[-1] if outputs else None
  packet["result_rc"] = rc_final
  packet["status"] = "ok" if rc_final == 0 else "failed"

  save_json(pf, packet)

  # Print tail for telegram
  tail = ""
  if outputs:
    tail = outputs[-1].get("output") or ""
  if len(tail) > 3500:
    tail = tail[-3500:]
  if tail.strip():
    print(tail)

  sys.exit(rc_final)

if __name__ == "__main__":
  main()
