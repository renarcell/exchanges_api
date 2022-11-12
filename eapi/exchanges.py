from .FtxExchange import FtxExchange
from .FtxExchange import FtxExchange
from .MexcExchange import MexcExchange
from .ExmoExchange import ExmoExchange
from .BitMartExchange import BitMartExchange
from .GateIoExchange import GateIoExchange


def get_all_exchanges():
    return [
        MexcExchange(),
        ExmoExchange(),
        BitMartExchange(),
        GateIoExchange(),
    ]