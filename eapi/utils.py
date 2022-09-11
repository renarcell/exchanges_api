from .FtxExchange import FtxExchange
from .MexcExchange import MexcExchange
from .ExmoExchange import ExmoExchange
from .BitMartExchange import BitMartExchange

def get_all_exchanges():
    return [
        FtxExchange(),
        MexcExchange(),
        ExmoExchange(),
        BitMartExchange(),
    ]