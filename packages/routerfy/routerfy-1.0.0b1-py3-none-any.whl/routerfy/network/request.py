from json import loads
from routerfy.network.url import URL

class Request():
    def __init__(self, *,
        httpMethod: str,
        path: str,
        headers: dict = None,
        rawQueryString: str = None,
        queryStringParameters: dict = None,
        pathParameters: dict = None,
        body: str = None,
        cookies: dict
        ):
        
        self._method = httpMethod
        self._url = URL(scheme="https", path=path, query=rawQueryString)
        self._headers = headers
        self._query_params = queryStringParameters
        self._path_params = pathParameters
        self._body = body
        self._cookies = cookies

    @property
    def method(self):
        return self._method
    
    @property
    def url(self):
        return self._url
    
    @property
    def headers(self):
        return self._headers
    
    @property
    def query_params(self):
        return self._query_params
    
    @property
    def path_params(self):
        return self._path_params
    
    @property
    def cookies(self):
        return self._cookies
    
    def body(self):
        return self._body if isinstance(self._body, bytes) else self._body.encode('utf-8') 
    
    def json(self):
        return loads(self._body)