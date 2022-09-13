from .ExchangeInterface import ExchangeInterface
from .con_utils import get, post


class GateIoExchange(ExchangeInterface):
    exchange_name = 'GATEIO'
    _base_url = 'https://api.gateio.ws/api/v4'

    def _transform_spot(self, data):
        pass

    def _parse_symbol(self, symbol):
        symbol.split('_')

    def _transform_market_ticker(self, obj):
        if type(obj) == type([]) and len(obj) > 2:
            temp_data = obj

            def m(item):
                c = item.copy()
                pair_names = item["currency_pair"].split('_')
                if len(pair_names) != 2:
                    return None
                c["baseCurrency"] = pair_names[0]
                c["quoteCurrency"] = pair_names[1]
                c["bid"] = item["highest_bid"]
                c["ask"] = item["lowest_ask"]
                return c

            def f(item):
                return item is not None and item["quoteCurrency"].lower() == "usd" or item["quoteCurrency"].lower() == "usdt"

            res = {
                "success": True,
                "result": list(filter(f, map(m, temp_data))),
            }
            return res

    def get_spot_markets(self):
        data = get(f'{self._base_url}/spot/tickers').json()
        return self._transform_market_ticker(data)

    def get_markets(self):
        pass

    def get_single_market(self, pair_name):
        pass

    def get_orderbook(self):
        pass