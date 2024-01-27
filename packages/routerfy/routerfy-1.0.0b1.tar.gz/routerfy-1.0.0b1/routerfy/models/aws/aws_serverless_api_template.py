import yaml

from typing import List
from os import path, mkdir, getcwd, listdir

from routerfy.types.aws.aws_serverless_api import AWSServerlessApi
from routerfy.utils.yaml import get_dumper

from routerfy.types import RouterfyConfig
from routerfy.routing import APIRouter
from routerfy.utils.net import find_router_instance
from routerfy.models.aws.aws_template import AWSTemplate
from routerfy.models.base_model import BaseModel
from routerfy.exceptions import InvalidConfigFile

from routerfy.utils import pascalify, python_class_to_AWS_type

class AWSServerlessRestApiTemplate(AWSTemplate):
    
    def __init__(self, routes_path: str, config: RouterfyConfig, **kwargs):
        super().__init__(**kwargs)
        self.application_name = config["AppName"]
        self.build_model = config["Api"].get("BuildModel", False)
        self.name = config["Api"].get("Name", self.application_name+"_API")
        self.config = config
        self.routes_path = routes_path
        
    def _check_optional_annotation(self, key: str, annotations: dict[str, type]):
        return str(annotations[key]).find("Optional") != -1 or str(annotations[key]).find("None") != -1
        
    def _build_models(self):
        
        assert self.routes_path is not None, "Routes path not found"

        api_router_list: List[APIRouter] = []

        for route in listdir(self.routes_path):
            api_router_list.append(find_router_instance(path.join(self.routes_path, route), APIRouter))

        if not api_router_list:
            return
        
        self.models = {}
        
        for router in api_router_list:
            for route in router.routes:
               for key in route.args.keys():
                    if issubclass(route.args[key], BaseModel):
                        annotations = route.args[key](arg_name=key).__annotations__
                        for arg in annotations.keys():
                            model_name = pascalify(route.name+"_model")
                            self.models = {
                                **self.models,
                                model_name: {
                                    "type": "object",
                                    "required": [*self.models.get(model_name, {}).get("required", []), *[arg for arg in annotations.keys() if not self._check_optional_annotation(arg, annotations)]],
                                    "properties": {
                                        **self.models.get(model_name, {}).get("properties", {}),
                                        arg: {"type": python_class_to_AWS_type(annotations[arg])}   
                                    }
                                }
                            }
                            
        
    
    def _get_template_header(self):
        return {
            **self.template_body,
            "Description": f"{self.name} API Gateway of {self.application_name} App." 
        }
    
    def build(self):
        if self.build_model:
            self._build_models()

        try:
            self.api_properties : AWSServerlessApi = {
                "Name": self.name,
                "StageName": self.config["Api"]["StageName"],
                **({"Models": self.models} if self.build_model and (len(self.models.keys()) > 0) else {})
            }
        except:
            InvalidConfigFile("Api>StageName", "missing")

        self.template_body = {
            **self._get_template_header(),
            "Resources": {
                "Type": "AWS::Serverless:RestApi",
                "Properties": {
                    **self.api_properties
                }
            }
        }
    
    def create_template(self):
        build_path = path.join(getcwd(), 'api')
        if not path.exists(build_path):
            mkdir(build_path)
        with open(path.join(getcwd(), 'api', 'template.yaml'), "w") as f:
            yaml.dump(self.template_body, f, Dumper=get_dumper())


        
        