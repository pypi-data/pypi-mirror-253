from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ExchangeCreateContract(_message.Message):
    __slots__ = ("owner_address", "first_token_id", "first_token_balance", "second_token_id", "second_token_balance")
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    FIRST_TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_TOKEN_BALANCE_FIELD_NUMBER: _ClassVar[int]
    SECOND_TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    SECOND_TOKEN_BALANCE_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    first_token_id: bytes
    first_token_balance: int
    second_token_id: bytes
    second_token_balance: int
    def __init__(self, owner_address: _Optional[bytes] = ..., first_token_id: _Optional[bytes] = ..., first_token_balance: _Optional[int] = ..., second_token_id: _Optional[bytes] = ..., second_token_balance: _Optional[int] = ...) -> None: ...

class ExchangeInjectContract(_message.Message):
    __slots__ = ("owner_address", "exchange_id", "token_id", "quant")
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    QUANT_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    exchange_id: int
    token_id: bytes
    quant: int
    def __init__(self, owner_address: _Optional[bytes] = ..., exchange_id: _Optional[int] = ..., token_id: _Optional[bytes] = ..., quant: _Optional[int] = ...) -> None: ...

class ExchangeWithdrawContract(_message.Message):
    __slots__ = ("owner_address", "exchange_id", "token_id", "quant")
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    QUANT_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    exchange_id: int
    token_id: bytes
    quant: int
    def __init__(self, owner_address: _Optional[bytes] = ..., exchange_id: _Optional[int] = ..., token_id: _Optional[bytes] = ..., quant: _Optional[int] = ...) -> None: ...

class ExchangeTransactionContract(_message.Message):
    __slots__ = ("owner_address", "exchange_id", "token_id", "quant", "expected")
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    QUANT_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    exchange_id: int
    token_id: bytes
    quant: int
    expected: int
    def __init__(self, owner_address: _Optional[bytes] = ..., exchange_id: _Optional[int] = ..., token_id: _Optional[bytes] = ..., quant: _Optional[int] = ..., expected: _Optional[int] = ...) -> None: ...
