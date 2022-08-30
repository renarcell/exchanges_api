import requests
from requests.exceptions import RequestException


def get(url, params=None):
    res = requests.get(url, params=params)
    if not res:
        raise RequestException(f'Response code:{res.status_code}')
    return res


def post(url, data=None):
    res = requests.get(url, data=data)
    if not res:
        raise RequestException(f'Response code:{res.status_code}')
    return res
