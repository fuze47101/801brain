import os
import subprocess
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

# ===== LOAD ENV =====
BRAIN_ROOT = os.path.expanduser("~/801brain")
load_dotenv(os.path.join(BRAIN_ROOT, ".env"))

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# ===== MESSAGE HANDLER =====
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    parts = text.split(" ")

    if len(parts) < 2:
        await update.message.reply_text(
            "Format:\n"
            "<project> resume\n"
            "<project> confirm\n"
            "<project> <role> <request>"
        )
        return

    project = parts[0]
    action = parts[1]

    # ===== RESUME MODE =====
    if action == "resume":
        command = [
            "python3",
            os.path.join(BRAIN_ROOT, "agents", "agent.py"),
            "cloud",
            project,
            "resume"
        ]

    # ===== CONFIRM TASKS =====
    elif action == "confirm":
        command = [
            "python3",
            os.path.join(BRAIN_ROOT, "agents", "agent.py"),
            "cloud",
            project,
            "confirm"
        ]

    # ===== ROLE MODE =====
    else:
        if len(parts) < 3:
            await update.message.reply_text(
                "Format: <project> <role> <request>"
            )
            return

        role = parts[1]
        request = " ".join(parts[2:])

        command = [
            "python3",
            os.path.join(BRAIN_ROOT, "agents", "agent.py"),
            "cloud",
            project,
            role,
            request
        ]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=90
        )

        output = result.stdout.strip()

        if not output:
            output = "No output returned."

    except Exception as e:
        output = f"Execution error: {str(e)}"

    # Telegram message size limit protection
    if len(output) > 4000:
        output = output[:3900] + "\n\n[Truncated]"

    await update.message.reply_text(output)

# ===== MAIN =====
def main():
    if not TELEGRAM_TOKEN:
        raise ValueError("TELEGRAM_TOKEN not found in .env file")

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Telegram Agent Running...")
    app.run_polling()

if __name__ == "__main__":
    main()
