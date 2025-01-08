from telegram.ext import Updater, CommandHandler
from backend.database import add_subscription

# Load Bot Token
from config import TELEGRAM_BOT_TOKEN

def start(update, context):
    update.message.reply_text("Welcome! Use /subscribe <wallet> to start monitoring events.")

def subscribe(update, context):
    if len(context.args) < 1:
        update.message.reply_text("Usage: /subscribe <wallet_address>")
        return

    wallet = context.args[0]
    chat_id = update.effective_chat.id

    # Save to database
    add_subscription(chat_id, wallet)
    update.message.reply_text(f"Subscribed to wallet: {wallet}")

def run_bot():
    updater = Updater(TELEGRAM_BOT_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("subscribe", subscribe))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    run_bot()
