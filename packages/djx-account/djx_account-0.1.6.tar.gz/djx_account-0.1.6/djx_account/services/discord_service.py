import datetime

import requests
from django.utils.timezone import now

from djx_account import settings


class DiscordService:

    @staticmethod
    def get_url(redirect_uri, *args, **kwargs):
        scopes = ["email", "guilds", "identify"]
        base_url = "https://discord.com/oauth2/authorize"
        req = requests.PreparedRequest()
        req.prepare_url(
            base_url, {
                "client_id": settings.DISCORD_CLIENT_ID,
                "redirect_uri": redirect_uri,
                "scope": " ".join(scopes),
                "response_type": "code"
            }
        )
        return req.url

    @staticmethod
    def check_token(code, redirect_uri, include_guilds=True, *args, **kwargs):
        base_url = "https://discord.com/api/v8/oauth2/token"
        data = {
            'client_id': settings.DISCORD_CLIENT_ID,
            'client_secret': settings.DISCORD_CLIENT_SECRET,
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': redirect_uri
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.post(base_url, data=data, headers=headers)
        response_data = response.json()
        access_token = response_data['access_token']
        refresh_token = response_data['refresh_token']
        expires_in = response_data['expires_in']
        expires_at = now() + datetime.timedelta(seconds=expires_in)
        user_data = DiscordService._get_user_data(access_token, include_guilds=include_guilds)
        return {
            "additional_data": {
                "discord_id": user_data['id'],
                "discord_guilds": user_data['guilds'],
            },
            "credentials": {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "expires_at": expires_at,
            },
            "user": {
                "username": user_data[settings.DISCORD_USERNAME_KEY],
                "email": user_data["email"]
            }
        }

    @staticmethod
    def _get_user_data(access_token, include_guilds=True):
        headers = {
            "Authorization": f'Bearer {access_token}'
        }
        user_request = requests.get('https://discordapp.com/api/users/@me', headers=headers)
        user_data = user_request.json()

        response = {
            **user_data,
            "guilds": DiscordService._get_user_guild(headers) if include_guilds else []
        }
        return response

    @staticmethod
    def _get_user_guild(headers):
        guilds_request = requests.get('https://discordapp.com/api/users/@me/guilds', headers=headers)
        guilds_data = guilds_request.json()
        guilds_data = [
            {
                "discord_id": guild['id'],
                "guild_name": guild['name'],
                "guild_permissions": guild['permissions'],
                "is_owner": guild['owner']
            } for guild in guilds_data
        ]
        return guilds_data
