from .FtxExchange import FtxExchange
from .MexcExchange import MexcExchange

def get_all_exchanges():
    return [
        FtxExchange(),
        MexcExchange(),
    ]