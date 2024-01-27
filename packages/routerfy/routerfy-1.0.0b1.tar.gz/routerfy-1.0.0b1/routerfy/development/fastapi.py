from fastapi import APIRouter, FastAPI

from dotenv import load_dotenv

from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

import os
import uvicorn
import platform

from routerfy.utils.net import is_port_in_use
from routerfy.utils.config import get_config, get_routes_path
from routerfy.utils.net import find_router_instance

app = FastAPI()

config = get_config()
    
routes_path = get_routes_path(config)

assert os.path.exists(routes_path) and not os.listdir(routes_path) == [], f'no routes was found. certify that all routes are in "{routes_path}" directory and the lambda folder contains a "route.py" file.'

# Get all routers from lambda modules

for path in os.listdir(routes_path):
    app.include_router(find_router_instance(os.path.join(routes_path, path), APIRouter))
    
try:
    cors_config = config["api"]["cors"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins = cors_config["AllowOrigins"],
        allow_credentials = cors_config["AllowCredentials"],
        allow_methods = cors_config["AllowMethods"],
        allow_headers = cors_config["AllowHeaders"],
    )
except:
    pass

app.add_middleware(GZipMiddleware)

def start_api():
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        os.system('clear')
    elif platform == "win32":
        os.system('cls')
    
    load_dotenv(routes_path + '.env')
    port = None
    for i in range(8000, 9000):
        if not is_port_in_use(i):
            port = i
    if port is None:
        raise ConnectionError("Failed to find available port to open server!")
    uvicorn.run(app="routerfy.development.fastapi:app", host="127.0.0.1", port=port, workers=1, reload=True)