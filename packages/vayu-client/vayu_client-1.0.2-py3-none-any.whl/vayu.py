from typing import List

from openapi_client.api import auth_api, events_api
from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration
from openapi_client.models import EventInput
from openapi_client.models.login_request import LoginRequest
from openapi_client.models.send_events_request import SendEventsRequest
from vayu_consts import VAYU_URL


class Vayu:
    def __init__(self, api_key: str):
        self.__login(api_key)
    
    def send_events(self, events: List[EventInput]):
        """
        Send events to Weft

        Args:
            events ([EventInput]): events to send
        """

        events_api = self.__build_events_api(VAYU_URL)
        send_events_request = SendEventsRequest(events=events)

        return events_api.send_events(send_events_request)

    def __login(self, api_key: str):
        auth_api = self.__build_auth_api(VAYU_URL)
        refresh_token_input = LoginRequest(refreshToken=api_key)

        refresh_response = auth_api.login(refresh_token_input)

        self.__access_token = refresh_response.token
    
    def __build_auth_api(self, host: str):
        configuration = Configuration(host)
        client = ApiClient(configuration)
        
        return auth_api.AuthApi(client)

    def __build_events_api(self, host: str):
        configuration = Configuration(host=host)
        client = ApiClient(configuration, header_name='Authorization', header_value=f'Bearer {self.__access_token}')
        
        return events_api.EventsApi(client)
