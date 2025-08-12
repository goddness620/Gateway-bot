import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# --- Load environment variables ---
TELEGRAM_TOKEN = os.getenv(AAGI0HT10oY01GU5Whta0DFas0KhxqJkfXA)
MAIN_CHANNEL_LINK = os.getenv(t.me/+FJ7om5uViodlMzYx)
CHAT_GROUP_LINK = os.getenv(t.me/+qG6umznWBlZhNDcx)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "🍌 *Welcome to Minion Books Gateway!* 🍌\n\n"
        "Join our main channel and our chat group to not miss restocks!.\n\n"
        "Click below to join!"
    )

    keyboard = [
        [InlineKeyboardButton("📢 Main Channel", url=MAIN_CHANNEL_LINK)],
        [InlineKeyboardButton("💬 Chat ", url=CHAT_GROUP_LINK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        welcome_text,
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

def main():
    if not TELEGRAM_TOKEN:
        print("Error: TELEGRAM_TOKEN is not set.")
        return

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
