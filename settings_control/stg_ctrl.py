import configparser

stg_path = 'settings.ini'


def readConfig():
    config = configparser.ConfigParser()
    config.read(stg_path)
    return config.get("Settings", "bot_api_key")


def createConfig():
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.add_section("Example")
    config.set("Settings", "bot_api_key", "telegram_api_key")
    config.set("Example", "bot_api_key", "6230511529:AAG5b4g2jE-ZhKB4LZa-MiTH6c3ofkb4k6Y")
    with open(stg_path, "w") as config_file:
        config.write(config_file)
