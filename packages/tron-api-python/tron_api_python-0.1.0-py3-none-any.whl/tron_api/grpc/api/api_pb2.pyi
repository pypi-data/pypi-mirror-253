from tron_api.grpc.core import Tron_pb2 as _Tron_pb2
from tron_api.grpc.core.contract import asset_issue_contract_pb2 as _asset_issue_contract_pb2
from tron_api.grpc.core.contract import account_contract_pb2 as _account_contract_pb2
from tron_api.grpc.core.contract import witness_contract_pb2 as _witness_contract_pb2
from tron_api.grpc.core.contract import balance_contract_pb2 as _balance_contract_pb2
from tron_api.grpc.core.contract import proposal_contract_pb2 as _proposal_contract_pb2
from tron_api.grpc.core.contract import storage_contract_pb2 as _storage_contract_pb2
from tron_api.grpc.core.contract import exchange_contract_pb2 as _exchange_contract_pb2
from tron_api.grpc.core.contract import market_contract_pb2 as _market_contract_pb2
from tron_api.grpc.core.contract import smart_contract_pb2 as _smart_contract_pb2
from tron_api.grpc.core.contract import shield_contract_pb2 as _shield_contract_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Return(_message.Message):
    __slots__ = ("result", "code", "message")
    class response_code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[Return.response_code]
        SIGERROR: _ClassVar[Return.response_code]
        CONTRACT_VALIDATE_ERROR: _ClassVar[Return.response_code]
        CONTRACT_EXE_ERROR: _ClassVar[Return.response_code]
        BANDWITH_ERROR: _ClassVar[Return.response_code]
        DUP_TRANSACTION_ERROR: _ClassVar[Return.response_code]
        TAPOS_ERROR: _ClassVar[Return.response_code]
        TOO_BIG_TRANSACTION_ERROR: _ClassVar[Return.response_code]
        TRANSACTION_EXPIRATION_ERROR: _ClassVar[Return.response_code]
        SERVER_BUSY: _ClassVar[Return.response_code]
        NO_CONNECTION: _ClassVar[Return.response_code]
        NOT_ENOUGH_EFFECTIVE_CONNECTION: _ClassVar[Return.response_code]
        OTHER_ERROR: _ClassVar[Return.response_code]
    SUCCESS: Return.response_code
    SIGERROR: Return.response_code
    CONTRACT_VALIDATE_ERROR: Return.response_code
    CONTRACT_EXE_ERROR: Return.response_code
    BANDWITH_ERROR: Return.response_code
    DUP_TRANSACTION_ERROR: Return.response_code
    TAPOS_ERROR: Return.response_code
    TOO_BIG_TRANSACTION_ERROR: Return.response_code
    TRANSACTION_EXPIRATION_ERROR: Return.response_code
    SERVER_BUSY: Return.response_code
    NO_CONNECTION: Return.response_code
    NOT_ENOUGH_EFFECTIVE_CONNECTION: Return.response_code
    OTHER_ERROR: Return.response_code
    RESULT_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    result: bool
    code: Return.response_code
    message: bytes
    def __init__(self, result: bool = ..., code: _Optional[_Union[Return.response_code, str]] = ..., message: _Optional[bytes] = ...) -> None: ...

class BlockReference(_message.Message):
    __slots__ = ("block_num", "block_hash")
    BLOCK_NUM_FIELD_NUMBER: _ClassVar[int]
    BLOCK_HASH_FIELD_NUMBER: _ClassVar[int]
    block_num: int
    block_hash: bytes
    def __init__(self, block_num: _Optional[int] = ..., block_hash: _Optional[bytes] = ...) -> None: ...

class WitnessList(_message.Message):
    __slots__ = ("witnesses",)
    WITNESSES_FIELD_NUMBER: _ClassVar[int]
    witnesses: _containers.RepeatedCompositeFieldContainer[_Tron_pb2.Witness]
    def __init__(self, witnesses: _Optional[_Iterable[_Union[_Tron_pb2.Witness, _Mapping]]] = ...) -> None: ...

class ProposalList(_message.Message):
    __slots__ = ("proposals",)
    PROPOSALS_FIELD_NUMBER: _ClassVar[int]
    proposals: _containers.RepeatedCompositeFieldContainer[_Tron_pb2.Proposal]
    def __init__(self, proposals: _Optional[_Iterable[_Union[_Tron_pb2.Proposal, _Mapping]]] = ...) -> None: ...

class ExchangeList(_message.Message):
    __slots__ = ("exchanges",)
    EXCHANGES_FIELD_NUMBER: _ClassVar[int]
    exchanges: _containers.RepeatedCompositeFieldContainer[_Tron_pb2.Exchange]
    def __init__(self, exchanges: _Optional[_Iterable[_Union[_Tron_pb2.Exchange, _Mapping]]] = ...) -> None: ...

class AssetIssueList(_message.Message):
    __slots__ = ("assetIssue",)
    ASSETISSUE_FIELD_NUMBER: _ClassVar[int]
    assetIssue: _containers.RepeatedCompositeFieldContainer[_asset_issue_contract_pb2.AssetIssueContract]
    def __init__(self, assetIssue: _Optional[_Iterable[_Union[_asset_issue_contract_pb2.AssetIssueContract, _Mapping]]] = ...) -> None: ...

class BlockList(_message.Message):
    __slots__ = ("block",)
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    block: _containers.RepeatedCompositeFieldContainer[_Tron_pb2.Block]
    def __init__(self, block: _Optional[_Iterable[_Union[_Tron_pb2.Block, _Mapping]]] = ...) -> None: ...

class TransactionList(_message.Message):
    __slots__ = ("transaction",)
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    transaction: _containers.RepeatedCompositeFieldContainer[_Tron_pb2.Transaction]
    def __init__(self, transaction: _Optional[_Iterable[_Union[_Tron_pb2.Transaction, _Mapping]]] = ...) -> None: ...

class TransactionIdList(_message.Message):
    __slots__ = ("txId",)
    TXID_FIELD_NUMBER: _ClassVar[int]
    txId: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, txId: _Optional[_Iterable[str]] = ...) -> None: ...

