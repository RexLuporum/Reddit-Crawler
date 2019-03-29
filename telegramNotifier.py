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

        title = caption + " - " + url
        if len(title) > 1024:
            self.LOGGER.info("Title to long. Need to cut it")
            max_length = 1023 - len("... - " + url)
            title = caption[:max_length] + "... - " + url
        self.LOGGER.debug("Sending "+title)
        self.bot.send_photo(chat_id=self.chat_id, photo=preview_url, caption=title, disable_notification=False)