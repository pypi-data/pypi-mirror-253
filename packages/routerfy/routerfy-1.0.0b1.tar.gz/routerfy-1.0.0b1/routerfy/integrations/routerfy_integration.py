from typing import Union, Literal
from functools import reduce

from routerfy.integrations.apigateway import LambdaIntegrationV1, LambdaIntegrationV2
from routerfy.network import Request

class RouterfyIntegration:
    def __init__(self, event: Union[LambdaIntegrationV1, LambdaIntegrationV2]):
        
        self._unparsed_event = event
        self._api_version = self.__check_event_version(event)
        
    @property
    def api_version(self):
        return self._api_version
        
    def __check_event_version(self, event: Union[LambdaIntegrationV1, LambdaIntegrationV2]) -> Literal['v1', 'v2']:
        
        event_keys = set(event.keys())

        lambda_integrations = [LambdaIntegrationV1, LambdaIntegrationV2]
        
        all_common_keys = [len(event_keys.intersection(set(lambda_integration.__annotations__.keys()))) for lambda_integration in lambda_integrations]

        if reduce(lambda x, y: x+y, all_common_keys) == 0:
            raise TypeError("Cannot determine event version for event: {}".format(event))
        
        max_common_key = all_common_keys[0]
        version = 'v1'
        
        for [index, common_key] in enumerate(all_common_keys):
            if common_key > max_common_key:
                version = f"v{index+1}"
        
        return version

    def get_request(self):
        """
            Convert aws proxy event to Routerfy Request.
        """
        if self.api_version == 'v1':
            return self.convert_v1_to_routerfy(self._unparsed_event)
        
        elif self.api_version == 'v2':
            return self.convert_v2_to_routerfy(self._unparsed_event)
        
        raise TypeError("Cannot determine version for event: {}".format(self._unparsed_event))
        
    def convert_v1_to_routerfy(self, event: LambdaIntegrationV1) -> Request:
        return Request(
            httpMethod=event['httpMethod'],
            path=event['resource'],
            headers=event['headers'],
            queryStringParameters=event['queryStringParameters'],
            rawQueryString="&".join([f"{key}={event['queryStringParameters'][key]}" for key in event['queryStringParameters'].keys()]) if event['queryStringParameters'] else None,
            pathParameters=event['pathParameters'],
            body=event['body'],
            cookies=None
        )

    def convert_v2_to_routerfy(self, event: LambdaIntegrationV2) -> Request:
        Request(
            httpMethod=event['requestContext']['http']['method'],
            path=event['requestContext']['http']['path'],
            headers=event['headers'],
            queryStringParameters=event['queryStringParameters'],
            rawQueryString=event['rawQueryString'],
            pathParameters=event['pathParameters'],
            body=event['body'],
            cookies={f"{cookie[0]}": f"{cookie[1]}" for cookie in [cookie.split("=") for cookie in event['cookies']]}
        )


        



