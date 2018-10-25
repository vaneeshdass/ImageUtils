import configparser


def get_config_object():
    config = configparser.ConfigParser()
    config.read('configuration.ini')
    return config
