import sys

args = sys.argv
parsed_exec_file = args[0].split("\\")[-1].split(".")[0]
if len(args) >= 2:
    arg_value = args[1]
else:
    arg_value = ""
if arg_value == "dev" or parsed_exec_file == "debugpy" or parsed_exec_file == "debug":
    from fastapi import APIRouter, Response, Request
    from pydantic import BaseModel
else:
    from routerfy.routing import APIRouter
    from routerfy.network import Response, Request
    from routerfy.models import BaseModel
    
__all__ = [
    "Response",
    "APIRouter",
    "Request",
    "BaseModel"
]