class DelegatedResourceMessage(_message.Message):
    __slots__ = ("fromAddress", "toAddress")
    FROMADDRESS_FIELD_NUMBER: _ClassVar[int]
    TOADDRESS_FIELD_NUMBER: _ClassVar[int]
    fromAddress: bytes
    toAddress: bytes
    def __init__(self, fromAddress: _Optional[bytes] = ..., toAddress: _Optional[bytes] = ...) -> None: ...

class DelegatedResourceList(_message.Message):
    __slots__ = ("delegatedResource",)
    DELEGATEDRESOURCE_FIELD_NUMBER: _ClassVar[int]
    delegatedResource: _containers.RepeatedCompositeFieldContainer[_Tron_pb2.DelegatedResource]
    def __init__(self, delegatedResource: _Optional[_Iterable[_Union[_Tron_pb2.DelegatedResource, _Mapping]]] = ...) -> None: ...

class GetAvailableUnfreezeCountRequestMessage(_message.Message):
    __slots__ = ("owner_address",)
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    def __init__(self, owner_address: _Optional[bytes] = ...) -> None: ...

class GetAvailableUnfreezeCountResponseMessage(_message.Message):
    __slots__ = ("count",)
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ...) -> None: ...

class CanDelegatedMaxSizeRequestMessage(_message.Message):
    __slots__ = ("type", "owner_address")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    type: int
    owner_address: bytes
    def __init__(self, type: _Optional[int] = ..., owner_address: _Optional[bytes] = ...) -> None: ...

class CanDelegatedMaxSizeResponseMessage(_message.Message):
    __slots__ = ("max_size",)
    MAX_SIZE_FIELD_NUMBER: _ClassVar[int]
    max_size: int
    def __init__(self, max_size: _Optional[int] = ...) -> None: ...

class CanWithdrawUnfreezeAmountRequestMessage(_message.Message):
    __slots__ = ("owner_address", "timestamp")
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    timestamp: int
    def __init__(self, owner_address: _Optional[bytes] = ..., timestamp: _Optional[int] = ...) -> None: ...

class CanWithdrawUnfreezeAmountResponseMessage(_message.Message):
    __slots__ = ("amount",)
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    amount: int
    def __init__(self, amount: _Optional[int] = ...) -> None: ...

class PricesResponseMessage(_message.Message):
    __slots__ = ("prices",)
    PRICES_FIELD_NUMBER: _ClassVar[int]
    prices: str
    def __init__(self, prices: _Optional[str] = ...) -> None: ...

class NodeList(_message.Message):
    __slots__ = ("nodes",)
    NODES_FIELD_NUMBER: _ClassVar[int]
    nodes: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(self, nodes: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...) -> None: ...

class Node(_message.Message):
    __slots__ = ("address",)
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: Address
    def __init__(self, address: _Optional[_Union[Address, _Mapping]] = ...) -> None: ...

class Address(_message.Message):
    __slots__ = ("host", "port")
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    host: bytes
    port: int
    def __init__(self, host: _Optional[bytes] = ..., port: _Optional[int] = ...) -> None: ...

class EmptyMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NumberMessage(_message.Message):
    __slots__ = ("num",)
    NUM_FIELD_NUMBER: _ClassVar[int]
    num: int
    def __init__(self, num: _Optional[int] = ...) -> None: ...

