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
kwards = {
    "category": "",
    "recv_window": ""
}
'''
class bingx(baseSpotExchange.BaseSpotExchange):
    def __init__(self, key, secret, **kwargs):
        super().__init__(key, secret, **kwargs)
        self.domain_url = "https://open-api.bingx.com"
        self.prefix = "/api/v4"
        self.category = kwargs["category"] if "category" in kwargs else "linear"
        self.recv_window = kwargs["recv_window"] if "recv_window" in kwargs else "5000"
        self.account_type = kwargs["account_type"] if "account_type" in kwargs else "UNIFIED"
        self.max_retries = 5
        self.symbolLotSize = {}

    def _getSymbol(self, symbol):
        return symbol.replace("/", "-")
    
    def _getUserSymbol(self, symbol):
        return symbol.replace("-", "/")
    
    ## Auth 
    def get_expire(self):
        return int((time.time() + 1) * 1000)  # websockets use seconds
    
    def generate_timestamp(self):
        """
        Return a millisecond integer timestamp.
        """
        return int(time.time() * 10**3)
    
    def _get_sign(self, payload):
        signature = hmac.new(self.secret.encode("utf-8"), payload.encode("utf-8"), digestmod=hashlib.sha256).hexdigest()
        print("sign=" + signature)
        return signature
    
    def _parseParams(self, paramsMap):
        sortedKeys = sorted(paramsMap)
        paramsStr = "&".join(["%s=%s" % (x, paramsMap[x]) for x in sortedKeys])
        return paramsStr+"&timestamp="+str(int(time.time() * 1000))

    def _send_request(self, method, path, params, payload):
        params = self._parseParams(params)
        url = "%s%s?%s&signature=%s" % (self.domain_url, path, params, self._get_sign(params))
        headers = {
            'X-BX-APIKEY': self.key,
        }
        try:
            response = requests.request(method, url, headers=headers, data=payload)
            return response.text
        except Exception as e:
            raise e
        
    def _prepare_params(self, params):
        payload = "&".join(
                [
                    str(k) + "=" + str(v)
                    for k, v in sorted(params.items())
                    if v is not None
                ]
            )
        return payload

    def _unsignedRequest(self, method=None, path=None, query=None, auth=False):
        path = self.domain_url + path
        if query is None:
            query = {}
        # Store original recv_window.
        recv_window = self.recv_window
        # Bug fix: change floating whole numbers to integers to prevent
        # auth signature errors.
        if query is not None:
            for i in query.keys():
                if isinstance(query[i], float) and query[i] == int(query[i]):
                    query[i] = int(query[i])
        # Send request and return headers with body. Retry if failed.
        retries_attempted = self.max_retries
        req_params = None
        while True:
            retries_attempted -= 1
            if retries_attempted < 0:
                raise Exception(
                    "Bad Request. Retries exceeded maximum."
                )
            req_params = self._prepare_params(query)
            # Authenticate if we are using a private endpoint.
            headers = {}
            if method == "GET":
                try:
                    if req_params:
                        client = requests.Session()
                        r = client.prepare_request(requests.Request(method, path, headers=headers))
                        #esp = client.send(r, timeout=60) 
                        resp = requests.get(path + f"?{req_params}", headers=headers)
                    else:
                        r = requests.get(path, headers=headers)
                    return resp.json()
                except Exception as e:
                    raise e
            if method == "POST":
                r = requests.post( path, data=req_params, headers=headers)
                return r.json()
            if method == "DELETE":
                r = requests.delete( path, data=req_params, headers=headers)
                return r.json()

    ## parsers
    '''
    {"retCode":0,"retMsg":"OK","result":
    {"list":[{"totalEquity":"233.33780771","accountIMRate":"0","totalMarginBalance":"233.07030533",
    "totalInitialMargin":"0","accountType":"UNIFIED","totalAvailableBalance":"233.07030533",
    "accountMMRate":"0","totalPerpUPL":"0","totalWalletBalance":"233.07030533",
    "accountLTV":"0","totalMaintenanceMargin":"0",
    "coin":[{"availableToBorrow":"","bonus":"0","accruedInterest":"0","availableToWithdraw":"0.00000978",
        "totalOrderIM":"0","equity":"0.00000978","totalPositionMM":"0","usdValue":"0.02315849",
        "unrealisedPnl":"0","collateralSwitch":true,"spotHedgingQty":"0","borrowAmount":"0.000000000000000000",
        "totalPositionIM":"0","walletBalance":"0.00000978","cumRealisedPnl":"-0.00000598","locked":"0",
        "marginCollateral":true,"coin":"ETH"},
        {"availableToBorrow":"","bonus":"0","accruedInterest":"",
        "availableToWithdraw":"0.004","totalOrderIM":"0","equity":"0.004","totalPositionMM":"0",
        "usdValue":"0.00481953","unrealisedPnl":"0","collateralSwitch":false,"spotHedgingQty":"0",
        "borrowAmount":"0.000000000000000000","totalPositionIM":"0","walletBalance":"0.004",
        "cumRealisedPnl":"0","locked":"0","marginCollateral":false,"coin":"XCAD"},
        {"availableToBorrow":"","bonus":"0","accruedInterest":"0","availableToWithdraw":"232.52736215","totalOrderIM":"0","equity":"232.52736215","totalPositionMM":"0","usdValue":"232.56261562","unrealisedPnl":"0","collateralSwitch":true,"spotHedgingQty":"0","borrowAmount":"0.000000000000000000","totalPositionIM":"0","walletBalance":"232.52736215","cumRealisedPnl":"-0.07024754","locked":"0","marginCollateral":true,"coin":"USDT"},{"availableToBorrow":"","bonus":"0","accruedInterest":"0","availableToWithdraw":"24.0062","totalOrderIM":"0","equity":"24.0062","totalPositionMM":"0","usdValue":"0.74721405","unrealisedPnl":"0","collateralSwitch":true,"spotHedgingQty":"0","borrowAmount":"0.000000000000000000","totalPositionIM":"0","walletBalance":"24.0062","cumRealisedPnl":"-1.7438","locked":"0","marginCollateral":true,"coin":"GALA"}]}]},"retExtInfo":{},"time":1702038150602}
    '''
    # balData = {"free": {"USDT": 1010, "BTC": ""}, "total": {"USDT": 1010, "BTC": 0}, "unrealisedPnl": {"USDT": 1010, "BTC": 0}}
    def _parseBalance(self, balData):
        parsedBal = {"free": {}, "total": {}, "unrealisedPnl": {}}
        balDataResult = balData.get("result", None)
        balDatList = balDataResult.get("list", [])
        if len(balDatList) == 0:
            return parsedBal
        balDatList = balDatList[0].get("coin", [])
        if len(balDatList) == 0:
            return parsedBal
        for balDataEle in balDatList:
            parsedBal["free"][balDataEle["coin"]] = balDataEle.get("walletBalance", None)
            parsedBal["total"][balDataEle["coin"]] = balDataEle.get("equity", None)
            parsedBal["unrealisedPnl"][balDataEle["coin"]] = balDataEle.get("unrealisedPnl", None)
        return parsedBal
    

    '''
    {"code":0,"msg":"","debugMsg":"","data":{"symbol":"BTC-USDT","orderId":1735300085442314240,
    "transactTime":1702562755342,"price":"41033.08","origQty":"0.001","executedQty":"0",
    "cummulativeQuoteQty":"0","status":"PENDING","type":"LIMIT","side":"BUY"}}
    '''
    def _parseOrder(self, order):
        parsedOrder = {"id": None, "symbol": None, "price": None, "amount": None, 
                       "side": None, "timestamp": None, "status": None, "orderJson": None}
        print(order)
        if "data" in order and order["data"] != {}:
            order = order["data"]
            parsedOrder["id"] = order["orderId"]
            parsedOrder["symbol"] = self._getUserSymbol(order["symbol"])
            parsedOrder["price"] = float(order["price"])
            parsedOrder["amount"] = float(order["origQty"])
            parsedOrder["side"] = order["side"].lower()
            parsedOrder["timestamp"] = int(order["transactTime"])
            parsedOrder["status"] = order["status"]
            parsedOrder["orderJson"] = json.dumps(order)
        return parsedOrder
    
    def _parseCreateorder(self, order):
        parsedOrder = {}
        parsedOrder["id"] = order["orderId"]
        parsedOrder["symbol"] = None
        parsedOrder["price"] = None
        parsedOrder["amount"] = None
        parsedOrder["side"] = None
        parsedOrder["timestamp"] = None
        parsedOrder["status"] = None
        parsedOrder["orderJson"] = json.dumps(order)
        return parsedOrder

    def _parseOpenOrders(self, orders):
        parsedOrderList = []
        orderjson = json.loads(orders)
        if "data" in orderjson and "orders" in orderjson["data"]:
            for order in orderjson["data"]["orders"]:
                parsedOrderList.append(self._parseOrder(order))
        return parsedOrderList

    '''
    {'retCode': 0, 'retMsg': 'OK', 'result': {'nextPageCursor': 'f3708d4e-24d6-4528-9037-764d03610479%3A1702055115208%2Cf3708d4e-24d6-4528-9037-764d03610479%3A1702055115208', 'category': 'linear', 'list': [{'symbol': 'BTCUSDT', 'orderType': 'Limit', 'orderLinkId': '', 'slLimitPrice': '0', 'orderId': 'f3708d4e-24d6-4528-9037-764d03610479', 'cancelType': 'UNKNOWN', 'avgPrice': '43832.1', 'stopOrderType': '', 'lastPriceOnCreated': '43832', 'orderStatus': 'Filled', 'takeProfit': '', 'cumExecValue': '43.8321', 'tpslMode': 'UNKNOWN', 'smpType': 'None', 'triggerDirection': 0, 'blockTradeId': '', 'isLeverage': '', 'rejectReason': 'EC_NoError', 'price': '43920', 'orderIv': '', 'createdTime': '1702055115208', 'tpTriggerBy': '', 'positionIdx': 0, 'timeInForce': 'GTC', 'leavesValue': '0', 'updatedTime': '1702055115209', 'side': 'Buy', 'smpGroup': 0, 'triggerPrice': '', 'tpLimitPrice': '0', 'cumExecFee': '0.02410766', 'leavesQty': '0', 'slTriggerBy': '', 'closeOnTrigger': False, 'placeType': '', 'cumExecQty': '0.001', 'reduceOnly': False, 'qty': '0.001', 'stopLoss': '', 'smpOrderId': '', 'triggerBy': ''}]}, 'retExtInfo': {}, 'time': 1702055320777}
    '''
    def _parseFetchedOrder(self, order):
        pass

    ## Exchange functions 

    # https://www.gate.io/docs/developers/apiv4/en/#create-a-futures-order
    def create_order(self, symbol, type, side, amount, price=None, params={}):
        try:
            ticker = self._getSymbol(symbol)
            params = {
                "symbol": ticker,
                "side": side.upper(),
                "type": type.upper(),
                "quantity": float(amount),
                "timestamp": self.generate_timestamp()
            }
            params.update(params) 
            print(params)
            if type == "limit":
               params["price"] = float(price)
            apiUrl = "/openApi/spot/v1/trade/order"
            response = self._send_request(method='POST', path=apiUrl, params=params, payload={})
            return self._parseOrder(response)
        except Exception as e:
            raise e
    
    def fetch_order(self, id, symbol=None):
        apiUrl = "/openApi/spot/v1/trade/query"
        queryParams = {"orderId": id, "symbol": symbol}  # maybe have a set symbol function ?
        try:
            resp = resp = self._send_request(method='GET', path=apiUrl, params=queryParams, payload=None)
            return resp #self._parseOrder(resp)
        except Exception as e:
            raise e

    def fetch_open_orders(self, symbol=None,  kwargs=None):
        apiUrl = "/openApi/spot/v1/trade/openOrders"
        queryParams = {"timestamp": self.generate_timestamp()}
        try:
            resp = self._send_request(method='GET', path=apiUrl, params=queryParams, payload=None)
            return self._parseOpenOrders(resp)
        except Exception as e:
            raise e
        
    def cancel_order(self, id, params={}):
        apiUrl = "/openApi/spot/v1/trade/cancel"
        queryParams = {"orderId": id, "symbol": self._getSymbol(params["symbol"])}
        try:
            resp = self._send_request(method='GET', path=apiUrl, params=queryParams, payload=None)
            return self._parseOrder(resp)
        except Exception as e:
            raise e

    def fetch_ticker(self, symbol: str, params={}) -> baseTypes.Ticker:
        apiUrl = "/openApi/spot/v1/common/symbols"
        queryParams = {"symbol": self._getSymbol(symbol)}
        try:
            resp = self._unsignedRequest(method='GET', path=apiUrl, query=queryParams)
            return resp # parse this response into Ticker
        except Exception as e:
            raise e
    
    # params = {"startTime": 1702512246000, "endTime": 1702512248000, "limit": 100}
    def fetch_ohlcv(self, symbol, interval, params={}):
        apiUrl = "/openApi/spot/v2/market/kline"
        queryParams = {"symbol": self._getSymbol(symbol), "interval": interval}
        try:
            resp = self._unsignedRequest(method='GET', path=apiUrl, query=queryParams)
            return resp # parse this response into Ticker
        except Exception as e:
            raise e
    
    def fetch_balance(self, params={}) -> baseTypes.Balances:
        apiUrl = '/openApi/spot/v1/account/balance'
        queryParams = {}
        try:
            resp = self._send_request(method='GET', path=apiUrl, params=queryParams, payload=None)
            return resp #self._parseBalance(resp)
        except Exception as e:
            raise e