import json
from collections import OrderedDict

import tweepy
from requests import PreparedRequest

from djx_account import settings


class TwitterService:

    @staticmethod
    def get_url(redirect_uri, oauth_state, **kwargs):
        req = PreparedRequest()
        if oauth_state:
            oauth_state = json.dumps(OrderedDict(oauth_state))
            req.prepare_url(redirect_uri, {"state": oauth_state})
            redirect_uri = req.url
        redirect_uri = redirect_uri.strip("/")
        auth = tweepy.OAuth1UserHandler(settings.TWITTER_API_KEY, settings.TWITTER_API_KEY_SECRET,
                                        callback=redirect_uri)
        return auth.get_authorization_url()

    @staticmethod
    def check_token(oauth_token, oauth_verifier, **kwargs):
        auth = tweepy.OAuthHandler(settings.TWITTER_API_KEY, settings.TWITTER_API_KEY_SECRET)
        auth.request_token = {
            "oauth_token": oauth_token,
            "oauth_token_secret": oauth_verifier
        }
        auth.get_access_token(verifier=oauth_verifier)
        auth.set_access_token(
            auth.access_token,
            auth.access_token_secret
        )
        api = tweepy.API(auth)
        data = api.verify_credentials(include_email=True, skip_status=True, include_entities=False)
        email = data.email
        return {
            "user": {
                "email": email
            }
        }
