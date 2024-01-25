from tron_api.grpc.core.contract import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FreezeBalanceContract(_message.Message):
    __slots__ = ("owner_address", "frozen_balance", "frozen_duration", "resource", "receiver_address")
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    FROZEN_BALANCE_FIELD_NUMBER: _ClassVar[int]
    FROZEN_DURATION_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    frozen_balance: int
    frozen_duration: int
    resource: _common_pb2.ResourceCode
    receiver_address: bytes
    def __init__(self, owner_address: _Optional[bytes] = ..., frozen_balance: _Optional[int] = ..., frozen_duration: _Optional[int] = ..., resource: _Optional[_Union[_common_pb2.ResourceCode, str]] = ..., receiver_address: _Optional[bytes] = ...) -> None: ...

class UnfreezeBalanceContract(_message.Message):
    __slots__ = ("owner_address", "resource", "receiver_address")
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    resource: _common_pb2.ResourceCode
    receiver_address: bytes
    def __init__(self, owner_address: _Optional[bytes] = ..., resource: _Optional[_Union[_common_pb2.ResourceCode, str]] = ..., receiver_address: _Optional[bytes] = ...) -> None: ...

class WithdrawBalanceContract(_message.Message):
    __slots__ = ("owner_address",)
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    def __init__(self, owner_address: _Optional[bytes] = ...) -> None: ...

class TransferContract(_message.Message):
    __slots__ = ("owner_address", "to_address", "amount")
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TO_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    to_address: bytes
    amount: int
    def __init__(self, owner_address: _Optional[bytes] = ..., to_address: _Optional[bytes] = ..., amount: _Optional[int] = ...) -> None: ...

class TransactionBalanceTrace(_message.Message):
    __slots__ = ("transaction_identifier", "operation", "type", "status")
    class Operation(_message.Message):
        __slots__ = ("operation_identifier", "address", "amount")
        OPERATION_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        ADDRESS_FIELD_NUMBER: _ClassVar[int]
        AMOUNT_FIELD_NUMBER: _ClassVar[int]
        operation_identifier: int
        address: bytes
        amount: int
        def __init__(self, operation_identifier: _Optional[int] = ..., address: _Optional[bytes] = ..., amount: _Optional[int] = ...) -> None: ...
    TRANSACTION_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    transaction_identifier: bytes
    operation: _containers.RepeatedCompositeFieldContainer[TransactionBalanceTrace.Operation]
    type: str
    status: str
    def __init__(self, transaction_identifier: _Optional[bytes] = ..., operation: _Optional[_Iterable[_Union[TransactionBalanceTrace.Operation, _Mapping]]] = ..., type: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class BlockBalanceTrace(_message.Message):
    __slots__ = ("block_identifier", "timestamp", "transaction_balance_trace")
    class BlockIdentifier(_message.Message):
        __slots__ = ("hash", "number")
        HASH_FIELD_NUMBER: _ClassVar[int]
        NUMBER_FIELD_NUMBER: _ClassVar[int]
        hash: bytes
        number: int
        def __init__(self, hash: _Optional[bytes] = ..., number: _Optional[int] = ...) -> None: ...
    BLOCK_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_BALANCE_TRACE_FIELD_NUMBER: _ClassVar[int]
    block_identifier: BlockBalanceTrace.BlockIdentifier
    timestamp: int
    transaction_balance_trace: _containers.RepeatedCompositeFieldContainer[TransactionBalanceTrace]
    def __init__(self, block_identifier: _Optional[_Union[BlockBalanceTrace.BlockIdentifier, _Mapping]] = ..., timestamp: _Optional[int] = ..., transaction_balance_trace: _Optional[_Iterable[_Union[TransactionBalanceTrace, _Mapping]]] = ...) -> None: ...

class AccountTrace(_message.Message):
    __slots__ = ("balance", "placeholder")
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
    balance: int
    placeholder: int
    def __init__(self, balance: _Optional[int] = ..., placeholder: _Optional[int] = ...) -> None: ...

class AccountIdentifier(_message.Message):
    __slots__ = ("address",)
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: bytes
    def __init__(self, address: _Optional[bytes] = ...) -> None: ...

class AccountBalanceRequest(_message.Message):
    __slots__ = ("account_identifier", "block_identifier")
    ACCOUNT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    BLOCK_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    account_identifier: AccountIdentifier
    block_identifier: BlockBalanceTrace.BlockIdentifier
    def __init__(self, account_identifier: _Optional[_Union[AccountIdentifier, _Mapping]] = ..., block_identifier: _Optional[_Union[BlockBalanceTrace.BlockIdentifier, _Mapping]] = ...) -> None: ...

class AccountBalanceResponse(_message.Message):
    __slots__ = ("balance", "block_identifier")
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    BLOCK_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    balance: int
    block_identifier: BlockBalanceTrace.BlockIdentifier
    def __init__(self, balance: _Optional[int] = ..., block_identifier: _Optional[_Union[BlockBalanceTrace.BlockIdentifier, _Mapping]] = ...) -> None: ...

class FreezeBalanceV2Contract(_message.Message):
    __slots__ = ("owner_address", "frozen_balance", "resource")
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    FROZEN_BALANCE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    frozen_balance: int
    resource: _common_pb2.ResourceCode
    def __init__(self, owner_address: _Optional[bytes] = ..., frozen_balance: _Optional[int] = ..., resource: _Optional[_Union[_common_pb2.ResourceCode, str]] = ...) -> None: ...

class UnfreezeBalanceV2Contract(_message.Message):
    __slots__ = ("owner_address", "unfreeze_balance", "resource")
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    UNFREEZE_BALANCE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    unfreeze_balance: int
    resource: _common_pb2.ResourceCode
    def __init__(self, owner_address: _Optional[bytes] = ..., unfreeze_balance: _Optional[int] = ..., resource: _Optional[_Union[_common_pb2.ResourceCode, str]] = ...) -> None: ...

class WithdrawExpireUnfreezeContract(_message.Message):
    __slots__ = ("owner_address",)
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    def __init__(self, owner_address: _Optional[bytes] = ...) -> None: ...

class DelegateResourceContract(_message.Message):
    __slots__ = ("owner_address", "resource", "balance", "receiver_address", "lock", "lock_period")
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    LOCK_FIELD_NUMBER: _ClassVar[int]
    LOCK_PERIOD_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    resource: _common_pb2.ResourceCode
    balance: int
    receiver_address: bytes
    lock: bool
    lock_period: int
    def __init__(self, owner_address: _Optional[bytes] = ..., resource: _Optional[_Union[_common_pb2.ResourceCode, str]] = ..., balance: _Optional[int] = ..., receiver_address: _Optional[bytes] = ..., lock: bool = ..., lock_period: _Optional[int] = ...) -> None: ...

class UnDelegateResourceContract(_message.Message):
    __slots__ = ("owner_address", "resource", "balance", "receiver_address")
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    resource: _common_pb2.ResourceCode
    balance: int
    receiver_address: bytes
    def __init__(self, owner_address: _Optional[bytes] = ..., resource: _Optional[_Union[_common_pb2.ResourceCode, str]] = ..., balance: _Optional[int] = ..., receiver_address: _Optional[bytes] = ...) -> None: ...

class CancelAllUnfreezeV2Contract(_message.Message):
    __slots__ = ("owner_address",)
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    def __init__(self, owner_address: _Optional[bytes] = ...) -> None: ...
