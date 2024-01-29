import datetime
import requests
from django.utils.timezone import now
from djx_account import settings
from google.auth.transport import requests as google_request
from google.oauth2 import id_token
from djx_account.utils.error_messages import ErrorMessage
from djx_account.utils.exceptions import BadRequestException
from datetime import date


class GoogleService:

    @staticmethod
    def get_url(redirect_uri, **kwargs):
        client_id = settings.GOOGLE_CLIENT_ID
        base_url = "https://accounts.google.com/o/oauth2/auth"

        scope = " ".join([
            "https://www.googleapis.com/auth/userinfo.email",
            "https://www.googleapis.com/auth/userinfo.profile",
            "https://www.googleapis.com/auth/user.birthday.read",
            "https://www.googleapis.com/auth/user.phonenumbers.read"

        ])
        req = requests.PreparedRequest()
        req.prepare_url(base_url,
                        {"client_id": client_id,
                         "redirect_uri": redirect_uri,
                         "scope": scope,
                         "response_type": "code"})
        return req.url

    @staticmethod
    def check_token(code, redirect_uri, **kwargs):
        response = requests.post(
            url="https://oauth2.googleapis.com/token",
            data={"code": code, "client_id": settings.GOOGLE_CLIENT_ID,
                  "redirect_uri": redirect_uri,
                  "client_secret": settings.GOOGLE_CLIENT_SECRET,
                  "grant_type": "authorization_code"},
        )
        if response.status_code != 200:
            raise BadRequestException(ErrorMessage.invalid_code)

        data = response.json()
        token = data['id_token']
        token_data = id_token.verify_oauth2_token(token, google_request.Request(), clock_skew_in_seconds=10)
        expires_in = data['expires_in']
        expires_at = now() + datetime.timedelta(seconds=expires_in)

        birth_date = GoogleService.get_birthdate(data)

        first_name = token_data.get("given_name", "")
        last_name = token_data.get("family_name", "")
        return {
            "user": {
                "email": token_data["email"],
                "username": token_data["email"],
                "first_name": first_name,
                "last_name": last_name,
                "birth_date": birth_date
            },
            "credentials": {
                "access_token": data['access_token'],
                "expires_at": expires_at,
            },
            "additional_data": {
                "email_verified": token_data["email_verified"]
            }
        }

    @staticmethod
    def get_birthdate(data):
        access_token = data['access_token']
        people_api_url = "https://people.googleapis.com/v1/people/me?personFields=birthdays"
        headers = {"Authorization": f"Bearer {access_token}"}
        people_response = requests.get(people_api_url, headers=headers)

        if people_response.status_code == 200:
            people_data = people_response.json()
            birthdays = people_data.get('birthdays', [])
            for birthday in birthdays:
                if 'date' in birthday and 'year' in birthday['date']:
                    birthday_date = birthday["date"]
                    year = birthday_date.get("year")
                    month = birthday_date.get("month", 1)
                    day = birthday_date.get("day", 1)
                    formatted_date = date(year, month, day)
                    return formatted_date
        return None

    @staticmethod
    def get_phone_number(data):
        access_token = data['access_token']
        people_api_url = "https://people.googleapis.com/v1/people/me?personFields=phoneNumbers"
        headers = {"Authorization": f"Bearer {access_token}"}
        people_response = requests.get(people_api_url, headers=headers)

        phone_number = None  # Définir par défaut à None
        if people_response.status_code == 200:
            people_data = people_response.json()
            phone_numbers = people_data.get('phoneNumbers', [])
            print(phone_numbers)
            if phone_numbers:
                # Prendre le premier numéro de téléphone disponible
                phone_number = phone_numbers[0].get('value')
                print(phone_numbers)
