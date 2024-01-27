class APIRouterNotFound(Exception):
    def __init__(self, lambda_path: str):
        self.lambda_path = lambda_path
        super().__init__("Cannot find an valid API Router object in the module: {}".format(lambda_path))