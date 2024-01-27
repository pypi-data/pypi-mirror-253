from typing import TypedDict, List, Optional, Union

class AccessLogSetting(TypedDict):
    DestinationArn: str
    Format: str

class Definition(TypedDict):
    Bucket: str
    Key: str
    Version: str

class CorsConfiguration(TypedDict):
    AllowCredentials: bool
    AllowHeaders: str
    AllowMethods: str
    AllowOrigins: str
    MaxAge: str

class Map(TypedDict):
    key: str
    value: str

class DomainConfiguration(TypedDict):
    BasePath: Optional[List]
    NormalizeBasePath: Optional[bool]
    CertificateArn: str
    DomainName: str
    EndpointConfiguration: Optional[str]
    MutualTlsAuthentication: dict #Must be a MutualTlsAuthentication type TODO create type
    OwnershipVerificationCertificateArn: str
    Route53: dict #Must be a Route53Configuration type TODO create type
    SecurityPolicy: str

class MethodSettings(TypedDict):
    CacheDataEncrypted: Optional[bool]
    CacheTtlInSeconds: Optional[int]
    CachingEnabled: Optional[bool]
    DataTraceEnabled: Optional[bool]
    HttpMethod: Optional[str]
    LoggingLevel: Optional[str]
    MetricsEnabled: Optional[bool]
    ResourcePath: Optional[str]
    ThrottlingBurstLimit: Optional[int]
    ThrottlingRateLimit: Optional[float]

class EndpointConfiguration(TypedDict):
    Type: Optional[str]
    VPCEndpointIds: Optional[List]

class AWSServerlessApi(TypedDict):
    AccessLogSetting: Optional[AccessLogSetting]
    AlwaysDeploy: Optional[bool]
    ApiKeySourceType: Optional[str]
    Auth: Optional[str]
    BinaryMediaTypes: Optional[List[str]]
    CacheClusterEnabled: Optional[bool]
    CacheClusterSize: Optional[str]
    Cors: Union[str,CorsConfiguration]
    DefinitionBody: Optional[dict]
    DefinitionUri: Optional[Union[str,Definition]]
    Description: Optional[str]
    DisableExecuteApiEndpoint: Optional[bool]
    Domain: Optional[DomainConfiguration]
    EndpointConfiguration: Optional[EndpointConfiguration]
    FailOnWarnings: Optional[bool]
    GatewayResponses: Optional[dict]
    MergeDefinitions: Optional[bool]
    MethodSettings: Optional[MethodSettings]
    MinimumCompressionSize: Optional[int]
    Mode: Optional[str]
    Models: Optional[dict]
    Name: Optional[str]
    OpenApiVersion: Optional[str]
    PropagateTags: Optional[bool]
    StageName: str
    Tags: Optional[List[Map]]
    TracingEnabled: Optional[bool]
    Variables: Optional[List[Map]]