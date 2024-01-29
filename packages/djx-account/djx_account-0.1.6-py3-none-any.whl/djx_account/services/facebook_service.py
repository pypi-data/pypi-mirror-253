import json
from collections import OrderedDict

import facebook

from djx_account import settings
from djx_account.services.oauth_service_interface import OauthServiceInterface


class FacebookService(OauthServiceInterface):

    @staticmethod
    def get_url(redirect_uri, oauth_state=None, **kwargs):
        if not oauth_state:
            oauth_state = {}
        data = {
            'app_id': settings.FACEBOOK_CLIENT_ID,
            'canvas_url': redirect_uri,
            'perms': ['email', 'public_profile', ]
        }
        if oauth_state:
            data['state'] = json.dumps(OrderedDict(oauth_state))

        url = facebook.GraphAPI().get_auth_url(
            **data
        )
        return url

    @staticmethod
    def check_token(code, redirect_uri, **kwargs):
        api = facebook.GraphAPI().get_access_token_from_code(
            code, redirect_uri,
            settings.FACEBOOK_CLIENT_ID,
            settings.FACEBOOK_SECRET)
        access_token = api['access_token']
        fields = 'email,id,first_name,last_name,birthday'
        me = facebook.GraphAPI(access_token=access_token).get_object('me', **{"fields": fields})
        return {
            "user": me
        }
