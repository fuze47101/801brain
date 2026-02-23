#!/usr/bin/env bash
set -euo pipefail

ROOT="$HOME/801brain"
SESSION="brain"
LOGFILE="$ROOT/logs/execution_log.md"

mkdir -p "$ROOT/scripts" "$ROOT/logs"
touch "$LOGFILE"

# Create session if missing
if ! tmux has-session -t "$SESSION" 2>/dev/null; then
  tmux new-session -d -s "$SESSION" -c "$ROOT"
fi

# Window 0: Command Center
tmux rename-window -t "$SESSION":0 "cmd"

# Pane 0: shell
tmux send-keys -t "$SESSION":0.0 "cd \"$ROOT\"" C-m

# Split right pane: live log tail (NO newline parse errors)
tmux split-window -h -t "$SESSION":0 -c "$ROOT"
tmux send-keys -t "$SESSION":0.1 "cd \"$ROOT\" && tail -n 120 -f \"$LOGFILE\"" C-m

# Split bottom-left pane: quick status helpers
tmux select-pane -t "$SESSION":0.0
tmux split-window -v -t "$SESSION":0 -c "$ROOT"
tmux send-keys -t "$SESSION":0.2 "cd \"$ROOT\" && echo 'Ready. Commands: git status | ls | ps aux | tmux ls'" C-m

# Helpful defaults
tmux select-pane -t "$SESSION":0.0

echo "✅ Brain command center ready."
echo "Attach with:"
echo "tmux attach -t $SESSION"