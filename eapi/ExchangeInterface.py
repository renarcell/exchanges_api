from abc import ABCMeta, abstractmethod

class ExchangeInterface(metaclass=ABCMeta):
    @property
    @abstractmethod
    def exchange_name(self):
        pass
    
    @property
    @abstractmethod
    def _base_url(self):
        pass

    @abstractmethod
    def get_markets(self):
        """Return all exchange pairs"""
        return {"success": True, "result": [
            {
                "name": "TONCOIN/USD",
                "baseCurrency": "TONCOIN",
                "quoteCurrency": "USD",
                "ask": 3949.25,
                "bid": 3949,
            }
        ]}

    @abstractmethod
    def get_single_market(self, pair_name):
        pass

    @abstractmethod
    def get_orderbook(self):
        """Return orderbook of pair
        {"success": bool, "result": {"bids": [[price, value]...], "asks": [[price, value]...]}}"""
        return {"success": True, "result": {"bids": [[0.974,372.1], [0.9735,142.8]], "asks": [[0.9755,379.7], [0.976,1202.0]]}}