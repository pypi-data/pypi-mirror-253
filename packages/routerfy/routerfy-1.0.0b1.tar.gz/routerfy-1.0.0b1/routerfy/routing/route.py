import re
import inspect
from typing import Callable, Any

class Route():
    def __init__(self, method: str, path: str, callback: Callable[..., Any]):

        assert isinstance(path, str), "A path must be a string"
        assert path.startswith("/"), "A path prefix must start with '/'"
        self._name = callback.__name__
        self._method = method
        self._path = path if not re.search("{\w+}", path) else path.replace("}", "+}")
        self._args = inspect.getfullargspec(callback).annotations
        self._callback = callback
        
    @property
    def name(self):
        return self._name

    @property
    def path(self):
        return self._path
    
    @property
    def method(self):
        return self._method
    
    @property
    def args(self):
        return self._args
    
    @property
    def callback(self):
        return self._callback
