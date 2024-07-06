import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler
from telegram.ext.filters import Filters  # Import Filters from the correct module
from modules import welcome, start
from utils.config import TOKEN
from database.db import init_db


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


# Initialize database
init_db()


def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN, use_context=True)


    # Get the dispatcher to register handlers
    dp = updater.dispatcher


    # Register the start handler
    dp.add_handler(CommandHandler("start", start.start))


    # Register the button handler
    dp.add_handler(CallbackQueryHandler(start.button))


    # Register the welcome handler
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome.new_member))


    # Start the Bot
    updater.start_polling()


    # Run the bot until you press Ctrl-C
    updater.idle()


if __name__ == '__main__':
    main()