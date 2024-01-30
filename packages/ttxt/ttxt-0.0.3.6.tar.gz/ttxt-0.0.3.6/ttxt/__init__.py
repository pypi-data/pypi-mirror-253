from ttxt.base import baseFuturesExchange, baseSpotExchange
from ttxt.exchanges.gateFutures import gateFutures
from ttxt.exchanges.bybitFutures import bybitFutures
from ttxt.exchanges.bitgetFutures import bitgetFutures
from ttxt.exchanges.bingx import bingx
from ttxt.exchanges.biconomy import biconomy
from ttxt.exchanges.mexc import mexc

exchanges = [
    "gateFutures",
    "bybitFutures",
    "bitgetFutures",
    "bingx",
    "biconomy",
    "mexc"
]

base = [
    "baseFuturesExchange",
    "baseSpotExchange"
]

_all__ =  exchanges + base