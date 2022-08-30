from .ExchangeInterface import ExchangeInterface
from .con_utils import get, post


class MexcExchange(ExchangeInterface):
    exchange_name = 'MEXC'
    _base_url = 'https://www.mexc.com'

    def _transform_spot(self, data):
        pass

    def _parse_symbol(self, symbol):
        symbol.split('_')

    def _transform_market_ticker(self, obj):
        temp_data = obj['data']

        def m(item):
            c = item.copy()
            c["baseCurrency"] = item['symbol'].split('_')[0]
            c["quoteCurrency"] = item['symbol'].split('_')[1]
            c["price"] = (float(item['bid']) + float(item['ask'])) / 2
            return c

        def f(item):
            return item["quoteCurrency"].lower() == "usd" or item["quoteCurrency"].lower() == "usdt"

        res = {
            "success": obj['code'] == 200,
        }
        res["result"] = list(filter(f, map(m, temp_data)))
        return res

    def get_markets(self):
        get(f'{self._base_url}/markets')

    def get_merkets_with_price(self):
        get(f'{self._base_url}/markets')

    def get_spot_markets(self):
        data = get(f'{self._base_url}/open/api/v2/market/ticker').json()
        return self._transform_market_ticker(data)

    def get_single_market(self, pair_name):
        get(f'{self._base_url}/markets/{pair_name}')

    def get_orderbook(self):
        pass