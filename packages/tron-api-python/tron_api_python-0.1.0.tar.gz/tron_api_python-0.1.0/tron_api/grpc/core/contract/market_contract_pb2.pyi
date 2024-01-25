from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MarketSellAssetContract(_message.Message):
    __slots__ = ("owner_address", "sell_token_id", "sell_token_quantity", "buy_token_id", "buy_token_quantity")
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SELL_TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    SELL_TOKEN_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    BUY_TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    BUY_TOKEN_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    sell_token_id: bytes
    sell_token_quantity: int
    buy_token_id: bytes
    buy_token_quantity: int
    def __init__(self, owner_address: _Optional[bytes] = ..., sell_token_id: _Optional[bytes] = ..., sell_token_quantity: _Optional[int] = ..., buy_token_id: _Optional[bytes] = ..., buy_token_quantity: _Optional[int] = ...) -> None: ...

class MarketCancelOrderContract(_message.Message):
    __slots__ = ("owner_address", "order_id")
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    order_id: bytes
    def __init__(self, owner_address: _Optional[bytes] = ..., order_id: _Optional[bytes] = ...) -> None: ...
