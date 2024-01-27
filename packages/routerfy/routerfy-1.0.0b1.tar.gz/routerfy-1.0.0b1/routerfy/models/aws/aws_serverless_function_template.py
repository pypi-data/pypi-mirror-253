import re
import yaml

from os import path

from routerfy.utils.yaml import Sub, get_dumper

from routerfy.types import RouterfyConfig
from routerfy.routing import APIRouter
from routerfy.models.base_model import BaseModel
from routerfy.utils import find_router_instance, pascalify
from routerfy.models.aws.aws_template import AWSTemplate

class AWSServerlessFunctionTemplate(AWSTemplate):
    
    def __init__(self, src: str, config: RouterfyConfig, **kwargs):
        super().__init__(**kwargs)
        self.application_name = config['AppName']
        self.build_model = config["Api"].get("BuildModel", False)
        self.name = src.split('\\')[-1]
        self.router = find_router_instance(src, APIRouter)
        self.config = config
        self.src = src
    
    def _get_global_config(self):
            self.template_body = {
                **self.template_body,
                **self.config.get('Global', {})
            }
    
    def _get_local_config(self):
        if self.name in self.config.get('Local', {}):
            self.template_body = {
                **self.template_body,
                **self.config['Local'][self.name]
            }
            
    def _get_lambda_global_config(self):
        return self.config.get("LambdaGlobal", {})
    
    def _get_lambda_local_config(self):
        return self.config.get("LambdaLocal", {}).get(self.name, {})
    
    def _parse_path(self, path: str):
        if path == "/":
            return ""
        query_path = re.search("\{\w+\}", path.split('/')[-1])
        if query_path is not None:
            return "/".join(path.split('/')[:-1])+f"/{path.split('/')[-1].replace('}', '+}')}"
            
    def build(self):
        """Build Lambda Resource
        """
        self._get_global_config()
        self._get_local_config()
        global_lambda_config = self._get_lambda_global_config()
        local_lambda_config = self._get_lambda_local_config()
        
        self.template_body = {
            **self.template_body,
            "Description": f"{self.name} Lambda of {self.application_name} App.",
            "Resources": {
                self.name: {
                    "Type": "AWS::Serverless::Function",
                    "Properties":{
                        "Architectures": [
                            "x86_64"
                        ],
                        "CodeUri": ".",
                        "Description": f"{self.name} Lambda of {self.application_name} App.",
                        "Events": {
                            pascalify(route.name): {
                                "Type": "Api",
                                "Properties":{
                                    "RestApiId": Sub(r"arn:aws:apigateway:${AWS::Region}:${AWS::AccountId}:restapi:" + self.application_name + "_API"),
                                    "Path": self.router.prefix + self._parse_path(route.path),
                                    "Method": route.method,
                                    **({"RequestModel": {
                                        "Model": pascalify(route.name+"_model"),
                                        "Required": True,
                                        "ValidateBody": True
                                    }} if self.build_model and len([value for value in route.args.values() if issubclass(value, BaseModel)]) > 0 else {})
                                }
                            } for route in self.router.routes
                        },
                        "FunctionName": f"{self.application_name}_{self.name}",
                        "Handler": "app.lambda_handler",
                        "Runtime": "python3.10",
                        "Timeout": 60,
                        **global_lambda_config,
                        **local_lambda_config
                    },
                }
            }
        }
    
    def create_template(self):
        """Write Lambda Template on lambda folder.
        """
        with open(path.join(self.src, 'template.yaml'), "w") as f:
            yaml.dump(self.template_body, f, Dumper=get_dumper())