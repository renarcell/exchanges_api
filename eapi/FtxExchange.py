from .ExchangeInterface import ExchangeInterface
from .con_utils import get, post, get_json
from .exceptions import ServerError, ClientError, ParseError
from .utils import check_data, delete_excess_fields

class FtxExchange(ExchangeInterface):
    exchange_name = 'FTX'
    _base_url = 'https://ftx.com/api'

    def get_markets(self):
        get(f'{self._base_url}/markets')

    def get_merkets_with_price(self):
        get(f'{self._base_url}/markets')

    def get_spot_markets(self):
        data = get_json(f'{self._base_url}/markets')
        check_data(data)
        data = {
            "success": data["success"],
            "result": map(delete_excess_fields, data["result"])
        }
        check_data(data)
        data['result'] = list(filter(lambda x: x['type'] != "spot" or x['baseCurrency'] != None, data['result']))
        return data

    def get_single_market(self, pair_name):
        get(f'{self._base_url}/markets/{pair_name}')

    def get_orderbook(self):
        pass