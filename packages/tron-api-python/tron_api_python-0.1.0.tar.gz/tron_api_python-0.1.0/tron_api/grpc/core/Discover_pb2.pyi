from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Endpoint(_message.Message):
    __slots__ = ("address", "port", "nodeId", "addressIpv6")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    NODEID_FIELD_NUMBER: _ClassVar[int]
    ADDRESSIPV6_FIELD_NUMBER: _ClassVar[int]
    address: bytes
    port: int
    nodeId: bytes
    addressIpv6: bytes
    def __init__(self, address: _Optional[bytes] = ..., port: _Optional[int] = ..., nodeId: _Optional[bytes] = ..., addressIpv6: _Optional[bytes] = ...) -> None: ...

class PingMessage(_message.Message):
    __slots__ = ("to", "version", "timestamp")
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    to: Endpoint
    version: int
    timestamp: int
    def __init__(self, to: _Optional[_Union[Endpoint, _Mapping]] = ..., version: _Optional[int] = ..., timestamp: _Optional[int] = ..., **kwargs) -> None: ...

class PongMessage(_message.Message):
    __slots__ = ("echo", "timestamp")
    FROM_FIELD_NUMBER: _ClassVar[int]
    ECHO_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    echo: int
    timestamp: int
    def __init__(self, echo: _Optional[int] = ..., timestamp: _Optional[int] = ..., **kwargs) -> None: ...

class FindNeighbours(_message.Message):
    __slots__ = ("targetId", "timestamp")
    FROM_FIELD_NUMBER: _ClassVar[int]
    TARGETID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    targetId: bytes
    timestamp: int
    def __init__(self, targetId: _Optional[bytes] = ..., timestamp: _Optional[int] = ..., **kwargs) -> None: ...

class Neighbours(_message.Message):
    __slots__ = ("neighbours", "timestamp")
    FROM_FIELD_NUMBER: _ClassVar[int]
    NEIGHBOURS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    neighbours: _containers.RepeatedCompositeFieldContainer[Endpoint]
    timestamp: int
    def __init__(self, neighbours: _Optional[_Iterable[_Union[Endpoint, _Mapping]]] = ..., timestamp: _Optional[int] = ..., **kwargs) -> None: ...

class BackupMessage(_message.Message):
    __slots__ = ("flag", "priority")
    FLAG_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    flag: bool
    priority: int
    def __init__(self, flag: bool = ..., priority: _Optional[int] = ...) -> None: ...
