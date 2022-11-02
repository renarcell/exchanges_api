from .ExchangeInterface import ExchangeInterface
from .con_utils import get, post
from .utils import BaseUrl, check_data, delete_excess_fields


class BitMartExchange(ExchangeInterface):
    exchange_name = 'BITMART'
    _base_url = 'https://api-cloud.bitmart.com'

    def _transform_spot(self, data):
        pass

    def _parse_symbol(self, symbol):
        symbol.split('_')

    def _transform_market_ticker(self, obj):
        if obj["message"] == "OK":
            temp_data = obj['data']['tickers']

            def m(item):
                c = item.copy()
                c["baseCurrency"] = item['symbol'].split('_')[0]
                c["quoteCurrency"] = item['symbol'].split('_')[1]
                c["bid"] = item["best_bid"]
                c["ask"] = item["best_ask"]
                return c

            def f(item):
                return item["quoteCurrency"].lower() == "usd" or item["quoteCurrency"].lower() == "usdt"

            res = {
                "success": obj["message"] == "OK",
                "result": list(filter(f, map(m, temp_data))),
            }
            return res

    def get_spot_markets(self):
        data = get(f'{self._base_url}/spot/v1/ticker').json()
        return self._transform_market_ticker(data)

    def get_markets(self):
        pass

    def get_single_market(self, pair_name):
        pass

    def get_orderbook(self):
        pass
