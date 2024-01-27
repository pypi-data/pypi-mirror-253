from collections import namedtuple
import datetime as dt

SymbolDetail = namedtuple('SymbolDetail', 'symbol multiplier tick_size commission rth_start rth_end')

symbols = [
    SymbolDetail(symbol='@ES#', multiplier=50, tick_size=0.25, commission=1.61, rth_start=dt.time(9, 30),
                 rth_end=dt.time(16, 0)),
    SymbolDetail(symbol='QCL#', multiplier=1000, tick_size=0.01, commission=2.42, rth_start=None, rth_end=None),
]


def load_symbol_lookup() -> dict:
    lookup = dict()
    for detail in symbols:
        lookup[detail.symbol] = detail
    return lookup


