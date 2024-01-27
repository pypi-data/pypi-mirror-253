from routerfy.exceptions import InvalidBody

class BaseModel:
    def __init__(self, **kwargs):
        self._name = kwargs.get("arg_name", "")
        
        body = kwargs.get("body", {})
        
        if len(body.keys()) > 0:
            if self._name in body.keys():
                self._body = body[self.name]
            else:
                self._body = body
            
            self._validate_body()
    
    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        
    
    def _check_optional_annotation(self, annotation_key: str):
        is_optional = str(self.__annotations__[annotation_key]).find("Optional") != -1 or str(self.__annotations__[annotation_key]).find("None") != -1
        
        if not is_optional:
            raise InvalidBody(name=self._name, body_model={annotation_key: str(self.__annotations__[annotation_key])})
        
    def _validate_body(self):
        for key in self.__annotations__.keys():
                        
            if self._body.get(key, None) is None:
                self._check_optional_annotation(key)
                
            self.__setattr__(key, self._body[key])