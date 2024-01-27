from routerfy.types.routerfy_config import Local

class AWSTemplate():
    def __init__(self,**kwargs):
        self.template_body: Local = {
            "AWSTemplateFormatVersion": kwargs.get("AWSTemplateFormatVersion", '2010-09-09'),
            "Transform": kwargs.get("Transform","AWS::Serverless-2016-10-31")
        }