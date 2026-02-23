#!/usr/bin/env python3
"""
Orchestrator: creates a pending packet for Telegram approvals.

Usage examples (run in terminal):
  python agents/orchestrator.py --chat-id <YOUR_CHAT_ID> --project atlas --summary "Build core schema v1" --files "fuzeatlas/database/core_v1.sql,fuzeatlas/scripts/build_core_dev.sh" --run-script "~/fuzeatlas/scripts/build_core_dev.sh"

This writes:
  ~/801brain/logs/pending/<chat_id>.json
"""

import argparse
import json
import os
import pathlib
from datetime import datetime, timezone
import uuid


BRAIN_ROOT = pathlib.Path(os.path.expanduser("~/801brain"))
PENDING_DIR = BRAIN_ROOT / "logs" / "pending"
PENDING_DIR.mkdir(parents=True, exist_ok=True)


def pending_path(chat_id: int) -> pathlib.Path:
    return PENDING_DIR / f"{chat_id}.json"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chat-id", type=int, required=True)
    ap.add_argument("--project", type=str, required=True)
    ap.add_argument("--summary", type=str, required=True)
    ap.add_argument("--files", type=str, default="")
    ap.add_argument("--commands", type=str, default="")
    ap.add_argument("--run-script", type=str, default="")
    args = ap.parse_args()

    packet = {
        "id": f"chg_{uuid.uuid4().hex[:10]}",
        "project": args.project,
        "summary": args.summary,
        "files": [f.strip() for f in args.files.split(",") if f.strip()],
        "commands": [c.strip() for c in args.commands.split(",") if c.strip()],
        "run_script": args.run_script.strip() or None,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }

    p = pending_path(args.chat_id)
    p.write_text(json.dumps(packet, indent=2))
    print(f"✅ Wrote pending packet:\n{p}\n\nNext: open Telegram and reply 'approve' or 'reject'.")


if __name__ == "__main__":
    main()