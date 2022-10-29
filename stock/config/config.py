import yaml
import logging

from stock.config.key_vault import KeyvaultClient

logger = logging.getLogger(__name__)

def get_config_from_yaml(profile=None):
    path = 'application.yml' if profile == None else f'application-{profile}.yml'
    with open(path, 'r') as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print("yaml file read failed, {}", exc)
    return config

class Config:
    def __init__(self, profile=None):
        self.__config = {'profile': profile}
        self.__config.update(get_config_from_yaml(profile))

    def get(self, property_key):
        paths = property_key.split('.')
        target = self.__config

        try:
            for path in paths:
                target = target[path]
            return target
        except:
            logger.error(f"Wrong config for the path: {property_key}")
            return None
    