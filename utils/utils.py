import configparser


def read_env_config(category, key):
    file_path = "envconfig/config.ini"
    config = configparser.ConfigParser()
    config.read(file_path)
    return config.get(category, key)
