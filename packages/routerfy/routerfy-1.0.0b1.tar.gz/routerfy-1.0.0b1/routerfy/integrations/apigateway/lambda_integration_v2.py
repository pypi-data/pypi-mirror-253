from typing import TypedDict, Union, Optional, List

class Validity(TypedDict):
    notBefore: str
    notAfter: str

class ClientCert(TypedDict):
    clientCertPem: str
    subjectDN: str
    issuerDN: str
    serialNumber: str
    validity: Validity

class Jwt(TypedDict):
    claims: Optional[Union[str, Union[str, int]]]
    scopes: Optional[List[str]]

class Authorizer(TypedDict):
    jwt: Jwt

class Http(TypedDict):
    method: str
    path: str
    protocol: str
    sourceIp: str
    userAgent: str

class RequestContext(TypedDict):
    accountId: str
    apiId: str
    authentication: ClientCert
    authorizer: Authorizer
    domainName: str
    domainPrefix: str
    http: Http
    requestId: str
    routeKey: str
    stage: str
    time: str
    timeEpoch: int

class LambdaIntegrationV2(TypedDict):
    routeKey: str
    rawPath: str
    rawQueryString: str
    cookies: list[str]
    headers: dict[str, Union[str, int]]    
    queryStringParameters: Optional[dict[str, Union[str, int]]]
    requestContext: RequestContext
    body: Optional[str]
    pathParameters: Optional[dict[str, Union[str, int]]]
    isBase64Encoded: bool
    stageVariables: Optional[dict[str, str]]