from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BuyStorageBytesContract(_message.Message):
    __slots__ = ("owner_address", "bytes")
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BYTES_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    bytes: int
    def __init__(self, owner_address: _Optional[bytes] = ..., bytes: _Optional[int] = ...) -> None: ...

class BuyStorageContract(_message.Message):
    __slots__ = ("owner_address", "quant")
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    QUANT_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    quant: int
    def __init__(self, owner_address: _Optional[bytes] = ..., quant: _Optional[int] = ...) -> None: ...

class SellStorageContract(_message.Message):
    __slots__ = ("owner_address", "storage_bytes")
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    storage_bytes: int
    def __init__(self, owner_address: _Optional[bytes] = ..., storage_bytes: _Optional[int] = ...) -> None: ...

class UpdateBrokerageContract(_message.Message):
    __slots__ = ("owner_address", "brokerage")
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BROKERAGE_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    brokerage: int
    def __init__(self, owner_address: _Optional[bytes] = ..., brokerage: _Optional[int] = ...) -> None: ...
