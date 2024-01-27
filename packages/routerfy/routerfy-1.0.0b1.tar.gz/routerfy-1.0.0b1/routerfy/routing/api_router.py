from typing import Callable, Any, List, Union
from routerfy.integrations import RouterfyIntegration
from routerfy.integrations.apigateway import LambdaIntegrationV1, LambdaIntegrationV2
from routerfy.network import Request, Response
from routerfy.routing.route import Route
from routerfy.models import BaseModel

class APIRouter():
    def __init__(
        self, 
        *,
        prefix: str = None, 
    ) -> None:
        
        if prefix is None:
            prefix = ""
        else:
            assert prefix.startswith("/"), "A path prefix must start with '/'"
            assert not prefix.endswith("/"), "A path prefix must not end with '/'"

        self.routes: List[Route] = []
        self.prefix = prefix
    
    def add_api_router(
        self,
        path: str,
        method: str
    ) -> Callable:
        
        def decorator(callback: Callable[..., Any]):
            self.routes.append(Route(method, path, callback))
            return callback
        
        return decorator

    def _find_route(self, event: Request) -> Union[Route, None]:
        
        for route in self.routes:
            full_path = self.prefix + route.path
            
            if full_path.endswith("/"):
                full_path = full_path[:-1]
            
            if not (route.method == event.method and full_path == event.url.path):
                continue
            
            return route
        
        return None
    
    def handle_request(self, event: Union[LambdaIntegrationV1, LambdaIntegrationV2]):
        
        routerfy_integration = RouterfyIntegration(event)
        
        routerfy_request = routerfy_integration.get_request()
        
        route = self._find_route(routerfy_request)

        if route is None:
            return {
                "body": "route not found",
                "statusCode": 404,
                "headers": {
                    "Content-Type": "application/json"
                }
            }
            
        args = {}
        
        for key in route.args.keys():
            args[key] = None
            
            if issubclass(route.args[key], BaseModel):  
                args[key] = route.args[key](arg_name=key, body=routerfy_request.json())
            
            if key == "body":
                args[key] = event['body']
            
            if key == "request":
                args[key] = routerfy_request
            
            if routerfy_request.path_params is not None:
                if key in routerfy_request.path_params.keys():
                    args[key] = routerfy_request.path_params[key]
                    break
                    
            if routerfy_request.query_params is not None:
                if key in routerfy_request.query_params.keys():
                    args[key] = routerfy_request.query_params[key]
                    break
        
        result = route.callback(**args)
        
        parsed_result = result if isinstance(result, Response) else Response(result)
        
        return {
            "body": parsed_result.content,
            "statusCode": parsed_result.status_code,
            "headers": parsed_result.headers
        }

    def get(self, path: str, *args, **kwargs):
        return self.add_api_router(path, method="GET")
    
    def post(self, path: str, *args, **kwargs):
        return self.add_api_router(path, method="POST")
    
    def put(self, path: str, *args, **kwargs):
        return self.add_api_router(path, method="PUT")
    
    def patch(self, path: str, *args, **kwargs):
        return self.add_api_router(path, method="PATCH")
    
    def delete(self,path: str, *args, **kwargs):
        return self.add_api_router(path, method="DELETE")
    
    def options(self,path: str, *args, **kwargs):
        return self.add_api_router(path, method="OPTIONS")