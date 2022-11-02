from .ExchangeInterface import ExchangeInterface
from .con_utils import get, post
from .utils import BaseUrl, check_data, delete_excess_fields


class ExmoExchange(ExchangeInterface):
    exchange_name = 'EXMO'
    _base_url = 'https://api.exmo.com/v1.1'

    def parse_pair_name(self, pair_name):
        return pair_name.split('_')

    def _transform_exmo_ticker(self, response_json):
        res = {}
        if len(response_json) > 2:
            res["success"] = True
            result_array = []
            for crypt_name in response_json:
                crypt_obj = {}
                crypt_obj["baseCurrency"] = self.parse_pair_name(crypt_name)[0]
                crypt_obj["quoteCurrency"] = self.parse_pair_name(crypt_name)[1]
                crypt_obj["name"] = f'{crypt_obj["baseCurrency"]}/{crypt_obj["quoteCurrency"]}'
                crypt_obj["bid"] = response_json[crypt_name]["buy_price"]
                crypt_obj["ask"] = response_json[crypt_name]["sell_price"]
                result_array.append(crypt_obj)
            res["result"] = result_array
        return res

    def get_markets(self):
        pass

    def get_merkets_with_price(self):
        pass

    def get_spot_markets(self):
        res = get(f'{self._base_url}/ticker').json()
        transformed_res = self._transform_exmo_ticker(res)
        transformed_res['result'] = list(
            filter(lambda x: (x['baseCurrency'] != None) and x['quoteCurrency'] == 'USDT', transformed_res['result']))
        return transformed_res

    def get_single_market(self, pair_name):
        pass
        #get(f'{self._base_url}/markets/{pair_name}')

    def get_orderbook(self):
        pass