
import importlib
from decouple import config, Csv


class ConfigDefault:
    APP_TITLE = config(
        "APP_TITLE", default='Comunicator', cast=str)
    APP_VERSION = config("APP_VERSION", default='0.1.1', cast=str)
    COMMUNICATOR_API = config("COMMUNICATOR_API", cast=str)
    COMMUNICATOR_TOKEN = config("COMMUNICATOR_TOKEN", cast=str)
    COMMUNICATOR_WHATSAPP_TYPES = config(
        "COMMUNICATOR_WHATSAPP_TYPES",
        default="whatsapp,whatsapp360dialog,whatsappcloudapi", cast=Csv())


def get_config():
    """ Create Configs object to load in application"""
    config_app = getattr(importlib.import_module(
        "communicator.configs"), 'ConfigDefault')
    return config_app
