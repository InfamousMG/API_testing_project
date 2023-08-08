import configparser


def get_config():
    # creating an object from Configparser class and reading the properties.ini file
    # where endpoint address is stored
    config = configparser.ConfigParser()
    config.read("utilities/properties.ini")
    return config
