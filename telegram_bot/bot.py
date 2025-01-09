from telegram.ext import Updater, CommandHandler
from backend.database import add_subscription, remove_subscription, get_subscriptions
from config import TELEGRAM_BOT_TOKEN

def start(update, context):
    update.message.reply_text("Welcome to Eventra AI! Use /subscribe <contract_address> to monitor a smart contract.")

def help_command(update, context):
    update.message.reply_text(
        "/subscribe <contract_address> - Monitor a specific contract address.
"
        "/unsubscribe <contract_address> - Stop monitoring a contract address.
"
        "/status - View active subscriptions.
"
        "/help - Show available commands."
    )

def subscribe(update, context):
    if len(context.args) < 1:
        update.message.reply_text("Usage: /subscribe <contract_address>")
        return

    contract_address = context.args[0]
    chat_id = update.effective_chat.id

    if len(contract_address) != 44:
        update.message.reply_text("Invalid contract address. Please try again.")
        return

    add_subscription(chat_id, contract_address)
    update.message.reply_text(f"Subscribed to contract address: {contract_address}")

def unsubscribe(update, context):
    if len(context.args) < 1:
        update.message.reply_text("Usage: /unsubscribe <contract_address>")
        return

    contract_address = context.args[0]
    chat_id = update.effective_chat.id
    remove_subscription(chat_id, contract_address)
    update.message.reply_text(f"Unsubscribed from contract address: {contract_address}")

def status(update, context):
    chat_id = update.effective_chat.id
    subscriptions = get_subscriptions(chat_id)
    if subscriptions:
        update.message.reply_text("Your subscriptions:
" + "
".join(sub.contract_address for sub in subscriptions))
    else:
        update.message.reply_text("You have no active subscriptions.")

def run_bot():
    updater = Updater(TELEGRAM_BOT_TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("subscribe", subscribe))
    dispatcher.add_handler(CommandHandler("unsubscribe", unsubscribe))
    dispatcher.add_handler(CommandHandler("status", status))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    run_bot()
