from typing import TypedDict, Optional, List, Union

class Cors(TypedDict):
    AllowCredentials: Optional[bool]
    AllowHeaders: Optional[List[str]]
    AllowMethods:  Optional[List[str]]
    AllowOrigins: Optional[List[str]]
    ExposeHeaders: Optional[List[str]]
    MaxAge: Optional[int]
    
class ApiConfig(TypedDict):
    Name: Optional[str]
    StageName: str
    BuildModel: Optional[bool]
    Cors: Optional[Cors]

class RoutesConfig(TypedDict):
    Dir: Optional[str]
    
class MetadataDescription(TypedDict):
    Description: str
    
class Metadata(TypedDict):
    Instances: MetadataDescription
    Databases: MetadataDescription
    
class Parameter(TypedDict):
    Type: Union[str, int, List[int], List[str]]
    AllowedPattern: Optional[str]
    AllowedValues: Optional[List[str]]
    ConstraintDescription: Optional[str]
    Default: Optional[str]
    Description: Optional[str]
    MaxLength: Optional[int]
    MaxValue: Optional[int]
    MinLength: Optional[int]
    MinValue: Optional[int]
    NoEcho: Optional[bool]
    
class Resource(TypedDict):
    Type: str
    Properties: dict
    
class Export(TypedDict):
    Name: str
    
class Output(TypedDict):
    Description: Optional[str]
    Value: Union[str, int, dict, List]
    Export: Optional[Export]
    
class Global(TypedDict):
    AWSTemplateFormatVersion: Optional[str]
    Description: Optional[str]
    Metadata: Optional[Metadata]
    Parameters: Optional[dict[str, Parameter]]
    Rules: Optional[dict]
    Mappings: Optional[dict]
    Conditions: Optional[dict[str, dict[str, Optional[List]]]]
    Transform: Optional[List[str]]
    
class Local(TypedDict):
    AWSTemplateFormatVersion: Optional[str]
    Description: Optional[str]
    Metadata: Optional[Metadata]
    Parameters: Optional[dict[str, Parameter]]
    Rules: Optional[dict]
    Mappings: Optional[dict]
    Conditions: Optional[dict[str, dict[str, Optional[List]]]]
    Transform: Optional[List[str]]
    Resources: Optional[dict[str, Resource]]
    Outputs: Optional[dict[str, Output]]
    
class RouterfyConfig(TypedDict):
    AppName: str
    Api: Optional[ApiConfig]
    Routes: Optional[RoutesConfig]
    Global: Optional[Global]
    Local: Optional[dict[str, Local]]
    GlobalLambdaProperties: Optional[dict]
    LocalLambdaProperties: Optional[dict[str, dict]]