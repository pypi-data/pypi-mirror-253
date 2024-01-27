from json import dumps
from typing import Any, Optional, Mapping

class Response():
    def __init__(
            self, 
            content: Any = None,
            status_code: int = 200,
            headers: Optional[Mapping[str, str]] = None,
            media_type: Optional[str] = None
        ):
        
        if headers is None:
            headers = {
                "Content-Type": "application/json"
            }
            
        self._content = dumps(content)
        self._status_code = status_code
        self._headers = headers
        self._media_type = media_type
        
    @property
    def content(self):
        return self._content
    
    @property
    def status_code(self):
        return self._status_code
    
    @property
    def headers(self):
        return self._headers
    
    @property
    def media_type(self):
        return self._media_type