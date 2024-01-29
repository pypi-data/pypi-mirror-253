import json
from collections import OrderedDict

import requests

try:
    import msal
except ModuleNotFoundError:
    pass
from djx_account import settings

from djx_account.services.oauth_service_interface import OauthServiceInterface
from djx_account.utils.error_messages import ErrorMessage
from djx_account.utils.exceptions import BadRequestException


class MicrosoftService(OauthServiceInterface):

    @staticmethod
    def get_url(redirect_uri, oauth_state, **kwargs):
        app = msal.ConfidentialClientApplication(
            client_id=settings.MICROSOFT_CLIENT_ID,
            client_credential=settings.MICROSOFT_SECRET
        )
        data = {
            'scopes': ['email', 'User.Read'],
            'redirect_uri': redirect_uri
        }
        if oauth_state:
            data['state'] = json.dumps(OrderedDict(oauth_state))
        url = app.get_authorization_request_url(**data)
        return url

    @staticmethod
    def check_token(code, redirect_uri, **kwargs):
        app = msal.ConfidentialClientApplication(
            client_id=settings.MICROSOFT_CLIENT_ID,
            client_credential=settings.MICROSOFT_SECRET
        )
        data = {
            'code': code,
            'scopes': ['email', 'User.Read'],
            'redirect_uri': redirect_uri
        }
        result = app.acquire_token_by_authorization_code(**data)
        try:
            claims = result['id_token_claims']
        except KeyError:
            raise BadRequestException(detail=ErrorMessage.invalid_code)
        user_info = MicrosoftService.get_user_info_from_graph(result["access_token"])
        email = claims['email'] if 'email' in claims else None
        response = {
            "user": {
                **user_info,
                "email": email
            }
        }
        return response

    @staticmethod
    def get_user_info_from_graph(access_token):
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        graph_response = requests.get('https://graph.microsoft.com/v1.0/me', headers=headers)
        if graph_response.status_code == 200:
            user_data = graph_response.json()
            return {
                "email": user_data.get('mail', ''),
                "first_name": user_data.get('givenName', ''),
                "last_name": user_data.get('surname', '')
            }
