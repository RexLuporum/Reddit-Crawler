import configparser


class Configuration:
    CONFIG_FILE = "config.ini"

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(self.CONFIG_FILE)

    def is_telegram_enabled(self):
        return self.to_bool(self.config['Telegram']['enabled'])

    def get_telegram_bot_token(self):
        return self.config['Telegram']['bot_token']

    def get_telegram_chat_id(self):
        return int(self.config['Telegram']['chat_id'])

    def is_reddit_enabled(self):
        return self.to_bool(self.config['Reddit']['enabled'])

    def get_redditor(self):
        return self.config['Reddit']['redditor']

    def get_subreddit(self):
        return self.config['Reddit']['subreddit']

    def get_reddit_client_id(self):
        return self.config['Reddit']['client_id']

    def get_reddit_client_secret(self):
        return self.config['Reddit']['client_secret']

    def get_reddit_username(self):
        return self.config['Reddit']['username']

    def get_reddit_password(self):
        return self.config['Reddit']['password']

    def to_bool(self, value):
        return value.lower() in ("yes", "true", "t", "1")