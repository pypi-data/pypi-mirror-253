from typing import Literal

class InvalidBody(Exception):
    def __init__(self, name: str, body_model: dict):
        super().__init__("Required key missing on {} body: {}".format(name, body_model))
        
class InvalidConfigFile(Exception):
    def __init__(self, property: str, invalidation: Literal['missing', 'incorrect', 'bad formatted']):
        super().__init__("Invalid configuration file, {} property is {}.".format(property, invalidation))