#!/usr/bin/env bash
set -euo pipefail

BRAIN_ROOT="${HOME}/801brain"
SESSION="${1:-brain}"

cd "$BRAIN_ROOT"

if ! command -v tmux >/dev/null 2>&1; then
  echo "❌ tmux not installed. Install with: brew install tmux"
  exit 1
fi

# If you're already inside tmux, don't try to attach inside attach.
if [ -n "${TMUX:-}" ]; then
  echo "ℹ️ You are already inside a tmux session."
  echo "Use: tmux switch-client -t ${SESSION}  (or detach with Ctrl-b d)"
  exit 0
fi

# Start session if missing
if ! tmux has-session -t "$SESSION" 2>/dev/null; then
  tmux new-session -d -s "$SESSION" -n "cmd"
  tmux send-keys -t "${SESSION}:cmd" "cd ~/801brain" C-m
  tmux send-keys -t "${SESSION}:cmd" "source .venv/bin/activate" C-m
  tmux send-keys -t "${SESSION}:cmd" "echo '✅ 801brain command center'" C-m

  tmux new-window -t "$SESSION" -n "telegram"
  tmux send-keys -t "${SESSION}:telegram" "cd ~/801brain" C-m
  tmux send-keys -t "${SESSION}:telegram" "source .venv/bin/activate" C-m
  tmux send-keys -t "${SESSION}:telegram" "./scripts/run_telegram.sh" C-m

  tmux new-window -t "$SESSION" -n "logs"
  tmux send-keys -t "${SESSION}:logs" "cd ~/801brain && tail -n 120 -f logs/execution_log.md" C-m
fi

tmux attach -t "$SESSION"