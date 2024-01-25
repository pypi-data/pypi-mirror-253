from tron_api.grpc.core import Tron_pb2 as _Tron_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccountCreateContract(_message.Message):
    __slots__ = ("owner_address", "account_address", "type")
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    account_address: bytes
    type: _Tron_pb2.AccountType
    def __init__(self, owner_address: _Optional[bytes] = ..., account_address: _Optional[bytes] = ..., type: _Optional[_Union[_Tron_pb2.AccountType, str]] = ...) -> None: ...

class AccountUpdateContract(_message.Message):
    __slots__ = ("account_name", "owner_address")
    ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    account_name: bytes
    owner_address: bytes
    def __init__(self, account_name: _Optional[bytes] = ..., owner_address: _Optional[bytes] = ...) -> None: ...

class SetAccountIdContract(_message.Message):
    __slots__ = ("account_id", "owner_address")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    account_id: bytes
    owner_address: bytes
    def __init__(self, account_id: _Optional[bytes] = ..., owner_address: _Optional[bytes] = ...) -> None: ...

class AccountPermissionUpdateContract(_message.Message):
    __slots__ = ("owner_address", "owner", "witness", "actives")
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    WITNESS_FIELD_NUMBER: _ClassVar[int]
    ACTIVES_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    owner: _Tron_pb2.Permission
    witness: _Tron_pb2.Permission
    actives: _containers.RepeatedCompositeFieldContainer[_Tron_pb2.Permission]
    def __init__(self, owner_address: _Optional[bytes] = ..., owner: _Optional[_Union[_Tron_pb2.Permission, _Mapping]] = ..., witness: _Optional[_Union[_Tron_pb2.Permission, _Mapping]] = ..., actives: _Optional[_Iterable[_Union[_Tron_pb2.Permission, _Mapping]]] = ...) -> None: ...
