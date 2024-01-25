from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class VoteAssetContract(_message.Message):
    __slots__ = ("owner_address", "vote_address", "support", "count")
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VOTE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SUPPORT_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    vote_address: _containers.RepeatedScalarFieldContainer[bytes]
    support: bool
    count: int
    def __init__(self, owner_address: _Optional[bytes] = ..., vote_address: _Optional[_Iterable[bytes]] = ..., support: bool = ..., count: _Optional[int] = ...) -> None: ...
