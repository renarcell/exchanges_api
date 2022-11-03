import requests
from .exceptions import ClientError, ServerError


def get(url, params=None):
    res = requests.get(url, params=params)
    if 500 <= res.status_code < 600:
        raise ServerError(f'Response code:{res.status_code}')
    if not res:
        raise ClientError(f'Response code:{res.status_code}')
    return res


def post(url, data=None):
    res = requests.get(url, data=data)
    if 500 <= res.status_code < 600:
        raise ServerError(f'Response code:{res.status_code}')
    if not res:
        raise ClientError(f'Response code:{res.status_code}')
    return res

def get_json(url, method='GET'):
    if method == 'GET':
        try:
            data = get(url).json()
            return data
        except ValueError as e:
            raise ParseError(e)
    assert method == 'GET' or method == 'POST'

