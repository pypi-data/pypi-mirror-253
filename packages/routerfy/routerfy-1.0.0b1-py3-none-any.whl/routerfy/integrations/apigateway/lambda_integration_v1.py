from typing import TypedDict, Union, List, Optional

class Authorizer(TypedDict):
    claims: Optional[dict[str, Union[str, int]]]
    scopes: Optional[list[str]]
    
class Validity(TypedDict):
    notBefore: str
    notAfter: str
    
class ClientCert(TypedDict):
    clientCertPem: str
    subjectDN: str
    issuerDN: str
    serialNumber: str
    validity: Validity

class Identity(TypedDict):
    accessKey: Optional[str]
    accountId: Optional[str]
    caller: Optional[str]
    cognitoAuthenticationProvider: Optional[str]
    cognitoAuthenticationType: Optional[str]
    cognitoIdentityId: Optional[str]
    cognitoIdentityPoolId: Optional[str]
    principalOrgId: Optional[str]
    sourceIp: str
    user: Optional[str]
    userAgent: str
    userArn: Optional[str]
    clientCert: ClientCert
    

class RequestContext(TypedDict):
    accountId: str
    apiId: str
    authorizer: Authorizer
    domainName: str
    domainPrefix: str
    extendedRequestId: str
    httpMethod: str
    identity: Identity
    path: str
    protocol: str
    requestId: str
    requestTime: str
    requestTimeEpoch: int
    resourceId: Optional[str]
    resourcePath: str
    stage: str
    
class LambdaIntegrationV1(TypedDict):
    resource: str
    path: str
    httpMethod: str
    headers: Optional[dict[str, Union[str, int]]]
    multiValueHeaders: Optional[dict[str, List[Union[str, int]]]]
    queryStringParameters: Optional[dict[str, Union[str, int]]]
    multiValueQueryStringParameters: Optional[dict[str, List[Union[str, int]]]]
    requestContext: RequestContext
    pathParameters: Optional[dict[str, Union[str, int]]]
    stageVariables: Optional[dict[str, Union[str, int]]]
    body: Optional[str]
    isBase64Encoded: bool
    