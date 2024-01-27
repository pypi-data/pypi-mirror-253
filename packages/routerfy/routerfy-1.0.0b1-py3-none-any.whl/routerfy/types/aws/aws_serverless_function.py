from typing import TypedDict, List, Union, Optional

class FunctionCode(TypedDict):
    Bucket: str
    Key: str
    Version: str
    
class DeadLetterQueue(TypedDict):
    TargetArn: str
    Type: str
    
class Hooks(TypedDict):
    PostTraffic: str
    PreTraffic: str
    
class DeploymentPreference(TypedDict):
    Alarms: List
    Enabled: bool
    Hooks: Hooks
    PassthroughCondition: bool
    Role: str
    TriggerConfigurations: List
    Type: str

class Environment(TypedDict):
    Variables: dict

class EphemeralStorage(TypedDict):
    Size: int

class EventInvokeDestinationConfigurationGenericEvent(TypedDict):
    Destination: str
    Type: str

class EventInvokeDestinationConfiguration(TypedDict):
    OnFailure: EventInvokeDestinationConfigurationGenericEvent
    OnSuccess: EventInvokeDestinationConfigurationGenericEvent

class EventInvokeConfiguration(TypedDict):
    DestinationConfig: EventInvokeDestinationConfiguration
    MaximumEventAgeInSeconds: int
    MaximumRetryAttempts: int
    
class ResourcePolicyStatement(TypedDict):
    AwsAccountBlacklist: List
    AwsAccountWhitelist: List
    CustomStatements: List
    IntrinsicVpcBlacklist: List
    IntrinsicVpcWhitelist: List
    IntrinsicVpceBlacklist: List
    IntrinsicVpceWhitelist: List
    IpRangeBlacklist: List
    IpRangeWhitelist: List
    SourceVpcBlacklist: List
    SourceVpcWhitelist: List
    
class ApiFunctionAuth(TypedDict):
    ApiKeyRequired: bool
    AuthorizationScopes: List
    Authorizer: str
    InvokeRole: str
    OverrideApiAuth: bool
    ResourcePolicy: ResourcePolicyStatement
    
class RequestModel(TypedDict):
    Model: str
    Required: bool
    ValidateBody: bool
    ValidateParameters: bool
    
class RequestParameter(TypedDict):
    Caching: bool
    Required: bool
    
class Api(TypedDict):
    Auth: ApiFunctionAuth
    Method: str
    Path: str
    RequestModel: RequestModel
    RequestParameters: List[Union[str, RequestParameter]]
    RestApiId: str
    TimeoutInMillis: int
    
class EventSource(TypedDict):
    Type: str
    Properties: Api
    
class Cors(TypedDict):
    AllowCredentials: bool
    AllowHeaders: List[str]
    AllowMethods: List[str]
    AllowOrigins: List[str]
    ExposeHeaders: List[str]
    MaxAge: int
    
class FunctionUrlConfig(TypedDict):
    AuthType: str
    Cors: Cors
    InvokeMode: str
    
class ImageConfig(TypedDict):
    Command: List[str]
    EntryPoint: List[str]
    WorkingDirectory: str
    
class LoggingConfig(TypedDict):
    ApplicationLogLevel: str
    LogFormat: str
    LogGroup: str
    SystemLogLevel: str

class ProvisionedConcurrencyConfig(TypedDict):
    ProvisionedConcurrentExecutions: int
    
class RuntimeManagementConfig(TypedDict):
    RuntimeVersionArn: str
    UpdateRuntimeOn: str

class SnapStart(TypedDict):
    ApplyOn: str

class VpcConfig(TypedDict):
    Ipv6AllowedForDualStack: bool
    SecurityGroupIds: List[str]
    SubnetIds: List[str]

class AWSServerlessFunction(TypedDict):
    Architectures: Optional[List]
    AssumeRolePolicyDocument: Optional[dict]
    AutoPublishAlias: Optional[str]
    AutoPublishAliasAllProperties: Optional[bool]
    AutoPublishCodeSha256: Optional[str]
    CodeSigningConfigArn: Optional[str]
    CodeUri: Union[str, FunctionCode]
    DeadLetterQueue: Optional[Union[dict, DeadLetterQueue]]
    DeploymentPreference: Optional[DeploymentPreference]
    Description: Optional[str]
    Environment: Optional[Environment]  
    EphemeralStorage: Optional[EphemeralStorage]
    EventInvokeConfig: Optional[EventInvokeConfiguration]
    Events: List[EventSource]
    FileSystemConfigs: Optional[List]
    FunctionName: str
    FunctionUrlConfig: Optional[FunctionUrlConfig]
    Handler: str
    ImageConfig: Optional[ImageConfig]
    ImageUri: Optional[str]
    InlineCode: Optional[str]
    KmsKeyArn: str
    Layers: List
    LoggingConfig: LoggingConfig
    MemorySize: int
    PackageType: str
    PermissionsBoundary: str
    Policies: List[str | List | List[dict]]
    PropagateTags: bool
    ProvisionedConcurrencyConfig: ProvisionedConcurrencyConfig
    ReservedConcurrentExecutions: int
    Role: str
    RolePath: str
    Runtime: str
    RuntimeManagementConfig: RuntimeManagementConfig
    SnapStart: SnapStart
    Tags: dict
    Timeout: int
    Tracing: str
    VersionDescription: str
    VpcConfig: VpcConfig