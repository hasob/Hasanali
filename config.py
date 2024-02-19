import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6720857511:AAEgLIT3fT751_jsMJwr8hr5KI-Qrgly0VA")

    APP_ID = int(os.environ.get("APP_ID", 26004411))

    API_HASH = os.environ.get("API_HASH", "4b9a73c02e89da49ef7f7df8a7e30f65")

    