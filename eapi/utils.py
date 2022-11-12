from urllib.parse import urljoin
from .exceptions import ServerError, ClientError, ParseError


class BaseUrl:
    def __init__(self, base_url):
        self.base_url = base_url

    def __str__(self):
        return self.base_url

    def __repr__(self):
        return self.base_url

    def __add__(self, other):
        return urljoin(self.base_url, other)


def check_data(data):
    if 'result' not in data or 'success' not in data:
        raise ParseError("'result' not in data or 'success' not in data")
    if not data['success']:
        raise ParseError("Success is FALSE")
    if not isinstance(data['result'], list) or len(data['result']) < 2:
        raise ServerError("not isinstance(res['result'], list) or len(res['result']) < 2")
    return True


def delete_excess_fields(item):
    return {
        "name": item["name"],
        "baseCurrency": item["baseCurrency"],
        "quoteCurrency": item["quoteCurrency"],
        "ask": item["ask"],
        "bid": item["bid"],
    }


def etf_filter(data):
    etf = ['3S', '3L', '5S', '5L']
    def f(data):
        for d in data:
            chars = d['baseCurrency'][-2:]
            if cars in etf:
                return False
            return True

    return list(filter(f, data))
