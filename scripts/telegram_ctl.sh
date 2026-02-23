#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PID_FILE="$ROOT/logs/telegram_agent.pid"
LOG_FILE="$ROOT/logs/telegram_agent.out"
LOCK_FILE="$ROOT/logs/telegram_agent.lock"

start() {
  # if pidfile exists and pid is alive, do nothing
  if [[ -f "$PID_FILE" ]]; then
    PID="$(cat "$PID_FILE" 2>/dev/null || true)"
    if [[ -n "${PID:-}" ]] && ps -p "$PID" >/dev/null 2>&1; then
      echo "ℹ️ Already running pid=$PID"
      exit 0
    fi
  fi

  # clean stale artifacts
  rm -f "$PID_FILE"

  cd "$ROOT"
  source .venv/bin/activate
  set -a; source .env; set +a

  nohup python -u agents/telegram_agent.py > "$LOG_FILE" 2>&1 &
  echo $! > "$PID_FILE"
  sleep 0.8

  PID="$(cat "$PID_FILE")"
  if ps -p "$PID" >/dev/null 2>&1; then
    echo "✅ Started pid=$PID"
  else
    echo "❌ Failed to start. Tail logs:"
    tail -n 120 "$LOG_FILE" || true
    exit 1
  fi
}

stop() {
  # kill by pidfile if exists
  if [[ -f "$PID_FILE" ]]; then
    PID="$(cat "$PID_FILE" 2>/dev/null || true)"
    if [[ -n "${PID:-}" ]] && ps -p "$PID" >/dev/null 2>&1; then
      kill "$PID" 2>/dev/null || true
      sleep 0.5
      kill -9 "$PID" 2>/dev/null || true
    fi
  fi

  # also kill any stragglers
  pkill -9 -f "agents/telegram_agent.py" 2>/dev/null || true

  rm -f "$PID_FILE" "$LOCK_FILE"
  echo "✅ Stopped"
}

status() {
  if [[ -f "$PID_FILE" ]]; then
    PID="$(cat "$PID_FILE" 2>/dev/null || true)"
    if [[ -n "${PID:-}" ]] && ps -p "$PID" >/dev/null 2>&1; then
      echo "✅ Running pid=$PID"
      exit 0
    fi
  fi
  echo "❌ Not running"
  exit 1
}

logs() {
  tail -n 200 -f "$LOG_FILE"
}

case "${1:-status}" in
  start) start ;;
  stop) stop ;;
  restart) stop; start ;;
  status) status ;;
  logs) logs ;;
  *) echo "Usage: $0 {start|stop|restart|status|logs}" ;;
esac
