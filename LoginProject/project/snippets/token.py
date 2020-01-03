import datetime
import pdb

import jwt
import requests
from project.settings import SECRET_KEY, AUTH_ENDPOINT


def token_activation(username, password):
   

    data = {
        'username': username,
        'password': password,
        'exp': datetime.datetime.now()+datetime.timedelta(days=2)
    }
    token = jwt.encode(data, SECRET_KEY, algorithm="HS256").decode('utf-8')
    return token


def token_validation(username, password):

    data = {
        'username': username,
        'password': password
    }
    tokson = requests.post(AUTH_ENDPOINT, data=data)
    token = tokson.json()['access']
    return token



from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six
class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )
account_activation_token = TokenGenerator()