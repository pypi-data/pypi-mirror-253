class URL():
    def __init__(self, scheme: str = None, path: str = None, query: str = None):
        self._scheme = scheme
        self._path = path
        self._query = query
    
    @property
    def scheme(self):
        return self._scheme
    
    @property
    def path(self):
        return self._path
    
    @property
    def query(self):
        return self._query