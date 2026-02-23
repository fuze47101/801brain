#!/usr/bin/env bash
set -euo pipefail

ROOT="$HOME/801brain"
SESSION="telegram"

cd "$ROOT"

mkdir -p "$ROOT/scripts" "$ROOT/logs"

# Create session if missing
if ! tmux has-session -t "$SESSION" 2>/dev/null; then
  tmux new-session -d -s "$SESSION" -c "$ROOT"
fi

# Start bot if not running
if pgrep -f "$ROOT/agents/telegram_agent.py" >/dev/null 2>&1; then
  echo "ℹ️ Bot already running."
else
  tmux send-keys -t "$SESSION":0 \
    "cd \"$ROOT\" && source .venv/bin/activate && set -a && source .env && set +a && python agents/telegram_agent.py" C-m
  echo "✅ Telegram bot started in tmux session: $SESSION"
fi

# Advice depending on whether you're already inside tmux
if [[ -n "${TMUX:-}" ]]; then
  echo "✅ You're already inside tmux."
  echo "Switch to the bot session with:"
  echo "tmux switch-client -t $SESSION"
else
  echo "✅ Attach with:"
  echo "tmux attach -t $SESSION"
fi