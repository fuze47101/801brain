import subprocess
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# SET THESE
BOT_TOKEN = "8394346026:AAHI2LvcMguX4qIcwXE047eujnWjWDxdiWw"
AUTHORIZED_USER_ID = 7215420287  # replace with your Telegram user ID

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != AUTHORIZED_USER_ID:
        await update.message.reply_text("Unauthorized.")
        return

    user_message = update.message.text

    try:
        # Call your hybrid agent
        result = subprocess.run(
            ["python3", "agent.py", "cloud", user_message],
            capture_output=True,
            text=True,
            timeout=120
        )

        response = result.stdout.strip()

        if not response:
            response = "No output returned."

    except Exception as e:
        response = f"Error: {str(e)}"

    # Telegram max message size safety
    if len(response) > 4000:
        response = response[:4000]

    await update.message.reply_text(response)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Telegram Agent Running...")
    app.run_polling()

if __name__ == "__main__":
    main()

