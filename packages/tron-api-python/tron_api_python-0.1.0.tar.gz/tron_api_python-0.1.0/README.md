# Tron Api For Python

Tron grpc and http api

### Demo
```python
import json

import grpc

from tron_api import tron_utils
from tron_api.grpc.api.api_pb2 import EmptyMessage, Return
from tron_api.grpc.api.api_pb2_grpc import WalletStub
from tron_api.grpc.core.Tron_pb2 import Block, Transaction
from tron_api.grpc.core.contract.balance_contract_pb2 import TransferContract
from tron_api.http.http_api_impl import TronSolidityNodeHttpApi, TronFullNodeHttpApi


private_key = bytes.fromhex("72015f629b750c4ce520209fa866b056a29d7957a1e29645c28ce72fe44fede1")
owner_address = tron_utils.ADDR("TECwVujGXYNTXJ3sWiJJhjRZS3zgptvENe")
to_address = tron_utils.ADDR("TECwVujGXYNTXJ3sWiJJhjRZS3zgptvENe")


class GrpcDemo:
    def __init__(self):
        channel = grpc.insecure_channel("172.18.0.3:50051")
        self.wallet_stub = WalletStub(channel)

    def get_demo(self):
        block: Block = self.wallet_stub.GetNowBlock(EmptyMessage())
        print(block)

    def transfer_demo(self):
        # grpc demo
        tran: Transaction = self.wallet_stub.CreateTransaction(TransferContract(
            owner_address=owner_address,
            to_address=to_address,
            amount=10
        ))
        tran.signature.append(tron_utils.sign_message(private_key, tran.raw_data.SerializeToString()))
        grpc_res: Return = self.wallet_stub.BroadcastTransaction(tran)
        print(grpc_res)


class HttpDemo:
    def __init__(self):
        self.http_api = TronFullNodeHttpApi(gateway="http://172.18.0.3:8090")

    def get_demo(self):
        status, block = self.http_api.getnowblock()
        print(block)

    def transfer_demo(self):
        # http demo
        status, transaction = self.http_api.createtransaction(json_data={
            'owner_address': owner_address.hex(),
            'to_address': to_address.hex(),
            'amount': 2 * 1_000_000,
        })
        transaction = json.loads(transaction)
        transaction["signature"] = [
            tron_utils.sign_message(private_key, bytes.fromhex(transaction.get("raw_data_hex"))).hex()]
        status, res = self.http_api.broadcasttransaction(json_data=transaction)
        print(status, res)


if __name__ == '__main__':
    print(tron_utils.private_key_to_address(private_key=private_key))

    g, h = GrpcDemo(), HttpDemo()
    g.get_demo()
    h.get_demo()
    # g.transfer_demo()
    # h.transfer_demo()

```