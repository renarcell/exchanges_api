from .ExchangeInterface import ExchangeInterface
from .con_utils import get, post

class FtxExchange(ExchangeInterface):
    exchange_name = 'FTX'
    _base_url = 'https://ftx.com/api'

    def get_markets(self):
        get(f'{self._base_url}/markets')

    def get_merkets_with_price(self):
        get(f'{self._base_url}/markets')
        
    def get_spot_markets(self):
        res = get(f'{self._base_url}/markets').json()
        res['result'] = list(filter(lambda x: (x['baseCurrency'] != None) and x['quoteCurrency'] == 'USD', res['result']))
        return res
    
    def get_single_market(self, pair_name):
        get(f'{self._base_url}/markets/{pair_name}')

    def get_orderbook(self):
        pass