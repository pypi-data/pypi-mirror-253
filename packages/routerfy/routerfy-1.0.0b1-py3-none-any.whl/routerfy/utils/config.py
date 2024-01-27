import os
import yaml

from routerfy.types import RouterfyConfig
from routerfy.utils.yaml import get_loader

path = os.getcwd()

def get_config() -> RouterfyConfig:
    """
        Get project path and load configuration file
    """

    config_path = os.path.join(path, "routerfy.config.yaml")

    assert os.path.exists(config_path), 'configuration file not found'

    with open(config_path, "rb") as f:
        return yaml.load(f, Loader=get_loader())

def get_routes_path(config: RouterfyConfig):
    # Check if have and get preferable routes directory
    try:
        routes_dir = config["router"]["routers_dir"]
    except:
        routes_dir = "routes"
        
    return os.path.join(path, routes_dir)