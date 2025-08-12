"""
Telegram Channel & Chat Welcome Bot
-----------------------------------
Sends a welcome message with two join buttons: one for your main channel,
one for your chat group.
"""

import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# --- CONFIG ---
TELEGRAM_TOKEN = os.getenv("8436242083:AAELCPxgeP6e3GVcpjCuLRKHvsLgtz4HEJw")

MAIN_CHANNEL_LINK = "https://t.me/+FJ7om5uViodlMzYx"  # replace with your channel invite link
CHAT_GROUP_LINK = "https://t.me/+qG6umznWBlZhNDcx"      # replace with your chat invite link

# --- COMMAND HANDLERS ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "🍌 *Welcome to Shark Chat Channel!* 🍌"
        "Join our main channel and our chat group to miss NO restocks!."
        "Click below to join!"
    )

    # Two buttons: Main Channel & Chat Group
    keyboard = [
        [InlineKeyboardButton("📢 Main Channel", url=MAIN_CHANNEL_LINK)],
        [InlineKeyboardButton("💬 Chat Group", url=CHAT_GROUP_LINK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        welcome_text,
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

# --- MAIN ---
def main():
    if TELEGRAM_TOKEN.startswith("YOUR_"):
        print("Please set TELEGRAM_TOKEN env var or edit the file.")
        return

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Bot is running... Press Ctrl+C to stop.")
    app.run_polling()

if __name__ == "__main__":
    main()