class BytesMessage(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bytes
    def __init__(self, value: _Optional[bytes] = ...) -> None: ...

class TimeMessage(_message.Message):
    __slots__ = ("beginInMilliseconds", "endInMilliseconds")
    BEGININMILLISECONDS_FIELD_NUMBER: _ClassVar[int]
    ENDINMILLISECONDS_FIELD_NUMBER: _ClassVar[int]
    beginInMilliseconds: int
    endInMilliseconds: int
    def __init__(self, beginInMilliseconds: _Optional[int] = ..., endInMilliseconds: _Optional[int] = ...) -> None: ...

class BlockReq(_message.Message):
    __slots__ = ("id_or_num", "detail")
    ID_OR_NUM_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    id_or_num: str
    detail: bool
    def __init__(self, id_or_num: _Optional[str] = ..., detail: bool = ...) -> None: ...

class BlockLimit(_message.Message):
    __slots__ = ("startNum", "endNum")
    STARTNUM_FIELD_NUMBER: _ClassVar[int]
    ENDNUM_FIELD_NUMBER: _ClassVar[int]
    startNum: int
    endNum: int
    def __init__(self, startNum: _Optional[int] = ..., endNum: _Optional[int] = ...) -> None: ...

class TransactionLimit(_message.Message):
    __slots__ = ("transactionId", "limitNum")
    TRANSACTIONID_FIELD_NUMBER: _ClassVar[int]
    LIMITNUM_FIELD_NUMBER: _ClassVar[int]
    transactionId: bytes
    limitNum: int
    def __init__(self, transactionId: _Optional[bytes] = ..., limitNum: _Optional[int] = ...) -> None: ...

class AccountPaginated(_message.Message):
    __slots__ = ("account", "offset", "limit")
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    account: _Tron_pb2.Account
    offset: int
    limit: int
    def __init__(self, account: _Optional[_Union[_Tron_pb2.Account, _Mapping]] = ..., offset: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class TimePaginatedMessage(_message.Message):
    __slots__ = ("timeMessage", "offset", "limit")
    TIMEMESSAGE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    timeMessage: TimeMessage
    offset: int
    limit: int
    def __init__(self, timeMessage: _Optional[_Union[TimeMessage, _Mapping]] = ..., offset: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class AccountNetMessage(_message.Message):
    __slots__ = ("freeNetUsed", "freeNetLimit", "NetUsed", "NetLimit", "assetNetUsed", "assetNetLimit", "TotalNetLimit", "TotalNetWeight")
    class AssetNetUsedEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class AssetNetLimitEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    FREENETUSED_FIELD_NUMBER: _ClassVar[int]
    FREENETLIMIT_FIELD_NUMBER: _ClassVar[int]
    NETUSED_FIELD_NUMBER: _ClassVar[int]
    NETLIMIT_FIELD_NUMBER: _ClassVar[int]
    ASSETNETUSED_FIELD_NUMBER: _ClassVar[int]
    ASSETNETLIMIT_FIELD_NUMBER: _ClassVar[int]
    TOTALNETLIMIT_FIELD_NUMBER: _ClassVar[int]
    TOTALNETWEIGHT_FIELD_NUMBER: _ClassVar[int]
    freeNetUsed: int
    freeNetLimit: int
    NetUsed: int
    NetLimit: int
    assetNetUsed: _containers.ScalarMap[str, int]
    assetNetLimit: _containers.ScalarMap[str, int]
    TotalNetLimit: int
    TotalNetWeight: int
    def __init__(self, freeNetUsed: _Optional[int] = ..., freeNetLimit: _Optional[int] = ..., NetUsed: _Optional[int] = ..., NetLimit: _Optional[int] = ..., assetNetUsed: _Optional[_Mapping[str, int]] = ..., assetNetLimit: _Optional[_Mapping[str, int]] = ..., TotalNetLimit: _Optional[int] = ..., TotalNetWeight: _Optional[int] = ...) -> None: ...

class AccountResourceMessage(_message.Message):
    __slots__ = ("freeNetUsed", "freeNetLimit", "NetUsed", "NetLimit", "assetNetUsed", "assetNetLimit", "TotalNetLimit", "TotalNetWeight", "TotalTronPowerWeight", "tronPowerUsed", "tronPowerLimit", "EnergyUsed", "EnergyLimit", "TotalEnergyLimit", "TotalEnergyWeight", "storageUsed", "storageLimit")
    class AssetNetUsedEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class AssetNetLimitEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    FREENETUSED_FIELD_NUMBER: _ClassVar[int]
    FREENETLIMIT_FIELD_NUMBER: _ClassVar[int]
    NETUSED_FIELD_NUMBER: _ClassVar[int]
    NETLIMIT_FIELD_NUMBER: _ClassVar[int]
    ASSETNETUSED_FIELD_NUMBER: _ClassVar[int]
    ASSETNETLIMIT_FIELD_NUMBER: _ClassVar[int]
    TOTALNETLIMIT_FIELD_NUMBER: _ClassVar[int]
    TOTALNETWEIGHT_FIELD_NUMBER: _ClassVar[int]
    TOTALTRONPOWERWEIGHT_FIELD_NUMBER: _ClassVar[int]
    TRONPOWERUSED_FIELD_NUMBER: _ClassVar[int]
    TRONPOWERLIMIT_FIELD_NUMBER: _ClassVar[int]
    ENERGYUSED_FIELD_NUMBER: _ClassVar[int]
    ENERGYLIMIT_FIELD_NUMBER: _ClassVar[int]
    TOTALENERGYLIMIT_FIELD_NUMBER: _ClassVar[int]
    TOTALENERGYWEIGHT_FIELD_NUMBER: _ClassVar[int]
    STORAGEUSED_FIELD_NUMBER: _ClassVar[int]
    STORAGELIMIT_FIELD_NUMBER: _ClassVar[int]
    freeNetUsed: int
    freeNetLimit: int
    NetUsed: int
    NetLimit: int
    assetNetUsed: _containers.ScalarMap[str, int]
    assetNetLimit: _containers.ScalarMap[str, int]
    TotalNetLimit: int
    TotalNetWeight: int
    TotalTronPowerWeight: int
    tronPowerUsed: int
    tronPowerLimit: int
    EnergyUsed: int
    EnergyLimit: int
    TotalEnergyLimit: int
    TotalEnergyWeight: int
    storageUsed: int
    storageLimit: int
    def __init__(self, freeNetUsed: _Optional[int] = ..., freeNetLimit: _Optional[int] = ..., NetUsed: _Optional[int] = ..., NetLimit: _Optional[int] = ..., assetNetUsed: _Optional[_Mapping[str, int]] = ..., assetNetLimit: _Optional[_Mapping[str, int]] = ..., TotalNetLimit: _Optional[int] = ..., TotalNetWeight: _Optional[int] = ..., TotalTronPowerWeight: _Optional[int] = ..., tronPowerUsed: _Optional[int] = ..., tronPowerLimit: _Optional[int] = ..., EnergyUsed: _Optional[int] = ..., EnergyLimit: _Optional[int] = ..., TotalEnergyLimit: _Optional[int] = ..., TotalEnergyWeight: _Optional[int] = ..., storageUsed: _Optional[int] = ..., storageLimit: _Optional[int] = ...) -> None: ...

class PaginatedMessage(_message.Message):
    __slots__ = ("offset", "limit")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    offset: int
    limit: int
    def __init__(self, offset: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class TransactionExtention(_message.Message):
    __slots__ = ("transaction", "txid", "constant_result", "result", "energy_used", "logs", "internal_transactions", "energy_penalty")
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    TXID_FIELD_NUMBER: _ClassVar[int]
    CONSTANT_RESULT_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ENERGY_USED_FIELD_NUMBER: _ClassVar[int]
    LOGS_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    ENERGY_PENALTY_FIELD_NUMBER: _ClassVar[int]
    transaction: _Tron_pb2.Transaction
    txid: bytes
    constant_result: _containers.RepeatedScalarFieldContainer[bytes]
    result: Return
    energy_used: int
    logs: _containers.RepeatedCompositeFieldContainer[_Tron_pb2.TransactionInfo.Log]
    internal_transactions: _containers.RepeatedCompositeFieldContainer[_Tron_pb2.InternalTransaction]
    energy_penalty: int
    def __init__(self, transaction: _Optional[_Union[_Tron_pb2.Transaction, _Mapping]] = ..., txid: _Optional[bytes] = ..., constant_result: _Optional[_Iterable[bytes]] = ..., result: _Optional[_Union[Return, _Mapping]] = ..., energy_used: _Optional[int] = ..., logs: _Optional[_Iterable[_Union[_Tron_pb2.TransactionInfo.Log, _Mapping]]] = ..., internal_transactions: _Optional[_Iterable[_Union[_Tron_pb2.InternalTransaction, _Mapping]]] = ..., energy_penalty: _Optional[int] = ...) -> None: ...

class EstimateEnergyMessage(_message.Message):
    __slots__ = ("result", "energy_required")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ENERGY_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    result: Return
    energy_required: int
    def __init__(self, result: _Optional[_Union[Return, _Mapping]] = ..., energy_required: _Optional[int] = ...) -> None: ...

class BlockExtention(_message.Message):
    __slots__ = ("transactions", "block_header", "blockid")
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    BLOCK_HEADER_FIELD_NUMBER: _ClassVar[int]
    BLOCKID_FIELD_NUMBER: _ClassVar[int]
    transactions: _containers.RepeatedCompositeFieldContainer[TransactionExtention]
    block_header: _Tron_pb2.BlockHeader
    blockid: bytes
    def __init__(self, transactions: _Optional[_Iterable[_Union[TransactionExtention, _Mapping]]] = ..., block_header: _Optional[_Union[_Tron_pb2.BlockHeader, _Mapping]] = ..., blockid: _Optional[bytes] = ...) -> None: ...

class BlockListExtention(_message.Message):
    __slots__ = ("block",)
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    block: _containers.RepeatedCompositeFieldContainer[BlockExtention]
    def __init__(self, block: _Optional[_Iterable[_Union[BlockExtention, _Mapping]]] = ...) -> None: ...

class TransactionListExtention(_message.Message):
    __slots__ = ("transaction",)
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    transaction: _containers.RepeatedCompositeFieldContainer[TransactionExtention]
    def __init__(self, transaction: _Optional[_Iterable[_Union[TransactionExtention, _Mapping]]] = ...) -> None: ...

class BlockIncrementalMerkleTree(_message.Message):
    __slots__ = ("number", "merkleTree")
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    MERKLETREE_FIELD_NUMBER: _ClassVar[int]
    number: int
    merkleTree: _shield_contract_pb2.IncrementalMerkleTree
    def __init__(self, number: _Optional[int] = ..., merkleTree: _Optional[_Union[_shield_contract_pb2.IncrementalMerkleTree, _Mapping]] = ...) -> None: ...

class TransactionSignWeight(_message.Message):
    __slots__ = ("permission", "approved_list", "current_weight", "result", "transaction")
    class Result(_message.Message):
        __slots__ = ("code", "message")
        class response_code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ENOUGH_PERMISSION: _ClassVar[TransactionSignWeight.Result.response_code]
            NOT_ENOUGH_PERMISSION: _ClassVar[TransactionSignWeight.Result.response_code]
            SIGNATURE_FORMAT_ERROR: _ClassVar[TransactionSignWeight.Result.response_code]
            COMPUTE_ADDRESS_ERROR: _ClassVar[TransactionSignWeight.Result.response_code]
            PERMISSION_ERROR: _ClassVar[TransactionSignWeight.Result.response_code]
            OTHER_ERROR: _ClassVar[TransactionSignWeight.Result.response_code]
        ENOUGH_PERMISSION: TransactionSignWeight.Result.response_code
        NOT_ENOUGH_PERMISSION: TransactionSignWeight.Result.response_code
        SIGNATURE_FORMAT_ERROR: TransactionSignWeight.Result.response_code
        COMPUTE_ADDRESS_ERROR: TransactionSignWeight.Result.response_code
        PERMISSION_ERROR: TransactionSignWeight.Result.response_code
        OTHER_ERROR: TransactionSignWeight.Result.response_code
        CODE_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        code: TransactionSignWeight.Result.response_code
        message: str
        def __init__(self, code: _Optional[_Union[TransactionSignWeight.Result.response_code, str]] = ..., message: _Optional[str] = ...) -> None: ...
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    APPROVED_LIST_FIELD_NUMBER: _ClassVar[int]
    CURRENT_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    permission: _Tron_pb2.Permission
    approved_list: _containers.RepeatedScalarFieldContainer[bytes]
    current_weight: int
    result: TransactionSignWeight.Result
    transaction: TransactionExtention
    def __init__(self, permission: _Optional[_Union[_Tron_pb2.Permission, _Mapping]] = ..., approved_list: _Optional[_Iterable[bytes]] = ..., current_weight: _Optional[int] = ..., result: _Optional[_Union[TransactionSignWeight.Result, _Mapping]] = ..., transaction: _Optional[_Union[TransactionExtention, _Mapping]] = ...) -> None: ...

class TransactionApprovedList(_message.Message):
    __slots__ = ("approved_list", "result", "transaction")
    class Result(_message.Message):
        __slots__ = ("code", "message")
        class response_code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SUCCESS: _ClassVar[TransactionApprovedList.Result.response_code]
            SIGNATURE_FORMAT_ERROR: _ClassVar[TransactionApprovedList.Result.response_code]
            COMPUTE_ADDRESS_ERROR: _ClassVar[TransactionApprovedList.Result.response_code]
            OTHER_ERROR: _ClassVar[TransactionApprovedList.Result.response_code]
        SUCCESS: TransactionApprovedList.Result.response_code
        SIGNATURE_FORMAT_ERROR: TransactionApprovedList.Result.response_code
        COMPUTE_ADDRESS_ERROR: TransactionApprovedList.Result.response_code
        OTHER_ERROR: TransactionApprovedList.Result.response_code
        CODE_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        code: TransactionApprovedList.Result.response_code
        message: str
        def __init__(self, code: _Optional[_Union[TransactionApprovedList.Result.response_code, str]] = ..., message: _Optional[str] = ...) -> None: ...
    APPROVED_LIST_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    approved_list: _containers.RepeatedScalarFieldContainer[bytes]
    result: TransactionApprovedList.Result
    transaction: TransactionExtention
    def __init__(self, approved_list: _Optional[_Iterable[bytes]] = ..., result: _Optional[_Union[TransactionApprovedList.Result, _Mapping]] = ..., transaction: _Optional[_Union[TransactionExtention, _Mapping]] = ...) -> None: ...

class IvkDecryptParameters(_message.Message):
    __slots__ = ("start_block_index", "end_block_index", "ivk")
    START_BLOCK_INDEX_FIELD_NUMBER: _ClassVar[int]
    END_BLOCK_INDEX_FIELD_NUMBER: _ClassVar[int]
    IVK_FIELD_NUMBER: _ClassVar[int]
    start_block_index: int
    end_block_index: int
    ivk: bytes
    def __init__(self, start_block_index: _Optional[int] = ..., end_block_index: _Optional[int] = ..., ivk: _Optional[bytes] = ...) -> None: ...

class IvkDecryptAndMarkParameters(_message.Message):
    __slots__ = ("start_block_index", "end_block_index", "ivk", "ak", "nk")
    START_BLOCK_INDEX_FIELD_NUMBER: _ClassVar[int]
    END_BLOCK_INDEX_FIELD_NUMBER: _ClassVar[int]
    IVK_FIELD_NUMBER: _ClassVar[int]
    AK_FIELD_NUMBER: _ClassVar[int]
    NK_FIELD_NUMBER: _ClassVar[int]
    start_block_index: int
    end_block_index: int
    ivk: bytes
    ak: bytes
    nk: bytes
    def __init__(self, start_block_index: _Optional[int] = ..., end_block_index: _Optional[int] = ..., ivk: _Optional[bytes] = ..., ak: _Optional[bytes] = ..., nk: _Optional[bytes] = ...) -> None: ...

class OvkDecryptParameters(_message.Message):
    __slots__ = ("start_block_index", "end_block_index", "ovk")
    START_BLOCK_INDEX_FIELD_NUMBER: _ClassVar[int]
    END_BLOCK_INDEX_FIELD_NUMBER: _ClassVar[int]
    OVK_FIELD_NUMBER: _ClassVar[int]
    start_block_index: int
    end_block_index: int
    ovk: bytes
    def __init__(self, start_block_index: _Optional[int] = ..., end_block_index: _Optional[int] = ..., ovk: _Optional[bytes] = ...) -> None: ...

class DecryptNotes(_message.Message):
    __slots__ = ("noteTxs",)
    class NoteTx(_message.Message):
        __slots__ = ("note", "txid", "index")
        NOTE_FIELD_NUMBER: _ClassVar[int]
        TXID_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        note: Note
        txid: bytes
        index: int
        def __init__(self, note: _Optional[_Union[Note, _Mapping]] = ..., txid: _Optional[bytes] = ..., index: _Optional[int] = ...) -> None: ...
    NOTETXS_FIELD_NUMBER: _ClassVar[int]
    noteTxs: _containers.RepeatedCompositeFieldContainer[DecryptNotes.NoteTx]
    def __init__(self, noteTxs: _Optional[_Iterable[_Union[DecryptNotes.NoteTx, _Mapping]]] = ...) -> None: ...

class DecryptNotesMarked(_message.Message):
    __slots__ = ("noteTxs",)
    class NoteTx(_message.Message):
        __slots__ = ("note", "txid", "index", "is_spend")
        NOTE_FIELD_NUMBER: _ClassVar[int]
        TXID_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        IS_SPEND_FIELD_NUMBER: _ClassVar[int]
        note: Note
        txid: bytes
        index: int
        is_spend: bool
        def __init__(self, note: _Optional[_Union[Note, _Mapping]] = ..., txid: _Optional[bytes] = ..., index: _Optional[int] = ..., is_spend: bool = ...) -> None: ...
    NOTETXS_FIELD_NUMBER: _ClassVar[int]
    noteTxs: _containers.RepeatedCompositeFieldContainer[DecryptNotesMarked.NoteTx]
    def __init__(self, noteTxs: _Optional[_Iterable[_Union[DecryptNotesMarked.NoteTx, _Mapping]]] = ...) -> None: ...

class Note(_message.Message):
    __slots__ = ("value", "payment_address", "rcm", "memo")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    RCM_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    value: int
    payment_address: str
    rcm: bytes
    memo: bytes
    def __init__(self, value: _Optional[int] = ..., payment_address: _Optional[str] = ..., rcm: _Optional[bytes] = ..., memo: _Optional[bytes] = ...) -> None: ...

class SpendNote(_message.Message):
    __slots__ = ("note", "alpha", "voucher", "path")
    NOTE_FIELD_NUMBER: _ClassVar[int]
    ALPHA_FIELD_NUMBER: _ClassVar[int]
    VOUCHER_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    note: Note
    alpha: bytes
    voucher: _shield_contract_pb2.IncrementalMerkleVoucher
    path: bytes
    def __init__(self, note: _Optional[_Union[Note, _Mapping]] = ..., alpha: _Optional[bytes] = ..., voucher: _Optional[_Union[_shield_contract_pb2.IncrementalMerkleVoucher, _Mapping]] = ..., path: _Optional[bytes] = ...) -> None: ...

class ReceiveNote(_message.Message):
    __slots__ = ("note",)
    NOTE_FIELD_NUMBER: _ClassVar[int]
    note: Note
    def __init__(self, note: _Optional[_Union[Note, _Mapping]] = ...) -> None: ...

class PrivateParameters(_message.Message):
    __slots__ = ("transparent_from_address", "ask", "nsk", "ovk", "from_amount", "shielded_spends", "shielded_receives", "transparent_to_address", "to_amount", "timeout")
    TRANSPARENT_FROM_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ASK_FIELD_NUMBER: _ClassVar[int]
    NSK_FIELD_NUMBER: _ClassVar[int]
    OVK_FIELD_NUMBER: _ClassVar[int]
    FROM_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    SHIELDED_SPENDS_FIELD_NUMBER: _ClassVar[int]
    SHIELDED_RECEIVES_FIELD_NUMBER: _ClassVar[int]
    TRANSPARENT_TO_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TO_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    transparent_from_address: bytes
    ask: bytes
    nsk: bytes
    ovk: bytes
    from_amount: int
    shielded_spends: _containers.RepeatedCompositeFieldContainer[SpendNote]
    shielded_receives: _containers.RepeatedCompositeFieldContainer[ReceiveNote]
    transparent_to_address: bytes
    to_amount: int
    timeout: int
    def __init__(self, transparent_from_address: _Optional[bytes] = ..., ask: _Optional[bytes] = ..., nsk: _Optional[bytes] = ..., ovk: _Optional[bytes] = ..., from_amount: _Optional[int] = ..., shielded_spends: _Optional[_Iterable[_Union[SpendNote, _Mapping]]] = ..., shielded_receives: _Optional[_Iterable[_Union[ReceiveNote, _Mapping]]] = ..., transparent_to_address: _Optional[bytes] = ..., to_amount: _Optional[int] = ..., timeout: _Optional[int] = ...) -> None: ...

class PrivateParametersWithoutAsk(_message.Message):
    __slots__ = ("transparent_from_address", "ak", "nsk", "ovk", "from_amount", "shielded_spends", "shielded_receives", "transparent_to_address", "to_amount", "timeout")
    TRANSPARENT_FROM_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    AK_FIELD_NUMBER: _ClassVar[int]
    NSK_FIELD_NUMBER: _ClassVar[int]
    OVK_FIELD_NUMBER: _ClassVar[int]
    FROM_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    SHIELDED_SPENDS_FIELD_NUMBER: _ClassVar[int]
    SHIELDED_RECEIVES_FIELD_NUMBER: _ClassVar[int]
    TRANSPARENT_TO_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TO_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    transparent_from_address: bytes
    ak: bytes
    nsk: bytes
    ovk: bytes
    from_amount: int
    shielded_spends: _containers.RepeatedCompositeFieldContainer[SpendNote]
    shielded_receives: _containers.RepeatedCompositeFieldContainer[ReceiveNote]
    transparent_to_address: bytes
    to_amount: int
    timeout: int
    def __init__(self, transparent_from_address: _Optional[bytes] = ..., ak: _Optional[bytes] = ..., nsk: _Optional[bytes] = ..., ovk: _Optional[bytes] = ..., from_amount: _Optional[int] = ..., shielded_spends: _Optional[_Iterable[_Union[SpendNote, _Mapping]]] = ..., shielded_receives: _Optional[_Iterable[_Union[ReceiveNote, _Mapping]]] = ..., transparent_to_address: _Optional[bytes] = ..., to_amount: _Optional[int] = ..., timeout: _Optional[int] = ...) -> None: ...

class SpendAuthSigParameters(_message.Message):
    __slots__ = ("ask", "tx_hash", "alpha")
    ASK_FIELD_NUMBER: _ClassVar[int]
    TX_HASH_FIELD_NUMBER: _ClassVar[int]
    ALPHA_FIELD_NUMBER: _ClassVar[int]
    ask: bytes
    tx_hash: bytes
    alpha: bytes
    def __init__(self, ask: _Optional[bytes] = ..., tx_hash: _Optional[bytes] = ..., alpha: _Optional[bytes] = ...) -> None: ...

class NfParameters(_message.Message):
    __slots__ = ("note", "voucher", "ak", "nk")
    NOTE_FIELD_NUMBER: _ClassVar[int]
    VOUCHER_FIELD_NUMBER: _ClassVar[int]
    AK_FIELD_NUMBER: _ClassVar[int]
    NK_FIELD_NUMBER: _ClassVar[int]
    note: Note
    voucher: _shield_contract_pb2.IncrementalMerkleVoucher
    ak: bytes
    nk: bytes
    def __init__(self, note: _Optional[_Union[Note, _Mapping]] = ..., voucher: _Optional[_Union[_shield_contract_pb2.IncrementalMerkleVoucher, _Mapping]] = ..., ak: _Optional[bytes] = ..., nk: _Optional[bytes] = ...) -> None: ...

class ExpandedSpendingKeyMessage(_message.Message):
    __slots__ = ("ask", "nsk", "ovk")
    ASK_FIELD_NUMBER: _ClassVar[int]
    NSK_FIELD_NUMBER: _ClassVar[int]
    OVK_FIELD_NUMBER: _ClassVar[int]
    ask: bytes
    nsk: bytes
    ovk: bytes
    def __init__(self, ask: _Optional[bytes] = ..., nsk: _Optional[bytes] = ..., ovk: _Optional[bytes] = ...) -> None: ...

class ViewingKeyMessage(_message.Message):
    __slots__ = ("ak", "nk")
    AK_FIELD_NUMBER: _ClassVar[int]
    NK_FIELD_NUMBER: _ClassVar[int]
    ak: bytes
    nk: bytes
    def __init__(self, ak: _Optional[bytes] = ..., nk: _Optional[bytes] = ...) -> None: ...

class IncomingViewingKeyMessage(_message.Message):
    __slots__ = ("ivk",)
    IVK_FIELD_NUMBER: _ClassVar[int]
    ivk: bytes
    def __init__(self, ivk: _Optional[bytes] = ...) -> None: ...

class DiversifierMessage(_message.Message):
    __slots__ = ("d",)
    D_FIELD_NUMBER: _ClassVar[int]
    d: bytes
    def __init__(self, d: _Optional[bytes] = ...) -> None: ...

class IncomingViewingKeyDiversifierMessage(_message.Message):
    __slots__ = ("ivk", "d")
    IVK_FIELD_NUMBER: _ClassVar[int]
    D_FIELD_NUMBER: _ClassVar[int]
    ivk: IncomingViewingKeyMessage
    d: DiversifierMessage
    def __init__(self, ivk: _Optional[_Union[IncomingViewingKeyMessage, _Mapping]] = ..., d: _Optional[_Union[DiversifierMessage, _Mapping]] = ...) -> None: ...

class PaymentAddressMessage(_message.Message):
    __slots__ = ("d", "pkD", "payment_address")
    D_FIELD_NUMBER: _ClassVar[int]
    PKD_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    d: DiversifierMessage
    pkD: bytes
    payment_address: str
    def __init__(self, d: _Optional[_Union[DiversifierMessage, _Mapping]] = ..., pkD: _Optional[bytes] = ..., payment_address: _Optional[str] = ...) -> None: ...

class ShieldedAddressInfo(_message.Message):
    __slots__ = ("sk", "ask", "nsk", "ovk", "ak", "nk", "ivk", "d", "pkD", "payment_address")
    SK_FIELD_NUMBER: _ClassVar[int]
    ASK_FIELD_NUMBER: _ClassVar[int]
    NSK_FIELD_NUMBER: _ClassVar[int]
    OVK_FIELD_NUMBER: _ClassVar[int]
    AK_FIELD_NUMBER: _ClassVar[int]
    NK_FIELD_NUMBER: _ClassVar[int]
    IVK_FIELD_NUMBER: _ClassVar[int]
    D_FIELD_NUMBER: _ClassVar[int]
    PKD_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    sk: bytes
    ask: bytes
    nsk: bytes
    ovk: bytes
    ak: bytes
    nk: bytes
    ivk: bytes
    d: bytes
    pkD: bytes
    payment_address: str
    def __init__(self, sk: _Optional[bytes] = ..., ask: _Optional[bytes] = ..., nsk: _Optional[bytes] = ..., ovk: _Optional[bytes] = ..., ak: _Optional[bytes] = ..., nk: _Optional[bytes] = ..., ivk: _Optional[bytes] = ..., d: _Optional[bytes] = ..., pkD: _Optional[bytes] = ..., payment_address: _Optional[str] = ...) -> None: ...

class NoteParameters(_message.Message):
    __slots__ = ("ak", "nk", "note", "txid", "index")
    AK_FIELD_NUMBER: _ClassVar[int]
    NK_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    TXID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    ak: bytes
    nk: bytes
    note: Note
    txid: bytes
    index: int
    def __init__(self, ak: _Optional[bytes] = ..., nk: _Optional[bytes] = ..., note: _Optional[_Union[Note, _Mapping]] = ..., txid: _Optional[bytes] = ..., index: _Optional[int] = ...) -> None: ...

class SpendResult(_message.Message):
    __slots__ = ("result", "message")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    result: bool
    message: str
    def __init__(self, result: bool = ..., message: _Optional[str] = ...) -> None: ...

class TransactionInfoList(_message.Message):
    __slots__ = ("transactionInfo",)
    TRANSACTIONINFO_FIELD_NUMBER: _ClassVar[int]
    transactionInfo: _containers.RepeatedCompositeFieldContainer[_Tron_pb2.TransactionInfo]
    def __init__(self, transactionInfo: _Optional[_Iterable[_Union[_Tron_pb2.TransactionInfo, _Mapping]]] = ...) -> None: ...

class SpendNoteTRC20(_message.Message):
    __slots__ = ("note", "alpha", "root", "path", "pos")
    NOTE_FIELD_NUMBER: _ClassVar[int]
    ALPHA_FIELD_NUMBER: _ClassVar[int]
    ROOT_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    note: Note
    alpha: bytes
    root: bytes
    path: bytes
    pos: int
    def __init__(self, note: _Optional[_Union[Note, _Mapping]] = ..., alpha: _Optional[bytes] = ..., root: _Optional[bytes] = ..., path: _Optional[bytes] = ..., pos: _Optional[int] = ...) -> None: ...

class PrivateShieldedTRC20Parameters(_message.Message):
    __slots__ = ("ask", "nsk", "ovk", "from_amount", "shielded_spends", "shielded_receives", "transparent_to_address", "to_amount", "shielded_TRC20_contract_address")
    ASK_FIELD_NUMBER: _ClassVar[int]
    NSK_FIELD_NUMBER: _ClassVar[int]
    OVK_FIELD_NUMBER: _ClassVar[int]
    FROM_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    SHIELDED_SPENDS_FIELD_NUMBER: _ClassVar[int]
    SHIELDED_RECEIVES_FIELD_NUMBER: _ClassVar[int]
    TRANSPARENT_TO_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TO_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    SHIELDED_TRC20_CONTRACT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ask: bytes
    nsk: bytes
    ovk: bytes
    from_amount: str
    shielded_spends: _containers.RepeatedCompositeFieldContainer[SpendNoteTRC20]
    shielded_receives: _containers.RepeatedCompositeFieldContainer[ReceiveNote]
    transparent_to_address: bytes
    to_amount: str
    shielded_TRC20_contract_address: bytes
    def __init__(self, ask: _Optional[bytes] = ..., nsk: _Optional[bytes] = ..., ovk: _Optional[bytes] = ..., from_amount: _Optional[str] = ..., shielded_spends: _Optional[_Iterable[_Union[SpendNoteTRC20, _Mapping]]] = ..., shielded_receives: _Optional[_Iterable[_Union[ReceiveNote, _Mapping]]] = ..., transparent_to_address: _Optional[bytes] = ..., to_amount: _Optional[str] = ..., shielded_TRC20_contract_address: _Optional[bytes] = ...) -> None: ...

class PrivateShieldedTRC20ParametersWithoutAsk(_message.Message):
    __slots__ = ("ak", "nsk", "ovk", "from_amount", "shielded_spends", "shielded_receives", "transparent_to_address", "to_amount", "shielded_TRC20_contract_address")
    AK_FIELD_NUMBER: _ClassVar[int]
    NSK_FIELD_NUMBER: _ClassVar[int]
    OVK_FIELD_NUMBER: _ClassVar[int]
    FROM_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    SHIELDED_SPENDS_FIELD_NUMBER: _ClassVar[int]
    SHIELDED_RECEIVES_FIELD_NUMBER: _ClassVar[int]
    TRANSPARENT_TO_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TO_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    SHIELDED_TRC20_CONTRACT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ak: bytes
    nsk: bytes
    ovk: bytes
    from_amount: str
    shielded_spends: _containers.RepeatedCompositeFieldContainer[SpendNoteTRC20]
    shielded_receives: _containers.RepeatedCompositeFieldContainer[ReceiveNote]
    transparent_to_address: bytes
    to_amount: str
    shielded_TRC20_contract_address: bytes
    def __init__(self, ak: _Optional[bytes] = ..., nsk: _Optional[bytes] = ..., ovk: _Optional[bytes] = ..., from_amount: _Optional[str] = ..., shielded_spends: _Optional[_Iterable[_Union[SpendNoteTRC20, _Mapping]]] = ..., shielded_receives: _Optional[_Iterable[_Union[ReceiveNote, _Mapping]]] = ..., transparent_to_address: _Optional[bytes] = ..., to_amount: _Optional[str] = ..., shielded_TRC20_contract_address: _Optional[bytes] = ...) -> None: ...

class ShieldedTRC20Parameters(_message.Message):
    __slots__ = ("spend_description", "receive_description", "binding_signature", "message_hash", "trigger_contract_input", "parameter_type")
    SPEND_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RECEIVE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BINDING_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_HASH_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_CONTRACT_INPUT_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_TYPE_FIELD_NUMBER: _ClassVar[int]
    spend_description: _containers.RepeatedCompositeFieldContainer[_shield_contract_pb2.SpendDescription]
    receive_description: _containers.RepeatedCompositeFieldContainer[_shield_contract_pb2.ReceiveDescription]
    binding_signature: bytes
    message_hash: bytes
    trigger_contract_input: str
    parameter_type: str
    def __init__(self, spend_description: _Optional[_Iterable[_Union[_shield_contract_pb2.SpendDescription, _Mapping]]] = ..., receive_description: _Optional[_Iterable[_Union[_shield_contract_pb2.ReceiveDescription, _Mapping]]] = ..., binding_signature: _Optional[bytes] = ..., message_hash: _Optional[bytes] = ..., trigger_contract_input: _Optional[str] = ..., parameter_type: _Optional[str] = ...) -> None: ...

class IvkDecryptTRC20Parameters(_message.Message):
    __slots__ = ("start_block_index", "end_block_index", "shielded_TRC20_contract_address", "ivk", "ak", "nk", "events")
    START_BLOCK_INDEX_FIELD_NUMBER: _ClassVar[int]
    END_BLOCK_INDEX_FIELD_NUMBER: _ClassVar[int]
    SHIELDED_TRC20_CONTRACT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    IVK_FIELD_NUMBER: _ClassVar[int]
    AK_FIELD_NUMBER: _ClassVar[int]
    NK_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    start_block_index: int
    end_block_index: int
    shielded_TRC20_contract_address: bytes
    ivk: bytes
    ak: bytes
    nk: bytes
    events: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, start_block_index: _Optional[int] = ..., end_block_index: _Optional[int] = ..., shielded_TRC20_contract_address: _Optional[bytes] = ..., ivk: _Optional[bytes] = ..., ak: _Optional[bytes] = ..., nk: _Optional[bytes] = ..., events: _Optional[_Iterable[str]] = ...) -> None: ...

class OvkDecryptTRC20Parameters(_message.Message):
    __slots__ = ("start_block_index", "end_block_index", "ovk", "shielded_TRC20_contract_address", "events")
    START_BLOCK_INDEX_FIELD_NUMBER: _ClassVar[int]
    END_BLOCK_INDEX_FIELD_NUMBER: _ClassVar[int]
    OVK_FIELD_NUMBER: _ClassVar[int]
    SHIELDED_TRC20_CONTRACT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    start_block_index: int
    end_block_index: int
    ovk: bytes
    shielded_TRC20_contract_address: bytes
    events: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, start_block_index: _Optional[int] = ..., end_block_index: _Optional[int] = ..., ovk: _Optional[bytes] = ..., shielded_TRC20_contract_address: _Optional[bytes] = ..., events: _Optional[_Iterable[str]] = ...) -> None: ...

class DecryptNotesTRC20(_message.Message):
    __slots__ = ("noteTxs",)
    class NoteTx(_message.Message):
        __slots__ = ("note", "position", "is_spent", "txid", "index", "to_amount", "transparent_to_address")
        NOTE_FIELD_NUMBER: _ClassVar[int]
        POSITION_FIELD_NUMBER: _ClassVar[int]
        IS_SPENT_FIELD_NUMBER: _ClassVar[int]
        TXID_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        TO_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        TRANSPARENT_TO_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        note: Note
        position: int
        is_spent: bool
        txid: bytes
        index: int
        to_amount: str
        transparent_to_address: bytes
        def __init__(self, note: _Optional[_Union[Note, _Mapping]] = ..., position: _Optional[int] = ..., is_spent: bool = ..., txid: _Optional[bytes] = ..., index: _Optional[int] = ..., to_amount: _Optional[str] = ..., transparent_to_address: _Optional[bytes] = ...) -> None: ...
    NOTETXS_FIELD_NUMBER: _ClassVar[int]
    noteTxs: _containers.RepeatedCompositeFieldContainer[DecryptNotesTRC20.NoteTx]
    def __init__(self, noteTxs: _Optional[_Iterable[_Union[DecryptNotesTRC20.NoteTx, _Mapping]]] = ...) -> None: ...

class NfTRC20Parameters(_message.Message):
    __slots__ = ("note", "ak", "nk", "position", "shielded_TRC20_contract_address")
    NOTE_FIELD_NUMBER: _ClassVar[int]
    AK_FIELD_NUMBER: _ClassVar[int]
    NK_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    SHIELDED_TRC20_CONTRACT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    note: Note
    ak: bytes
    nk: bytes
    position: int
    shielded_TRC20_contract_address: bytes
    def __init__(self, note: _Optional[_Union[Note, _Mapping]] = ..., ak: _Optional[bytes] = ..., nk: _Optional[bytes] = ..., position: _Optional[int] = ..., shielded_TRC20_contract_address: _Optional[bytes] = ...) -> None: ...

class NullifierResult(_message.Message):
    __slots__ = ("is_spent",)
    IS_SPENT_FIELD_NUMBER: _ClassVar[int]
    is_spent: bool
    def __init__(self, is_spent: bool = ...) -> None: ...

class ShieldedTRC20TriggerContractParameters(_message.Message):
    __slots__ = ("shielded_TRC20_Parameters", "spend_authority_signature", "amount", "transparent_to_address")
    SHIELDED_TRC20_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    SPEND_AUTHORITY_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TRANSPARENT_TO_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    shielded_TRC20_Parameters: ShieldedTRC20Parameters
    spend_authority_signature: _containers.RepeatedCompositeFieldContainer[BytesMessage]
    amount: str
    transparent_to_address: bytes
    def __init__(self, shielded_TRC20_Parameters: _Optional[_Union[ShieldedTRC20Parameters, _Mapping]] = ..., spend_authority_signature: _Optional[_Iterable[_Union[BytesMessage, _Mapping]]] = ..., amount: _Optional[str] = ..., transparent_to_address: _Optional[bytes] = ...) -> None: ...
