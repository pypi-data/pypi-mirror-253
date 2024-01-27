from typing import Union

import os

from sys import modules, path

import socket, errno
from importlib.util import spec_from_loader, module_from_spec
from importlib.machinery import SourceFileLoader

from routerfy.routing import APIRouter as RouterfyAPIRouter
from fastapi import APIRouter as FastAPIApiRouter

from routerfy.exceptions import APIRouterNotFound

def find_router_instance(src: str, router_class: Union[RouterfyAPIRouter, FastAPIApiRouter]) -> Union[RouterfyAPIRouter, FastAPIApiRouter]:
    try:
        path.append(src)
        
        module_name = src.split("\\")[-1]
        loader = SourceFileLoader(module_name, src)
        spec = spec_from_loader(module_name, loader)
        module = module_from_spec(spec)
        modules[module_name] = module
        
        module_name = src.split("\\")[-1]+".route"
        loader = SourceFileLoader(module_name, os.path.join(src, "route.py"))
        spec = spec_from_loader(module_name, loader)
        route_module = module_from_spec(spec)
        modules[module_name] = route_module
        
        loader.exec_module(route_module)
        
        attributtes = [item for item in dir(route_module) if not item.startswith("__")]
        
        for attribute in attributtes:
            possible_router_instance = route_module.__getattribute__(attribute)
            if isinstance(possible_router_instance, router_class):
                path.remove(src)
                return possible_router_instance
            
        raise APIRouterNotFound(src)
    except Exception as e:
        raise e

def is_port_in_use(port: int) -> bool:
    """Check if ports are currently in use.
    
    Args:
        port (int): Port you want to check it.

    Returns:
        bool: Return 'True' if in use else return 'False'.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(("127.0.0.1", port))
    except socket.error as e:
        if e.errno == errno.EADDRINUSE:
            return True
        else:
            pass
    s.close()
    return False