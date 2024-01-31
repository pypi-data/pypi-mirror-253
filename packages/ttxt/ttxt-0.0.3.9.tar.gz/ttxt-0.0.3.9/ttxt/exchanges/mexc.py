import hmac
import base64
import hashlib
import json
import time
import requests
from datetime import datetime as dt
from ttxt.base import baseSpotExchange
from ttxt.types import baseTypes

'''
kwards = {}
'''
class mexc(baseSpotExchange.BaseSpotExchange):
    def __init__(self, key, secret, **kwargs):
        super().__init__(key, secret, **kwargs)
        self.domain_url = "https://api.mexc.com"
        self.max_retries = 5
        self.symbolLotSize = {}
        self.recvWindow = 60000

    def _getSymbol(self, symbol):
        return symbol.replace("/", "")

    ## Auth 
    def get_expire(self):
        return int((time.time() + 1) * 1000)  # websockets use seconds
    
    def generate_timestamp(self):
        """
        Return a millisecond integer timestamp.
        """
        return int(time.time() * 10**3)
    
    def _get_sign(self, payload):
        # payload = ":"+ payload + "&secret_key=" + self.secret
        payload = payload + "&secret_key=" + self.secret
        signature = hashlib.md5(payload.encode()).hexdigest().upper()
        return signature
        
    def _parseParams(self, paramsMap):
        sortedKeys = sorted(paramsMap)
        paramsStr = "&".join(["%s=%s" % (x, paramsMap[x]) for x in sortedKeys])
        # return paramsStr+"&timestamp="+str(int(time.time() * 1000))
        return paramsStr
    
    def _check_resp_status(self, resp):
        if "code" in resp:
            if resp["code"] != 0:
                raise Exception(resp["message"])
            else:
                return resp  # success 
        if "message" in resp:
            raise Exception(resp["message"])
        raise Exception("Unknown error")
    
    def _authenticate(self,params):
        params = self._prepare_params(params)
        signature = hmac.new(
            self.secret.encode('utf-8'), 
            params.encode('utf-8'),
            hashlib.sha256
        ).hexdigest() 
        headers = {
            'X-MEXC-APIKEY': self.key
        }
        updatedParams = params + f"&signature={signature}"
        return headers, updatedParams
        
    def _send_request(self, method, path, params, payload={}):
        headers, updatedParams = self._authenticate(params)
        try:
            updatedurl = self.domain_url + path + "?"+ updatedParams
            response = requests.post(updatedurl, headers=headers)
            return response.json() #self._check_resp_status(response.json())
        except Exception as e:
            raise e
        
    def _prepare_params(self, params):
        payload = "&".join(
                [
                    str(k) + "=" + str(v)
                    for k, v in params.items()  #use for sort: sorted(params.items())
                    if v is not None
                ]
            )
        return payload

    ## parsers
    def _parseCreateorder(self, order):
        parsedOrder = {}
        parsedOrder["id"] = order.get('orderId', None)
        parsedOrder["symbol"] = order.get('symbol', None)
        parsedOrder["price"] = order.get("price", None)
        parsedOrder["amount"] = order.get("origQty", None)
        if "side" in order: 
            parsedOrder["side"] = order["side"].lower()
        else:
            parsedOrder["side"] = None
        parsedOrder["timestamp"] = order.get("transactTime", None)
        parsedOrder["status"] = "closed"
        parsedOrder["orderJson"] = json.dumps(order)
        return parsedOrder

    ## Exchange functions 
    # buy orders size are in quote and sell orders are in base
    def create_market_order(self, symbol, side, amount, params={}, price=None):
        apiUrl = "/api/v3/order"
        try:
            ticker = self._getSymbol(symbol)
            params = {
                'symbol': self._getSymbol(ticker),
                'side': side.upper(),
                'type': 'MARKET',
                'quantity': float(amount),
                'quoteOrderQty': float(amount),
                'recvWindow': self.recvWindow,
                'timestamp': int(time.time() * 1000)
            }
            params.update(params) 
            response = self._send_request(method='POST', path=apiUrl, params=params)
            return self._parseCreateorder(response)
        except Exception as e:
            raise e