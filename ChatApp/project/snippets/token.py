import datetime
import pdb

import jwt
import requests
from project.settings import SECRET_KEY, AUTH_ENDPOINT

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six


def token_activation(username, password):
   

    data = {
        'username': username,
        'password': password,
        'exp': datetime.datetime.now()+datetime.timedelta(days=2)
    }
    token = jwt.encode(data, SECRET_KEY, algorithm="HS256").decode('utf-8')
    return token


