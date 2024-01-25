from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WitnessCreateContract(_message.Message):
    __slots__ = ("owner_address", "url")
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    url: bytes
    def __init__(self, owner_address: _Optional[bytes] = ..., url: _Optional[bytes] = ...) -> None: ...

class WitnessUpdateContract(_message.Message):
    __slots__ = ("owner_address", "update_url")
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_URL_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    update_url: bytes
    def __init__(self, owner_address: _Optional[bytes] = ..., update_url: _Optional[bytes] = ...) -> None: ...

class VoteWitnessContract(_message.Message):
    __slots__ = ("owner_address", "votes", "support")
    class Vote(_message.Message):
        __slots__ = ("vote_address", "vote_count")
        VOTE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        VOTE_COUNT_FIELD_NUMBER: _ClassVar[int]
        vote_address: bytes
        vote_count: int
        def __init__(self, vote_address: _Optional[bytes] = ..., vote_count: _Optional[int] = ...) -> None: ...
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VOTES_FIELD_NUMBER: _ClassVar[int]
    SUPPORT_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    votes: _containers.RepeatedCompositeFieldContainer[VoteWitnessContract.Vote]
    support: bool
    def __init__(self, owner_address: _Optional[bytes] = ..., votes: _Optional[_Iterable[_Union[VoteWitnessContract.Vote, _Mapping]]] = ..., support: bool = ...) -> None: ...
