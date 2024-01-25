from tron_api.http.http_api_abc import TronFullNodeHttpApiABC, TronSolidityNodeHttpApiABC


class TronFullNodeHttpApi(TronFullNodeHttpApiABC):
    pass


class TronSolidityNodeHttpApi(TronSolidityNodeHttpApiABC):
    pass


if __name__ == '__main__':
    api = TronSolidityNodeHttpApi(gateway="http://172.18.0.3:8091")
    # POST
    code, data = api.getTransactionInfoById(
        json_data={"value": "7deb4a226ad87642da29422ec5a390a0e38f834d8f0c0db3ca0582bdbd7e2b15"})
    print(code, data)
    # GET
    code, data = api.getTransactionInfoById(
        query_string="value=7deb4a226ad87642da29422ec5a390a0e38f834d8f0c0db3ca0582bdbd7e2b15")
    print(code, data)
