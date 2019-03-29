from configuration import Configuration
from telegram.ext import Updater
import logging


class TelegramNotifier:
    chat_id = 0

    def __init__(self):
        config = Configuration()
        self.LOGGER = logging.getLogger("srgrafo_crawler")
        updater = Updater(token=config.get_telegram_bot_token())
        self.chat_id = config.get_telegram_chat_id()
        self.bot = updater.bot

    def send_messages(self, url, preview_url, caption):
        self.LOGGER.debug("Sending "+caption+" with url "+url)
        self.bot.send_photo(chat_id=self.chat_id, photo=preview_url, caption=caption + " - "+url)