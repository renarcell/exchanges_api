from .FtxExchange import FtxExchange
from .MexcExchange import MexcExchange
from .ExmoExchange import ExmoExchange

def get_all_exchanges():
    return [
        FtxExchange(),
        MexcExchange(),
        ExmoExchange(),
    ]