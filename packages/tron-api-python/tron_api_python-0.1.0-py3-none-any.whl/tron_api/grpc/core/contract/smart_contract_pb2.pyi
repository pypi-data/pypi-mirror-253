from tron_api.grpc.core import Tron_pb2 as _Tron_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SmartContract(_message.Message):
    __slots__ = ("origin_address", "contract_address", "abi", "bytecode", "call_value", "consume_user_resource_percent", "name", "origin_energy_limit", "code_hash", "trx_hash", "version")
    class ABI(_message.Message):
        __slots__ = ("entrys",)
        class Entry(_message.Message):
            __slots__ = ("anonymous", "constant", "name", "inputs", "outputs", "type", "payable", "stateMutability")
            class EntryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                UnknownEntryType: _ClassVar[SmartContract.ABI.Entry.EntryType]
                Constructor: _ClassVar[SmartContract.ABI.Entry.EntryType]
                Function: _ClassVar[SmartContract.ABI.Entry.EntryType]
                Event: _ClassVar[SmartContract.ABI.Entry.EntryType]
                Fallback: _ClassVar[SmartContract.ABI.Entry.EntryType]
                Receive: _ClassVar[SmartContract.ABI.Entry.EntryType]
                Error: _ClassVar[SmartContract.ABI.Entry.EntryType]
            UnknownEntryType: SmartContract.ABI.Entry.EntryType
            Constructor: SmartContract.ABI.Entry.EntryType
            Function: SmartContract.ABI.Entry.EntryType
            Event: SmartContract.ABI.Entry.EntryType
            Fallback: SmartContract.ABI.Entry.EntryType
            Receive: SmartContract.ABI.Entry.EntryType
            Error: SmartContract.ABI.Entry.EntryType
            class StateMutabilityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                UnknownMutabilityType: _ClassVar[SmartContract.ABI.Entry.StateMutabilityType]
                Pure: _ClassVar[SmartContract.ABI.Entry.StateMutabilityType]
                View: _ClassVar[SmartContract.ABI.Entry.StateMutabilityType]
                Nonpayable: _ClassVar[SmartContract.ABI.Entry.StateMutabilityType]
                Payable: _ClassVar[SmartContract.ABI.Entry.StateMutabilityType]
            UnknownMutabilityType: SmartContract.ABI.Entry.StateMutabilityType
            Pure: SmartContract.ABI.Entry.StateMutabilityType
            View: SmartContract.ABI.Entry.StateMutabilityType
            Nonpayable: SmartContract.ABI.Entry.StateMutabilityType
            Payable: SmartContract.ABI.Entry.StateMutabilityType
            class Param(_message.Message):
                __slots__ = ("indexed", "name", "type")
                INDEXED_FIELD_NUMBER: _ClassVar[int]
                NAME_FIELD_NUMBER: _ClassVar[int]
                TYPE_FIELD_NUMBER: _ClassVar[int]
                indexed: bool
                name: str
                type: str
                def __init__(self, indexed: bool = ..., name: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...
            ANONYMOUS_FIELD_NUMBER: _ClassVar[int]
            CONSTANT_FIELD_NUMBER: _ClassVar[int]
            NAME_FIELD_NUMBER: _ClassVar[int]
            INPUTS_FIELD_NUMBER: _ClassVar[int]
            OUTPUTS_FIELD_NUMBER: _ClassVar[int]
            TYPE_FIELD_NUMBER: _ClassVar[int]
            PAYABLE_FIELD_NUMBER: _ClassVar[int]
            STATEMUTABILITY_FIELD_NUMBER: _ClassVar[int]
            anonymous: bool
            constant: bool
            name: str
            inputs: _containers.RepeatedCompositeFieldContainer[SmartContract.ABI.Entry.Param]
            outputs: _containers.RepeatedCompositeFieldContainer[SmartContract.ABI.Entry.Param]
            type: SmartContract.ABI.Entry.EntryType
            payable: bool
            stateMutability: SmartContract.ABI.Entry.StateMutabilityType
            def __init__(self, anonymous: bool = ..., constant: bool = ..., name: _Optional[str] = ..., inputs: _Optional[_Iterable[_Union[SmartContract.ABI.Entry.Param, _Mapping]]] = ..., outputs: _Optional[_Iterable[_Union[SmartContract.ABI.Entry.Param, _Mapping]]] = ..., type: _Optional[_Union[SmartContract.ABI.Entry.EntryType, str]] = ..., payable: bool = ..., stateMutability: _Optional[_Union[SmartContract.ABI.Entry.StateMutabilityType, str]] = ...) -> None: ...
        ENTRYS_FIELD_NUMBER: _ClassVar[int]
        entrys: _containers.RepeatedCompositeFieldContainer[SmartContract.ABI.Entry]
        def __init__(self, entrys: _Optional[_Iterable[_Union[SmartContract.ABI.Entry, _Mapping]]] = ...) -> None: ...
    ORIGIN_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ABI_FIELD_NUMBER: _ClassVar[int]
    BYTECODE_FIELD_NUMBER: _ClassVar[int]
    CALL_VALUE_FIELD_NUMBER: _ClassVar[int]
    CONSUME_USER_RESOURCE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_ENERGY_LIMIT_FIELD_NUMBER: _ClassVar[int]
    CODE_HASH_FIELD_NUMBER: _ClassVar[int]
    TRX_HASH_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    origin_address: bytes
    contract_address: bytes
    abi: SmartContract.ABI
    bytecode: bytes
    call_value: int
    consume_user_resource_percent: int
    name: str
    origin_energy_limit: int
    code_hash: bytes
    trx_hash: bytes
    version: int
    def __init__(self, origin_address: _Optional[bytes] = ..., contract_address: _Optional[bytes] = ..., abi: _Optional[_Union[SmartContract.ABI, _Mapping]] = ..., bytecode: _Optional[bytes] = ..., call_value: _Optional[int] = ..., consume_user_resource_percent: _Optional[int] = ..., name: _Optional[str] = ..., origin_energy_limit: _Optional[int] = ..., code_hash: _Optional[bytes] = ..., trx_hash: _Optional[bytes] = ..., version: _Optional[int] = ...) -> None: ...

class ContractState(_message.Message):
    __slots__ = ("energy_usage", "energy_factor", "update_cycle")
    ENERGY_USAGE_FIELD_NUMBER: _ClassVar[int]
    ENERGY_FACTOR_FIELD_NUMBER: _ClassVar[int]
    UPDATE_CYCLE_FIELD_NUMBER: _ClassVar[int]
    energy_usage: int
    energy_factor: int
    update_cycle: int
    def __init__(self, energy_usage: _Optional[int] = ..., energy_factor: _Optional[int] = ..., update_cycle: _Optional[int] = ...) -> None: ...

class CreateSmartContract(_message.Message):
    __slots__ = ("owner_address", "new_contract", "call_token_value", "token_id")
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NEW_CONTRACT_FIELD_NUMBER: _ClassVar[int]
    CALL_TOKEN_VALUE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    new_contract: SmartContract
    call_token_value: int
    token_id: int
    def __init__(self, owner_address: _Optional[bytes] = ..., new_contract: _Optional[_Union[SmartContract, _Mapping]] = ..., call_token_value: _Optional[int] = ..., token_id: _Optional[int] = ...) -> None: ...

class TriggerSmartContract(_message.Message):
    __slots__ = ("owner_address", "contract_address", "call_value", "data", "call_token_value", "token_id")
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CALL_VALUE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    CALL_TOKEN_VALUE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    contract_address: bytes
    call_value: int
    data: bytes
    call_token_value: int
    token_id: int
    def __init__(self, owner_address: _Optional[bytes] = ..., contract_address: _Optional[bytes] = ..., call_value: _Optional[int] = ..., data: _Optional[bytes] = ..., call_token_value: _Optional[int] = ..., token_id: _Optional[int] = ...) -> None: ...

class ClearABIContract(_message.Message):
    __slots__ = ("owner_address", "contract_address")
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    contract_address: bytes
    def __init__(self, owner_address: _Optional[bytes] = ..., contract_address: _Optional[bytes] = ...) -> None: ...

class UpdateSettingContract(_message.Message):
    __slots__ = ("owner_address", "contract_address", "consume_user_resource_percent")
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CONSUME_USER_RESOURCE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    contract_address: bytes
    consume_user_resource_percent: int
    def __init__(self, owner_address: _Optional[bytes] = ..., contract_address: _Optional[bytes] = ..., consume_user_resource_percent: _Optional[int] = ...) -> None: ...

class UpdateEnergyLimitContract(_message.Message):
    __slots__ = ("owner_address", "contract_address", "origin_energy_limit")
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_ENERGY_LIMIT_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    contract_address: bytes
    origin_energy_limit: int
    def __init__(self, owner_address: _Optional[bytes] = ..., contract_address: _Optional[bytes] = ..., origin_energy_limit: _Optional[int] = ...) -> None: ...

class SmartContractDataWrapper(_message.Message):
    __slots__ = ("smart_contract", "runtimecode", "contract_state")
    SMART_CONTRACT_FIELD_NUMBER: _ClassVar[int]
    RUNTIMECODE_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_STATE_FIELD_NUMBER: _ClassVar[int]
    smart_contract: SmartContract
    runtimecode: bytes
    contract_state: ContractState
    def __init__(self, smart_contract: _Optional[_Union[SmartContract, _Mapping]] = ..., runtimecode: _Optional[bytes] = ..., contract_state: _Optional[_Union[ContractState, _Mapping]] = ...) -> None: ...
