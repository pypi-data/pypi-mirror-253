from google.protobuf import any_pb2 as _any_pb2
from tron_api.grpc.core import Discover_pb2 as _Discover_pb2
from tron_api.grpc.core.contract import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccountType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Normal: _ClassVar[AccountType]
    AssetIssue: _ClassVar[AccountType]
    Contract: _ClassVar[AccountType]

class ReasonCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REQUESTED: _ClassVar[ReasonCode]
    BAD_PROTOCOL: _ClassVar[ReasonCode]
    TOO_MANY_PEERS: _ClassVar[ReasonCode]
    DUPLICATE_PEER: _ClassVar[ReasonCode]
    INCOMPATIBLE_PROTOCOL: _ClassVar[ReasonCode]
    RANDOM_ELIMINATION: _ClassVar[ReasonCode]
    PEER_QUITING: _ClassVar[ReasonCode]
    UNEXPECTED_IDENTITY: _ClassVar[ReasonCode]
    LOCAL_IDENTITY: _ClassVar[ReasonCode]
    PING_TIMEOUT: _ClassVar[ReasonCode]
    USER_REASON: _ClassVar[ReasonCode]
    RESET: _ClassVar[ReasonCode]
    SYNC_FAIL: _ClassVar[ReasonCode]
    FETCH_FAIL: _ClassVar[ReasonCode]
    BAD_TX: _ClassVar[ReasonCode]
    BAD_BLOCK: _ClassVar[ReasonCode]
    FORKED: _ClassVar[ReasonCode]
    UNLINKABLE: _ClassVar[ReasonCode]
    INCOMPATIBLE_VERSION: _ClassVar[ReasonCode]
    INCOMPATIBLE_CHAIN: _ClassVar[ReasonCode]
    TIME_OUT: _ClassVar[ReasonCode]
    CONNECT_FAIL: _ClassVar[ReasonCode]
    TOO_MANY_PEERS_WITH_SAME_IP: _ClassVar[ReasonCode]
    LIGHT_NODE_SYNC_FAIL: _ClassVar[ReasonCode]
    BELOW_THAN_ME: _ClassVar[ReasonCode]
    NOT_WITNESS: _ClassVar[ReasonCode]
    NO_SUCH_MESSAGE: _ClassVar[ReasonCode]
    UNKNOWN: _ClassVar[ReasonCode]
Normal: AccountType
AssetIssue: AccountType
Contract: AccountType
REQUESTED: ReasonCode
BAD_PROTOCOL: ReasonCode
TOO_MANY_PEERS: ReasonCode
DUPLICATE_PEER: ReasonCode
INCOMPATIBLE_PROTOCOL: ReasonCode
RANDOM_ELIMINATION: ReasonCode
PEER_QUITING: ReasonCode
UNEXPECTED_IDENTITY: ReasonCode
LOCAL_IDENTITY: ReasonCode
PING_TIMEOUT: ReasonCode
USER_REASON: ReasonCode
RESET: ReasonCode
SYNC_FAIL: ReasonCode
FETCH_FAIL: ReasonCode
BAD_TX: ReasonCode
BAD_BLOCK: ReasonCode
FORKED: ReasonCode
UNLINKABLE: ReasonCode
INCOMPATIBLE_VERSION: ReasonCode
INCOMPATIBLE_CHAIN: ReasonCode
TIME_OUT: ReasonCode
CONNECT_FAIL: ReasonCode
TOO_MANY_PEERS_WITH_SAME_IP: ReasonCode
LIGHT_NODE_SYNC_FAIL: ReasonCode
BELOW_THAN_ME: ReasonCode
NOT_WITNESS: ReasonCode
NO_SUCH_MESSAGE: ReasonCode
UNKNOWN: ReasonCode

class AccountId(_message.Message):
    __slots__ = ("name", "address")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    name: bytes
    address: bytes
    def __init__(self, name: _Optional[bytes] = ..., address: _Optional[bytes] = ...) -> None: ...

class Vote(_message.Message):
    __slots__ = ("vote_address", "vote_count")
    VOTE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VOTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    vote_address: bytes
    vote_count: int
    def __init__(self, vote_address: _Optional[bytes] = ..., vote_count: _Optional[int] = ...) -> None: ...

class Proposal(_message.Message):
    __slots__ = ("proposal_id", "proposer_address", "parameters", "expiration_time", "create_time", "approvals", "state")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PENDING: _ClassVar[Proposal.State]
        DISAPPROVED: _ClassVar[Proposal.State]
        APPROVED: _ClassVar[Proposal.State]
        CANCELED: _ClassVar[Proposal.State]
    PENDING: Proposal.State
    DISAPPROVED: Proposal.State
    APPROVED: Proposal.State
    CANCELED: Proposal.State
    class ParametersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    PROPOSAL_ID_FIELD_NUMBER: _ClassVar[int]
    PROPOSER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    APPROVALS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    proposal_id: int
    proposer_address: bytes
    parameters: _containers.ScalarMap[int, int]
    expiration_time: int
    create_time: int
    approvals: _containers.RepeatedScalarFieldContainer[bytes]
    state: Proposal.State
    def __init__(self, proposal_id: _Optional[int] = ..., proposer_address: _Optional[bytes] = ..., parameters: _Optional[_Mapping[int, int]] = ..., expiration_time: _Optional[int] = ..., create_time: _Optional[int] = ..., approvals: _Optional[_Iterable[bytes]] = ..., state: _Optional[_Union[Proposal.State, str]] = ...) -> None: ...

class Exchange(_message.Message):
    __slots__ = ("exchange_id", "creator_address", "create_time", "first_token_id", "first_token_balance", "second_token_id", "second_token_balance")
    EXCHANGE_ID_FIELD_NUMBER: _ClassVar[int]
    CREATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    FIRST_TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_TOKEN_BALANCE_FIELD_NUMBER: _ClassVar[int]
    SECOND_TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    SECOND_TOKEN_BALANCE_FIELD_NUMBER: _ClassVar[int]
    exchange_id: int
    creator_address: bytes
    create_time: int
    first_token_id: bytes
    first_token_balance: int
    second_token_id: bytes
    second_token_balance: int
    def __init__(self, exchange_id: _Optional[int] = ..., creator_address: _Optional[bytes] = ..., create_time: _Optional[int] = ..., first_token_id: _Optional[bytes] = ..., first_token_balance: _Optional[int] = ..., second_token_id: _Optional[bytes] = ..., second_token_balance: _Optional[int] = ...) -> None: ...

class MarketOrder(_message.Message):
    __slots__ = ("order_id", "owner_address", "create_time", "sell_token_id", "sell_token_quantity", "buy_token_id", "buy_token_quantity", "sell_token_quantity_remain", "sell_token_quantity_return", "state", "prev", "next")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACTIVE: _ClassVar[MarketOrder.State]
        INACTIVE: _ClassVar[MarketOrder.State]
        CANCELED: _ClassVar[MarketOrder.State]
    ACTIVE: MarketOrder.State
    INACTIVE: MarketOrder.State
    CANCELED: MarketOrder.State
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SELL_TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    SELL_TOKEN_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    BUY_TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    BUY_TOKEN_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    SELL_TOKEN_QUANTITY_REMAIN_FIELD_NUMBER: _ClassVar[int]
    SELL_TOKEN_QUANTITY_RETURN_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PREV_FIELD_NUMBER: _ClassVar[int]
    NEXT_FIELD_NUMBER: _ClassVar[int]
    order_id: bytes
    owner_address: bytes
    create_time: int
    sell_token_id: bytes
    sell_token_quantity: int
    buy_token_id: bytes
    buy_token_quantity: int
    sell_token_quantity_remain: int
    sell_token_quantity_return: int
    state: MarketOrder.State
    prev: bytes
    next: bytes
    def __init__(self, order_id: _Optional[bytes] = ..., owner_address: _Optional[bytes] = ..., create_time: _Optional[int] = ..., sell_token_id: _Optional[bytes] = ..., sell_token_quantity: _Optional[int] = ..., buy_token_id: _Optional[bytes] = ..., buy_token_quantity: _Optional[int] = ..., sell_token_quantity_remain: _Optional[int] = ..., sell_token_quantity_return: _Optional[int] = ..., state: _Optional[_Union[MarketOrder.State, str]] = ..., prev: _Optional[bytes] = ..., next: _Optional[bytes] = ...) -> None: ...

class MarketOrderList(_message.Message):
    __slots__ = ("orders",)
    ORDERS_FIELD_NUMBER: _ClassVar[int]
    orders: _containers.RepeatedCompositeFieldContainer[MarketOrder]
    def __init__(self, orders: _Optional[_Iterable[_Union[MarketOrder, _Mapping]]] = ...) -> None: ...

class MarketOrderPairList(_message.Message):
    __slots__ = ("orderPair",)
    ORDERPAIR_FIELD_NUMBER: _ClassVar[int]
    orderPair: _containers.RepeatedCompositeFieldContainer[MarketOrderPair]
    def __init__(self, orderPair: _Optional[_Iterable[_Union[MarketOrderPair, _Mapping]]] = ...) -> None: ...

class MarketOrderPair(_message.Message):
    __slots__ = ("sell_token_id", "buy_token_id")
    SELL_TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    BUY_TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    sell_token_id: bytes
    buy_token_id: bytes
    def __init__(self, sell_token_id: _Optional[bytes] = ..., buy_token_id: _Optional[bytes] = ...) -> None: ...

class MarketAccountOrder(_message.Message):
    __slots__ = ("owner_address", "orders", "count", "total_count")
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ORDERS_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    orders: _containers.RepeatedScalarFieldContainer[bytes]
    count: int
    total_count: int
    def __init__(self, owner_address: _Optional[bytes] = ..., orders: _Optional[_Iterable[bytes]] = ..., count: _Optional[int] = ..., total_count: _Optional[int] = ...) -> None: ...

class MarketPrice(_message.Message):
    __slots__ = ("sell_token_quantity", "buy_token_quantity")
    SELL_TOKEN_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    BUY_TOKEN_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    sell_token_quantity: int
    buy_token_quantity: int
    def __init__(self, sell_token_quantity: _Optional[int] = ..., buy_token_quantity: _Optional[int] = ...) -> None: ...

class MarketPriceList(_message.Message):
    __slots__ = ("sell_token_id", "buy_token_id", "prices")
    SELL_TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    BUY_TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    PRICES_FIELD_NUMBER: _ClassVar[int]
    sell_token_id: bytes
    buy_token_id: bytes
    prices: _containers.RepeatedCompositeFieldContainer[MarketPrice]
    def __init__(self, sell_token_id: _Optional[bytes] = ..., buy_token_id: _Optional[bytes] = ..., prices: _Optional[_Iterable[_Union[MarketPrice, _Mapping]]] = ...) -> None: ...

class MarketOrderIdList(_message.Message):
    __slots__ = ("head", "tail")
    HEAD_FIELD_NUMBER: _ClassVar[int]
    TAIL_FIELD_NUMBER: _ClassVar[int]
    head: bytes
    tail: bytes
    def __init__(self, head: _Optional[bytes] = ..., tail: _Optional[bytes] = ...) -> None: ...

class ChainParameters(_message.Message):
    __slots__ = ("chainParameter",)
    class ChainParameter(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    CHAINPARAMETER_FIELD_NUMBER: _ClassVar[int]
    chainParameter: _containers.RepeatedCompositeFieldContainer[ChainParameters.ChainParameter]
    def __init__(self, chainParameter: _Optional[_Iterable[_Union[ChainParameters.ChainParameter, _Mapping]]] = ...) -> None: ...

class Account(_message.Message):
    __slots__ = ("account_name", "type", "address", "balance", "votes", "asset", "assetV2", "frozen", "net_usage", "acquired_delegated_frozen_balance_for_bandwidth", "delegated_frozen_balance_for_bandwidth", "old_tron_power", "tron_power", "asset_optimized", "create_time", "latest_opration_time", "allowance", "latest_withdraw_time", "code", "is_witness", "is_committee", "frozen_supply", "asset_issued_name", "asset_issued_ID", "latest_asset_operation_time", "latest_asset_operation_timeV2", "free_net_usage", "free_asset_net_usage", "free_asset_net_usageV2", "latest_consume_time", "latest_consume_free_time", "account_id", "net_window_size", "net_window_optimized", "account_resource", "codeHash", "owner_permission", "witness_permission", "active_permission", "frozenV2", "unfrozenV2", "delegated_frozenV2_balance_for_bandwidth", "acquired_delegated_frozenV2_balance_for_bandwidth")
    class Frozen(_message.Message):
        __slots__ = ("frozen_balance", "expire_time")
        FROZEN_BALANCE_FIELD_NUMBER: _ClassVar[int]
        EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
        frozen_balance: int
        expire_time: int
        def __init__(self, frozen_balance: _Optional[int] = ..., expire_time: _Optional[int] = ...) -> None: ...
    class AssetEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class AssetV2Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class LatestAssetOperationTimeEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class LatestAssetOperationTimeV2Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class FreeAssetNetUsageEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class FreeAssetNetUsageV2Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class AccountResource(_message.Message):
        __slots__ = ("energy_usage", "frozen_balance_for_energy", "latest_consume_time_for_energy", "acquired_delegated_frozen_balance_for_energy", "delegated_frozen_balance_for_energy", "storage_limit", "storage_usage", "latest_exchange_storage_time", "energy_window_size", "delegated_frozenV2_balance_for_energy", "acquired_delegated_frozenV2_balance_for_energy", "energy_window_optimized")
        ENERGY_USAGE_FIELD_NUMBER: _ClassVar[int]
        FROZEN_BALANCE_FOR_ENERGY_FIELD_NUMBER: _ClassVar[int]
        LATEST_CONSUME_TIME_FOR_ENERGY_FIELD_NUMBER: _ClassVar[int]
        ACQUIRED_DELEGATED_FROZEN_BALANCE_FOR_ENERGY_FIELD_NUMBER: _ClassVar[int]
        DELEGATED_FROZEN_BALANCE_FOR_ENERGY_FIELD_NUMBER: _ClassVar[int]
        STORAGE_LIMIT_FIELD_NUMBER: _ClassVar[int]
        STORAGE_USAGE_FIELD_NUMBER: _ClassVar[int]
        LATEST_EXCHANGE_STORAGE_TIME_FIELD_NUMBER: _ClassVar[int]
        ENERGY_WINDOW_SIZE_FIELD_NUMBER: _ClassVar[int]
        DELEGATED_FROZENV2_BALANCE_FOR_ENERGY_FIELD_NUMBER: _ClassVar[int]
        ACQUIRED_DELEGATED_FROZENV2_BALANCE_FOR_ENERGY_FIELD_NUMBER: _ClassVar[int]
        ENERGY_WINDOW_OPTIMIZED_FIELD_NUMBER: _ClassVar[int]
        energy_usage: int
        frozen_balance_for_energy: Account.Frozen
        latest_consume_time_for_energy: int
        acquired_delegated_frozen_balance_for_energy: int
        delegated_frozen_balance_for_energy: int
        storage_limit: int
        storage_usage: int
        latest_exchange_storage_time: int
        energy_window_size: int
        delegated_frozenV2_balance_for_energy: int
        acquired_delegated_frozenV2_balance_for_energy: int
        energy_window_optimized: bool
        def __init__(self, energy_usage: _Optional[int] = ..., frozen_balance_for_energy: _Optional[_Union[Account.Frozen, _Mapping]] = ..., latest_consume_time_for_energy: _Optional[int] = ..., acquired_delegated_frozen_balance_for_energy: _Optional[int] = ..., delegated_frozen_balance_for_energy: _Optional[int] = ..., storage_limit: _Optional[int] = ..., storage_usage: _Optional[int] = ..., latest_exchange_storage_time: _Optional[int] = ..., energy_window_size: _Optional[int] = ..., delegated_frozenV2_balance_for_energy: _Optional[int] = ..., acquired_delegated_frozenV2_balance_for_energy: _Optional[int] = ..., energy_window_optimized: bool = ...) -> None: ...
    class FreezeV2(_message.Message):
        __slots__ = ("type", "amount")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        AMOUNT_FIELD_NUMBER: _ClassVar[int]
        type: _common_pb2.ResourceCode
        amount: int
        def __init__(self, type: _Optional[_Union[_common_pb2.ResourceCode, str]] = ..., amount: _Optional[int] = ...) -> None: ...
    class UnFreezeV2(_message.Message):
        __slots__ = ("type", "unfreeze_amount", "unfreeze_expire_time")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        UNFREEZE_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        UNFREEZE_EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
        type: _common_pb2.ResourceCode
        unfreeze_amount: int
        unfreeze_expire_time: int
        def __init__(self, type: _Optional[_Union[_common_pb2.ResourceCode, str]] = ..., unfreeze_amount: _Optional[int] = ..., unfreeze_expire_time: _Optional[int] = ...) -> None: ...
    ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    VOTES_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    ASSETV2_FIELD_NUMBER: _ClassVar[int]
    FROZEN_FIELD_NUMBER: _ClassVar[int]
    NET_USAGE_FIELD_NUMBER: _ClassVar[int]
    ACQUIRED_DELEGATED_FROZEN_BALANCE_FOR_BANDWIDTH_FIELD_NUMBER: _ClassVar[int]
    DELEGATED_FROZEN_BALANCE_FOR_BANDWIDTH_FIELD_NUMBER: _ClassVar[int]
    OLD_TRON_POWER_FIELD_NUMBER: _ClassVar[int]
    TRON_POWER_FIELD_NUMBER: _ClassVar[int]
    ASSET_OPTIMIZED_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LATEST_OPRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    ALLOWANCE_FIELD_NUMBER: _ClassVar[int]
    LATEST_WITHDRAW_TIME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    IS_WITNESS_FIELD_NUMBER: _ClassVar[int]
    IS_COMMITTEE_FIELD_NUMBER: _ClassVar[int]
    FROZEN_SUPPLY_FIELD_NUMBER: _ClassVar[int]
    ASSET_ISSUED_NAME_FIELD_NUMBER: _ClassVar[int]
    ASSET_ISSUED_ID_FIELD_NUMBER: _ClassVar[int]
    LATEST_ASSET_OPERATION_TIME_FIELD_NUMBER: _ClassVar[int]
    LATEST_ASSET_OPERATION_TIMEV2_FIELD_NUMBER: _ClassVar[int]
    FREE_NET_USAGE_FIELD_NUMBER: _ClassVar[int]
    FREE_ASSET_NET_USAGE_FIELD_NUMBER: _ClassVar[int]
    FREE_ASSET_NET_USAGEV2_FIELD_NUMBER: _ClassVar[int]
    LATEST_CONSUME_TIME_FIELD_NUMBER: _ClassVar[int]
    LATEST_CONSUME_FREE_TIME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    NET_WINDOW_SIZE_FIELD_NUMBER: _ClassVar[int]
    NET_WINDOW_OPTIMIZED_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    CODEHASH_FIELD_NUMBER: _ClassVar[int]
    OWNER_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    WITNESS_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    FROZENV2_FIELD_NUMBER: _ClassVar[int]
    UNFROZENV2_FIELD_NUMBER: _ClassVar[int]
    DELEGATED_FROZENV2_BALANCE_FOR_BANDWIDTH_FIELD_NUMBER: _ClassVar[int]
    ACQUIRED_DELEGATED_FROZENV2_BALANCE_FOR_BANDWIDTH_FIELD_NUMBER: _ClassVar[int]
    account_name: bytes
    type: AccountType
    address: bytes
    balance: int
    votes: _containers.RepeatedCompositeFieldContainer[Vote]
    asset: _containers.ScalarMap[str, int]
    assetV2: _containers.ScalarMap[str, int]
    frozen: _containers.RepeatedCompositeFieldContainer[Account.Frozen]
    net_usage: int
    acquired_delegated_frozen_balance_for_bandwidth: int
    delegated_frozen_balance_for_bandwidth: int
    old_tron_power: int
    tron_power: Account.Frozen
    asset_optimized: bool
    create_time: int
    latest_opration_time: int
    allowance: int
    latest_withdraw_time: int
    code: bytes
    is_witness: bool
    is_committee: bool
    frozen_supply: _containers.RepeatedCompositeFieldContainer[Account.Frozen]
    asset_issued_name: bytes
    asset_issued_ID: bytes
    latest_asset_operation_time: _containers.ScalarMap[str, int]
    latest_asset_operation_timeV2: _containers.ScalarMap[str, int]
    free_net_usage: int
    free_asset_net_usage: _containers.ScalarMap[str, int]
    free_asset_net_usageV2: _containers.ScalarMap[str, int]
    latest_consume_time: int
    latest_consume_free_time: int
    account_id: bytes
    net_window_size: int
    net_window_optimized: bool
    account_resource: Account.AccountResource
    codeHash: bytes
    owner_permission: Permission
    witness_permission: Permission
    active_permission: _containers.RepeatedCompositeFieldContainer[Permission]
    frozenV2: _containers.RepeatedCompositeFieldContainer[Account.FreezeV2]
    unfrozenV2: _containers.RepeatedCompositeFieldContainer[Account.UnFreezeV2]
    delegated_frozenV2_balance_for_bandwidth: int
    acquired_delegated_frozenV2_balance_for_bandwidth: int
    def __init__(self, account_name: _Optional[bytes] = ..., type: _Optional[_Union[AccountType, str]] = ..., address: _Optional[bytes] = ..., balance: _Optional[int] = ..., votes: _Optional[_Iterable[_Union[Vote, _Mapping]]] = ..., asset: _Optional[_Mapping[str, int]] = ..., assetV2: _Optional[_Mapping[str, int]] = ..., frozen: _Optional[_Iterable[_Union[Account.Frozen, _Mapping]]] = ..., net_usage: _Optional[int] = ..., acquired_delegated_frozen_balance_for_bandwidth: _Optional[int] = ..., delegated_frozen_balance_for_bandwidth: _Optional[int] = ..., old_tron_power: _Optional[int] = ..., tron_power: _Optional[_Union[Account.Frozen, _Mapping]] = ..., asset_optimized: bool = ..., create_time: _Optional[int] = ..., latest_opration_time: _Optional[int] = ..., allowance: _Optional[int] = ..., latest_withdraw_time: _Optional[int] = ..., code: _Optional[bytes] = ..., is_witness: bool = ..., is_committee: bool = ..., frozen_supply: _Optional[_Iterable[_Union[Account.Frozen, _Mapping]]] = ..., asset_issued_name: _Optional[bytes] = ..., asset_issued_ID: _Optional[bytes] = ..., latest_asset_operation_time: _Optional[_Mapping[str, int]] = ..., latest_asset_operation_timeV2: _Optional[_Mapping[str, int]] = ..., free_net_usage: _Optional[int] = ..., free_asset_net_usage: _Optional[_Mapping[str, int]] = ..., free_asset_net_usageV2: _Optional[_Mapping[str, int]] = ..., latest_consume_time: _Optional[int] = ..., latest_consume_free_time: _Optional[int] = ..., account_id: _Optional[bytes] = ..., net_window_size: _Optional[int] = ..., net_window_optimized: bool = ..., account_resource: _Optional[_Union[Account.AccountResource, _Mapping]] = ..., codeHash: _Optional[bytes] = ..., owner_permission: _Optional[_Union[Permission, _Mapping]] = ..., witness_permission: _Optional[_Union[Permission, _Mapping]] = ..., active_permission: _Optional[_Iterable[_Union[Permission, _Mapping]]] = ..., frozenV2: _Optional[_Iterable[_Union[Account.FreezeV2, _Mapping]]] = ..., unfrozenV2: _Optional[_Iterable[_Union[Account.UnFreezeV2, _Mapping]]] = ..., delegated_frozenV2_balance_for_bandwidth: _Optional[int] = ..., acquired_delegated_frozenV2_balance_for_bandwidth: _Optional[int] = ...) -> None: ...

class Key(_message.Message):
    __slots__ = ("address", "weight")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    address: bytes
    weight: int
    def __init__(self, address: _Optional[bytes] = ..., weight: _Optional[int] = ...) -> None: ...

class DelegatedResource(_message.Message):
    __slots__ = ("to", "frozen_balance_for_bandwidth", "frozen_balance_for_energy", "expire_time_for_bandwidth", "expire_time_for_energy")
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    FROZEN_BALANCE_FOR_BANDWIDTH_FIELD_NUMBER: _ClassVar[int]
    FROZEN_BALANCE_FOR_ENERGY_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FOR_BANDWIDTH_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FOR_ENERGY_FIELD_NUMBER: _ClassVar[int]
    to: bytes
    frozen_balance_for_bandwidth: int
    frozen_balance_for_energy: int
    expire_time_for_bandwidth: int
    expire_time_for_energy: int
    def __init__(self, to: _Optional[bytes] = ..., frozen_balance_for_bandwidth: _Optional[int] = ..., frozen_balance_for_energy: _Optional[int] = ..., expire_time_for_bandwidth: _Optional[int] = ..., expire_time_for_energy: _Optional[int] = ..., **kwargs) -> None: ...

class authority(_message.Message):
    __slots__ = ("account", "permission_name")
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_NAME_FIELD_NUMBER: _ClassVar[int]
    account: AccountId
    permission_name: bytes
    def __init__(self, account: _Optional[_Union[AccountId, _Mapping]] = ..., permission_name: _Optional[bytes] = ...) -> None: ...

class Permission(_message.Message):
    __slots__ = ("type", "id", "permission_name", "threshold", "parent_id", "operations", "keys")
    class PermissionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Owner: _ClassVar[Permission.PermissionType]
        Witness: _ClassVar[Permission.PermissionType]
        Active: _ClassVar[Permission.PermissionType]
    Owner: Permission.PermissionType
    Witness: Permission.PermissionType
    Active: Permission.PermissionType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_NAME_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    type: Permission.PermissionType
    id: int
    permission_name: str
    threshold: int
    parent_id: int
    operations: bytes
    keys: _containers.RepeatedCompositeFieldContainer[Key]
    def __init__(self, type: _Optional[_Union[Permission.PermissionType, str]] = ..., id: _Optional[int] = ..., permission_name: _Optional[str] = ..., threshold: _Optional[int] = ..., parent_id: _Optional[int] = ..., operations: _Optional[bytes] = ..., keys: _Optional[_Iterable[_Union[Key, _Mapping]]] = ...) -> None: ...

class Witness(_message.Message):
    __slots__ = ("address", "voteCount", "pubKey", "url", "totalProduced", "totalMissed", "latestBlockNum", "latestSlotNum", "isJobs")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VOTECOUNT_FIELD_NUMBER: _ClassVar[int]
    PUBKEY_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    TOTALPRODUCED_FIELD_NUMBER: _ClassVar[int]
    TOTALMISSED_FIELD_NUMBER: _ClassVar[int]
    LATESTBLOCKNUM_FIELD_NUMBER: _ClassVar[int]
    LATESTSLOTNUM_FIELD_NUMBER: _ClassVar[int]
    ISJOBS_FIELD_NUMBER: _ClassVar[int]
    address: bytes
    voteCount: int
    pubKey: bytes
    url: str
    totalProduced: int
    totalMissed: int
    latestBlockNum: int
    latestSlotNum: int
    isJobs: bool
    def __init__(self, address: _Optional[bytes] = ..., voteCount: _Optional[int] = ..., pubKey: _Optional[bytes] = ..., url: _Optional[str] = ..., totalProduced: _Optional[int] = ..., totalMissed: _Optional[int] = ..., latestBlockNum: _Optional[int] = ..., latestSlotNum: _Optional[int] = ..., isJobs: bool = ...) -> None: ...

class Votes(_message.Message):
    __slots__ = ("address", "old_votes", "new_votes")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    OLD_VOTES_FIELD_NUMBER: _ClassVar[int]
    NEW_VOTES_FIELD_NUMBER: _ClassVar[int]
    address: bytes
    old_votes: _containers.RepeatedCompositeFieldContainer[Vote]
    new_votes: _containers.RepeatedCompositeFieldContainer[Vote]
    def __init__(self, address: _Optional[bytes] = ..., old_votes: _Optional[_Iterable[_Union[Vote, _Mapping]]] = ..., new_votes: _Optional[_Iterable[_Union[Vote, _Mapping]]] = ...) -> None: ...

class TXOutput(_message.Message):
    __slots__ = ("value", "pubKeyHash")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    PUBKEYHASH_FIELD_NUMBER: _ClassVar[int]
    value: int
    pubKeyHash: bytes
    def __init__(self, value: _Optional[int] = ..., pubKeyHash: _Optional[bytes] = ...) -> None: ...

class TXInput(_message.Message):
    __slots__ = ("raw_data", "signature")
    class raw(_message.Message):
        __slots__ = ("txID", "vout", "pubKey")
        TXID_FIELD_NUMBER: _ClassVar[int]
        VOUT_FIELD_NUMBER: _ClassVar[int]
        PUBKEY_FIELD_NUMBER: _ClassVar[int]
        txID: bytes
        vout: int
        pubKey: bytes
        def __init__(self, txID: _Optional[bytes] = ..., vout: _Optional[int] = ..., pubKey: _Optional[bytes] = ...) -> None: ...
    RAW_DATA_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    raw_data: TXInput.raw
    signature: bytes
    def __init__(self, raw_data: _Optional[_Union[TXInput.raw, _Mapping]] = ..., signature: _Optional[bytes] = ...) -> None: ...

class TXOutputs(_message.Message):
    __slots__ = ("outputs",)
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    outputs: _containers.RepeatedCompositeFieldContainer[TXOutput]
    def __init__(self, outputs: _Optional[_Iterable[_Union[TXOutput, _Mapping]]] = ...) -> None: ...

class ResourceReceipt(_message.Message):
    __slots__ = ("energy_usage", "energy_fee", "origin_energy_usage", "energy_usage_total", "net_usage", "net_fee", "result", "energy_penalty_total")
    ENERGY_USAGE_FIELD_NUMBER: _ClassVar[int]
    ENERGY_FEE_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_ENERGY_USAGE_FIELD_NUMBER: _ClassVar[int]
    ENERGY_USAGE_TOTAL_FIELD_NUMBER: _ClassVar[int]
    NET_USAGE_FIELD_NUMBER: _ClassVar[int]
    NET_FEE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ENERGY_PENALTY_TOTAL_FIELD_NUMBER: _ClassVar[int]
    energy_usage: int
    energy_fee: int
    origin_energy_usage: int
    energy_usage_total: int
    net_usage: int
    net_fee: int
    result: Transaction.Result.contractResult
    energy_penalty_total: int
    def __init__(self, energy_usage: _Optional[int] = ..., energy_fee: _Optional[int] = ..., origin_energy_usage: _Optional[int] = ..., energy_usage_total: _Optional[int] = ..., net_usage: _Optional[int] = ..., net_fee: _Optional[int] = ..., result: _Optional[_Union[Transaction.Result.contractResult, str]] = ..., energy_penalty_total: _Optional[int] = ...) -> None: ...

class MarketOrderDetail(_message.Message):
    __slots__ = ("makerOrderId", "takerOrderId", "fillSellQuantity", "fillBuyQuantity")
    MAKERORDERID_FIELD_NUMBER: _ClassVar[int]
    TAKERORDERID_FIELD_NUMBER: _ClassVar[int]
    FILLSELLQUANTITY_FIELD_NUMBER: _ClassVar[int]
    FILLBUYQUANTITY_FIELD_NUMBER: _ClassVar[int]
    makerOrderId: bytes
    takerOrderId: bytes
    fillSellQuantity: int
    fillBuyQuantity: int
    def __init__(self, makerOrderId: _Optional[bytes] = ..., takerOrderId: _Optional[bytes] = ..., fillSellQuantity: _Optional[int] = ..., fillBuyQuantity: _Optional[int] = ...) -> None: ...

class Transaction(_message.Message):
    __slots__ = ("raw_data", "signature", "ret")
    class Contract(_message.Message):
        __slots__ = ("type", "parameter", "provider", "ContractName", "Permission_id")
        class ContractType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            AccountCreateContract: _ClassVar[Transaction.Contract.ContractType]
            TransferContract: _ClassVar[Transaction.Contract.ContractType]
            TransferAssetContract: _ClassVar[Transaction.Contract.ContractType]
            VoteAssetContract: _ClassVar[Transaction.Contract.ContractType]
            VoteWitnessContract: _ClassVar[Transaction.Contract.ContractType]
            WitnessCreateContract: _ClassVar[Transaction.Contract.ContractType]
            AssetIssueContract: _ClassVar[Transaction.Contract.ContractType]
            WitnessUpdateContract: _ClassVar[Transaction.Contract.ContractType]
            ParticipateAssetIssueContract: _ClassVar[Transaction.Contract.ContractType]
            AccountUpdateContract: _ClassVar[Transaction.Contract.ContractType]
            FreezeBalanceContract: _ClassVar[Transaction.Contract.ContractType]
            UnfreezeBalanceContract: _ClassVar[Transaction.Contract.ContractType]
            WithdrawBalanceContract: _ClassVar[Transaction.Contract.ContractType]
            UnfreezeAssetContract: _ClassVar[Transaction.Contract.ContractType]
            UpdateAssetContract: _ClassVar[Transaction.Contract.ContractType]
            ProposalCreateContract: _ClassVar[Transaction.Contract.ContractType]
            ProposalApproveContract: _ClassVar[Transaction.Contract.ContractType]
            ProposalDeleteContract: _ClassVar[Transaction.Contract.ContractType]
            SetAccountIdContract: _ClassVar[Transaction.Contract.ContractType]
            CustomContract: _ClassVar[Transaction.Contract.ContractType]
            CreateSmartContract: _ClassVar[Transaction.Contract.ContractType]
            TriggerSmartContract: _ClassVar[Transaction.Contract.ContractType]
            GetContract: _ClassVar[Transaction.Contract.ContractType]
            UpdateSettingContract: _ClassVar[Transaction.Contract.ContractType]
            ExchangeCreateContract: _ClassVar[Transaction.Contract.ContractType]
            ExchangeInjectContract: _ClassVar[Transaction.Contract.ContractType]
            ExchangeWithdrawContract: _ClassVar[Transaction.Contract.ContractType]
            ExchangeTransactionContract: _ClassVar[Transaction.Contract.ContractType]
            UpdateEnergyLimitContract: _ClassVar[Transaction.Contract.ContractType]
            AccountPermissionUpdateContract: _ClassVar[Transaction.Contract.ContractType]
            ClearABIContract: _ClassVar[Transaction.Contract.ContractType]
            UpdateBrokerageContract: _ClassVar[Transaction.Contract.ContractType]
            ShieldedTransferContract: _ClassVar[Transaction.Contract.ContractType]
            MarketSellAssetContract: _ClassVar[Transaction.Contract.ContractType]
            MarketCancelOrderContract: _ClassVar[Transaction.Contract.ContractType]
            FreezeBalanceV2Contract: _ClassVar[Transaction.Contract.ContractType]
            UnfreezeBalanceV2Contract: _ClassVar[Transaction.Contract.ContractType]
            WithdrawExpireUnfreezeContract: _ClassVar[Transaction.Contract.ContractType]
            DelegateResourceContract: _ClassVar[Transaction.Contract.ContractType]
            UnDelegateResourceContract: _ClassVar[Transaction.Contract.ContractType]
            CancelAllUnfreezeV2Contract: _ClassVar[Transaction.Contract.ContractType]
        AccountCreateContract: Transaction.Contract.ContractType
        TransferContract: Transaction.Contract.ContractType
        TransferAssetContract: Transaction.Contract.ContractType
        VoteAssetContract: Transaction.Contract.ContractType
        VoteWitnessContract: Transaction.Contract.ContractType
        WitnessCreateContract: Transaction.Contract.ContractType
        AssetIssueContract: Transaction.Contract.ContractType
        WitnessUpdateContract: Transaction.Contract.ContractType
        ParticipateAssetIssueContract: Transaction.Contract.ContractType
        AccountUpdateContract: Transaction.Contract.ContractType
        FreezeBalanceContract: Transaction.Contract.ContractType
        UnfreezeBalanceContract: Transaction.Contract.ContractType
        WithdrawBalanceContract: Transaction.Contract.ContractType
        UnfreezeAssetContract: Transaction.Contract.ContractType
        UpdateAssetContract: Transaction.Contract.ContractType
        ProposalCreateContract: Transaction.Contract.ContractType
        ProposalApproveContract: Transaction.Contract.ContractType
        ProposalDeleteContract: Transaction.Contract.ContractType
        SetAccountIdContract: Transaction.Contract.ContractType
        CustomContract: Transaction.Contract.ContractType
        CreateSmartContract: Transaction.Contract.ContractType
        TriggerSmartContract: Transaction.Contract.ContractType
        GetContract: Transaction.Contract.ContractType
        UpdateSettingContract: Transaction.Contract.ContractType
        ExchangeCreateContract: Transaction.Contract.ContractType
        ExchangeInjectContract: Transaction.Contract.ContractType
        ExchangeWithdrawContract: Transaction.Contract.ContractType
        ExchangeTransactionContract: Transaction.Contract.ContractType
        UpdateEnergyLimitContract: Transaction.Contract.ContractType
        AccountPermissionUpdateContract: Transaction.Contract.ContractType
        ClearABIContract: Transaction.Contract.ContractType
        UpdateBrokerageContract: Transaction.Contract.ContractType
        ShieldedTransferContract: Transaction.Contract.ContractType
        MarketSellAssetContract: Transaction.Contract.ContractType
        MarketCancelOrderContract: Transaction.Contract.ContractType
        FreezeBalanceV2Contract: Transaction.Contract.ContractType
        UnfreezeBalanceV2Contract: Transaction.Contract.ContractType
        WithdrawExpireUnfreezeContract: Transaction.Contract.ContractType
        DelegateResourceContract: Transaction.Contract.ContractType
        UnDelegateResourceContract: Transaction.Contract.ContractType
        CancelAllUnfreezeV2Contract: Transaction.Contract.ContractType
        TYPE_FIELD_NUMBER: _ClassVar[int]
        PARAMETER_FIELD_NUMBER: _ClassVar[int]
        PROVIDER_FIELD_NUMBER: _ClassVar[int]
        CONTRACTNAME_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_ID_FIELD_NUMBER: _ClassVar[int]
        type: Transaction.Contract.ContractType
        parameter: _any_pb2.Any
        provider: bytes
        ContractName: bytes
        Permission_id: int
        def __init__(self, type: _Optional[_Union[Transaction.Contract.ContractType, str]] = ..., parameter: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., provider: _Optional[bytes] = ..., ContractName: _Optional[bytes] = ..., Permission_id: _Optional[int] = ...) -> None: ...
    class Result(_message.Message):
        __slots__ = ("fee", "ret", "contractRet", "assetIssueID", "withdraw_amount", "unfreeze_amount", "exchange_received_amount", "exchange_inject_another_amount", "exchange_withdraw_another_amount", "exchange_id", "shielded_transaction_fee", "orderId", "orderDetails", "withdraw_expire_amount", "cancel_unfreezeV2_amount")
        class code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SUCESS: _ClassVar[Transaction.Result.code]
            FAILED: _ClassVar[Transaction.Result.code]
        SUCESS: Transaction.Result.code
        FAILED: Transaction.Result.code
        class contractResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            DEFAULT: _ClassVar[Transaction.Result.contractResult]
            SUCCESS: _ClassVar[Transaction.Result.contractResult]
            REVERT: _ClassVar[Transaction.Result.contractResult]
            BAD_JUMP_DESTINATION: _ClassVar[Transaction.Result.contractResult]
            OUT_OF_MEMORY: _ClassVar[Transaction.Result.contractResult]
            PRECOMPILED_CONTRACT: _ClassVar[Transaction.Result.contractResult]
            STACK_TOO_SMALL: _ClassVar[Transaction.Result.contractResult]
            STACK_TOO_LARGE: _ClassVar[Transaction.Result.contractResult]
            ILLEGAL_OPERATION: _ClassVar[Transaction.Result.contractResult]
            STACK_OVERFLOW: _ClassVar[Transaction.Result.contractResult]
            OUT_OF_ENERGY: _ClassVar[Transaction.Result.contractResult]
            OUT_OF_TIME: _ClassVar[Transaction.Result.contractResult]
            JVM_STACK_OVER_FLOW: _ClassVar[Transaction.Result.contractResult]
            UNKNOWN: _ClassVar[Transaction.Result.contractResult]
            TRANSFER_FAILED: _ClassVar[Transaction.Result.contractResult]
            INVALID_CODE: _ClassVar[Transaction.Result.contractResult]
        DEFAULT: Transaction.Result.contractResult
        SUCCESS: Transaction.Result.contractResult
        REVERT: Transaction.Result.contractResult
        BAD_JUMP_DESTINATION: Transaction.Result.contractResult
        OUT_OF_MEMORY: Transaction.Result.contractResult
        PRECOMPILED_CONTRACT: Transaction.Result.contractResult
        STACK_TOO_SMALL: Transaction.Result.contractResult
        STACK_TOO_LARGE: Transaction.Result.contractResult
        ILLEGAL_OPERATION: Transaction.Result.contractResult
        STACK_OVERFLOW: Transaction.Result.contractResult
        OUT_OF_ENERGY: Transaction.Result.contractResult
        OUT_OF_TIME: Transaction.Result.contractResult
        JVM_STACK_OVER_FLOW: Transaction.Result.contractResult
        UNKNOWN: Transaction.Result.contractResult
        TRANSFER_FAILED: Transaction.Result.contractResult
        INVALID_CODE: Transaction.Result.contractResult
        class CancelUnfreezeV2AmountEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: int
            def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
        FEE_FIELD_NUMBER: _ClassVar[int]
        RET_FIELD_NUMBER: _ClassVar[int]
        CONTRACTRET_FIELD_NUMBER: _ClassVar[int]
        ASSETISSUEID_FIELD_NUMBER: _ClassVar[int]
        WITHDRAW_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        UNFREEZE_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        EXCHANGE_RECEIVED_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        EXCHANGE_INJECT_ANOTHER_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        EXCHANGE_WITHDRAW_ANOTHER_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        EXCHANGE_ID_FIELD_NUMBER: _ClassVar[int]
        SHIELDED_TRANSACTION_FEE_FIELD_NUMBER: _ClassVar[int]
        ORDERID_FIELD_NUMBER: _ClassVar[int]
        ORDERDETAILS_FIELD_NUMBER: _ClassVar[int]
        WITHDRAW_EXPIRE_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        CANCEL_UNFREEZEV2_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        fee: int
        ret: Transaction.Result.code
        contractRet: Transaction.Result.contractResult
        assetIssueID: str
        withdraw_amount: int
        unfreeze_amount: int
        exchange_received_amount: int
        exchange_inject_another_amount: int
        exchange_withdraw_another_amount: int
        exchange_id: int
        shielded_transaction_fee: int
        orderId: bytes
        orderDetails: _containers.RepeatedCompositeFieldContainer[MarketOrderDetail]
        withdraw_expire_amount: int
        cancel_unfreezeV2_amount: _containers.ScalarMap[str, int]
        def __init__(self, fee: _Optional[int] = ..., ret: _Optional[_Union[Transaction.Result.code, str]] = ..., contractRet: _Optional[_Union[Transaction.Result.contractResult, str]] = ..., assetIssueID: _Optional[str] = ..., withdraw_amount: _Optional[int] = ..., unfreeze_amount: _Optional[int] = ..., exchange_received_amount: _Optional[int] = ..., exchange_inject_another_amount: _Optional[int] = ..., exchange_withdraw_another_amount: _Optional[int] = ..., exchange_id: _Optional[int] = ..., shielded_transaction_fee: _Optional[int] = ..., orderId: _Optional[bytes] = ..., orderDetails: _Optional[_Iterable[_Union[MarketOrderDetail, _Mapping]]] = ..., withdraw_expire_amount: _Optional[int] = ..., cancel_unfreezeV2_amount: _Optional[_Mapping[str, int]] = ...) -> None: ...
    class raw(_message.Message):
        __slots__ = ("ref_block_bytes", "ref_block_num", "ref_block_hash", "expiration", "auths", "data", "contract", "scripts", "timestamp", "fee_limit")
        REF_BLOCK_BYTES_FIELD_NUMBER: _ClassVar[int]
        REF_BLOCK_NUM_FIELD_NUMBER: _ClassVar[int]
        REF_BLOCK_HASH_FIELD_NUMBER: _ClassVar[int]
        EXPIRATION_FIELD_NUMBER: _ClassVar[int]
        AUTHS_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        CONTRACT_FIELD_NUMBER: _ClassVar[int]
        SCRIPTS_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        FEE_LIMIT_FIELD_NUMBER: _ClassVar[int]
        ref_block_bytes: bytes
        ref_block_num: int
        ref_block_hash: bytes
        expiration: int
        auths: _containers.RepeatedCompositeFieldContainer[authority]
        data: bytes
        contract: _containers.RepeatedCompositeFieldContainer[Transaction.Contract]
        scripts: bytes
        timestamp: int
        fee_limit: int
        def __init__(self, ref_block_bytes: _Optional[bytes] = ..., ref_block_num: _Optional[int] = ..., ref_block_hash: _Optional[bytes] = ..., expiration: _Optional[int] = ..., auths: _Optional[_Iterable[_Union[authority, _Mapping]]] = ..., data: _Optional[bytes] = ..., contract: _Optional[_Iterable[_Union[Transaction.Contract, _Mapping]]] = ..., scripts: _Optional[bytes] = ..., timestamp: _Optional[int] = ..., fee_limit: _Optional[int] = ...) -> None: ...
    RAW_DATA_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    RET_FIELD_NUMBER: _ClassVar[int]
    raw_data: Transaction.raw
    signature: _containers.RepeatedScalarFieldContainer[bytes]
    ret: _containers.RepeatedCompositeFieldContainer[Transaction.Result]
    def __init__(self, raw_data: _Optional[_Union[Transaction.raw, _Mapping]] = ..., signature: _Optional[_Iterable[bytes]] = ..., ret: _Optional[_Iterable[_Union[Transaction.Result, _Mapping]]] = ...) -> None: ...

class TransactionInfo(_message.Message):
    __slots__ = ("id", "fee", "blockNumber", "blockTimeStamp", "contractResult", "contract_address", "receipt", "log", "result", "resMessage", "assetIssueID", "withdraw_amount", "unfreeze_amount", "internal_transactions", "exchange_received_amount", "exchange_inject_another_amount", "exchange_withdraw_another_amount", "exchange_id", "shielded_transaction_fee", "orderId", "orderDetails", "packingFee", "withdraw_expire_amount", "cancel_unfreezeV2_amount")
    class code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCESS: _ClassVar[TransactionInfo.code]
        FAILED: _ClassVar[TransactionInfo.code]
    SUCESS: TransactionInfo.code
    FAILED: TransactionInfo.code
    class Log(_message.Message):
        __slots__ = ("address", "topics", "data")
        ADDRESS_FIELD_NUMBER: _ClassVar[int]
        TOPICS_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        address: bytes
        topics: _containers.RepeatedScalarFieldContainer[bytes]
        data: bytes
        def __init__(self, address: _Optional[bytes] = ..., topics: _Optional[_Iterable[bytes]] = ..., data: _Optional[bytes] = ...) -> None: ...
    class CancelUnfreezeV2AmountEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    FEE_FIELD_NUMBER: _ClassVar[int]
    BLOCKNUMBER_FIELD_NUMBER: _ClassVar[int]
    BLOCKTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CONTRACTRESULT_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    RECEIPT_FIELD_NUMBER: _ClassVar[int]
    LOG_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    RESMESSAGE_FIELD_NUMBER: _ClassVar[int]
    ASSETISSUEID_FIELD_NUMBER: _ClassVar[int]
    WITHDRAW_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    UNFREEZE_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_RECEIVED_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_INJECT_ANOTHER_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_WITHDRAW_ANOTHER_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_ID_FIELD_NUMBER: _ClassVar[int]
    SHIELDED_TRANSACTION_FEE_FIELD_NUMBER: _ClassVar[int]
    ORDERID_FIELD_NUMBER: _ClassVar[int]
    ORDERDETAILS_FIELD_NUMBER: _ClassVar[int]
    PACKINGFEE_FIELD_NUMBER: _ClassVar[int]
    WITHDRAW_EXPIRE_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    CANCEL_UNFREEZEV2_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    fee: int
    blockNumber: int
    blockTimeStamp: int
    contractResult: _containers.RepeatedScalarFieldContainer[bytes]
    contract_address: bytes
    receipt: ResourceReceipt
    log: _containers.RepeatedCompositeFieldContainer[TransactionInfo.Log]
    result: TransactionInfo.code
    resMessage: bytes
    assetIssueID: str
    withdraw_amount: int
    unfreeze_amount: int
    internal_transactions: _containers.RepeatedCompositeFieldContainer[InternalTransaction]
    exchange_received_amount: int
    exchange_inject_another_amount: int
    exchange_withdraw_another_amount: int
    exchange_id: int
    shielded_transaction_fee: int
    orderId: bytes
    orderDetails: _containers.RepeatedCompositeFieldContainer[MarketOrderDetail]
    packingFee: int
    withdraw_expire_amount: int
    cancel_unfreezeV2_amount: _containers.ScalarMap[str, int]
    def __init__(self, id: _Optional[bytes] = ..., fee: _Optional[int] = ..., blockNumber: _Optional[int] = ..., blockTimeStamp: _Optional[int] = ..., contractResult: _Optional[_Iterable[bytes]] = ..., contract_address: _Optional[bytes] = ..., receipt: _Optional[_Union[ResourceReceipt, _Mapping]] = ..., log: _Optional[_Iterable[_Union[TransactionInfo.Log, _Mapping]]] = ..., result: _Optional[_Union[TransactionInfo.code, str]] = ..., resMessage: _Optional[bytes] = ..., assetIssueID: _Optional[str] = ..., withdraw_amount: _Optional[int] = ..., unfreeze_amount: _Optional[int] = ..., internal_transactions: _Optional[_Iterable[_Union[InternalTransaction, _Mapping]]] = ..., exchange_received_amount: _Optional[int] = ..., exchange_inject_another_amount: _Optional[int] = ..., exchange_withdraw_another_amount: _Optional[int] = ..., exchange_id: _Optional[int] = ..., shielded_transaction_fee: _Optional[int] = ..., orderId: _Optional[bytes] = ..., orderDetails: _Optional[_Iterable[_Union[MarketOrderDetail, _Mapping]]] = ..., packingFee: _Optional[int] = ..., withdraw_expire_amount: _Optional[int] = ..., cancel_unfreezeV2_amount: _Optional[_Mapping[str, int]] = ...) -> None: ...

class TransactionRet(_message.Message):
    __slots__ = ("blockNumber", "blockTimeStamp", "transactioninfo")
    BLOCKNUMBER_FIELD_NUMBER: _ClassVar[int]
    BLOCKTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONINFO_FIELD_NUMBER: _ClassVar[int]
    blockNumber: int
    blockTimeStamp: int
    transactioninfo: _containers.RepeatedCompositeFieldContainer[TransactionInfo]
    def __init__(self, blockNumber: _Optional[int] = ..., blockTimeStamp: _Optional[int] = ..., transactioninfo: _Optional[_Iterable[_Union[TransactionInfo, _Mapping]]] = ...) -> None: ...

class Transactions(_message.Message):
    __slots__ = ("transactions",)
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    transactions: _containers.RepeatedCompositeFieldContainer[Transaction]
    def __init__(self, transactions: _Optional[_Iterable[_Union[Transaction, _Mapping]]] = ...) -> None: ...

class BlockHeader(_message.Message):
    __slots__ = ("raw_data", "witness_signature")
    class raw(_message.Message):
        __slots__ = ("timestamp", "txTrieRoot", "parentHash", "number", "witness_id", "witness_address", "version", "accountStateRoot")
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        TXTRIEROOT_FIELD_NUMBER: _ClassVar[int]
        PARENTHASH_FIELD_NUMBER: _ClassVar[int]
        NUMBER_FIELD_NUMBER: _ClassVar[int]
        WITNESS_ID_FIELD_NUMBER: _ClassVar[int]
        WITNESS_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        ACCOUNTSTATEROOT_FIELD_NUMBER: _ClassVar[int]
        timestamp: int
        txTrieRoot: bytes
        parentHash: bytes
        number: int
        witness_id: int
        witness_address: bytes
        version: int
        accountStateRoot: bytes
        def __init__(self, timestamp: _Optional[int] = ..., txTrieRoot: _Optional[bytes] = ..., parentHash: _Optional[bytes] = ..., number: _Optional[int] = ..., witness_id: _Optional[int] = ..., witness_address: _Optional[bytes] = ..., version: _Optional[int] = ..., accountStateRoot: _Optional[bytes] = ...) -> None: ...
    RAW_DATA_FIELD_NUMBER: _ClassVar[int]
    WITNESS_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    raw_data: BlockHeader.raw
    witness_signature: bytes
    def __init__(self, raw_data: _Optional[_Union[BlockHeader.raw, _Mapping]] = ..., witness_signature: _Optional[bytes] = ...) -> None: ...

class Block(_message.Message):
    __slots__ = ("transactions", "block_header")
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    BLOCK_HEADER_FIELD_NUMBER: _ClassVar[int]
    transactions: _containers.RepeatedCompositeFieldContainer[Transaction]
    block_header: BlockHeader
    def __init__(self, transactions: _Optional[_Iterable[_Union[Transaction, _Mapping]]] = ..., block_header: _Optional[_Union[BlockHeader, _Mapping]] = ...) -> None: ...

class ChainInventory(_message.Message):
    __slots__ = ("ids", "remain_num")
    class BlockId(_message.Message):
        __slots__ = ("hash", "number")
        HASH_FIELD_NUMBER: _ClassVar[int]
        NUMBER_FIELD_NUMBER: _ClassVar[int]
        hash: bytes
        number: int
        def __init__(self, hash: _Optional[bytes] = ..., number: _Optional[int] = ...) -> None: ...
    IDS_FIELD_NUMBER: _ClassVar[int]
    REMAIN_NUM_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedCompositeFieldContainer[ChainInventory.BlockId]
    remain_num: int
    def __init__(self, ids: _Optional[_Iterable[_Union[ChainInventory.BlockId, _Mapping]]] = ..., remain_num: _Optional[int] = ...) -> None: ...

class BlockInventory(_message.Message):
    __slots__ = ("ids", "type")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SYNC: _ClassVar[BlockInventory.Type]
        ADVTISE: _ClassVar[BlockInventory.Type]
        FETCH: _ClassVar[BlockInventory.Type]
    SYNC: BlockInventory.Type
    ADVTISE: BlockInventory.Type
    FETCH: BlockInventory.Type
    class BlockId(_message.Message):
        __slots__ = ("hash", "number")
        HASH_FIELD_NUMBER: _ClassVar[int]
        NUMBER_FIELD_NUMBER: _ClassVar[int]
        hash: bytes
        number: int
        def __init__(self, hash: _Optional[bytes] = ..., number: _Optional[int] = ...) -> None: ...
    IDS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedCompositeFieldContainer[BlockInventory.BlockId]
    type: BlockInventory.Type
    def __init__(self, ids: _Optional[_Iterable[_Union[BlockInventory.BlockId, _Mapping]]] = ..., type: _Optional[_Union[BlockInventory.Type, str]] = ...) -> None: ...

class Inventory(_message.Message):
    __slots__ = ("type", "ids")
    class InventoryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TRX: _ClassVar[Inventory.InventoryType]
        BLOCK: _ClassVar[Inventory.InventoryType]
    TRX: Inventory.InventoryType
    BLOCK: Inventory.InventoryType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    type: Inventory.InventoryType
    ids: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, type: _Optional[_Union[Inventory.InventoryType, str]] = ..., ids: _Optional[_Iterable[bytes]] = ...) -> None: ...

class Items(_message.Message):
    __slots__ = ("type", "blocks", "block_headers", "transactions")
    class ItemType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ERR: _ClassVar[Items.ItemType]
        TRX: _ClassVar[Items.ItemType]
        BLOCK: _ClassVar[Items.ItemType]
        BLOCKHEADER: _ClassVar[Items.ItemType]
    ERR: Items.ItemType
    TRX: Items.ItemType
    BLOCK: Items.ItemType
    BLOCKHEADER: Items.ItemType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    BLOCKS_FIELD_NUMBER: _ClassVar[int]
    BLOCK_HEADERS_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    type: Items.ItemType
    blocks: _containers.RepeatedCompositeFieldContainer[Block]
    block_headers: _containers.RepeatedCompositeFieldContainer[BlockHeader]
    transactions: _containers.RepeatedCompositeFieldContainer[Transaction]
    def __init__(self, type: _Optional[_Union[Items.ItemType, str]] = ..., blocks: _Optional[_Iterable[_Union[Block, _Mapping]]] = ..., block_headers: _Optional[_Iterable[_Union[BlockHeader, _Mapping]]] = ..., transactions: _Optional[_Iterable[_Union[Transaction, _Mapping]]] = ...) -> None: ...

class DynamicProperties(_message.Message):
    __slots__ = ("last_solidity_block_num",)
    LAST_SOLIDITY_BLOCK_NUM_FIELD_NUMBER: _ClassVar[int]
    last_solidity_block_num: int
    def __init__(self, last_solidity_block_num: _Optional[int] = ...) -> None: ...

class DisconnectMessage(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: ReasonCode
    def __init__(self, reason: _Optional[_Union[ReasonCode, str]] = ...) -> None: ...

class HelloMessage(_message.Message):
    __slots__ = ("version", "timestamp", "genesisBlockId", "solidBlockId", "headBlockId", "address", "signature", "nodeType", "lowestBlockNum")
    class BlockId(_message.Message):
        __slots__ = ("hash", "number")
        HASH_FIELD_NUMBER: _ClassVar[int]
        NUMBER_FIELD_NUMBER: _ClassVar[int]
        hash: bytes
        number: int
        def __init__(self, hash: _Optional[bytes] = ..., number: _Optional[int] = ...) -> None: ...
    FROM_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    GENESISBLOCKID_FIELD_NUMBER: _ClassVar[int]
    SOLIDBLOCKID_FIELD_NUMBER: _ClassVar[int]
    HEADBLOCKID_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    NODETYPE_FIELD_NUMBER: _ClassVar[int]
    LOWESTBLOCKNUM_FIELD_NUMBER: _ClassVar[int]
    version: int
    timestamp: int
    genesisBlockId: HelloMessage.BlockId
    solidBlockId: HelloMessage.BlockId
    headBlockId: HelloMessage.BlockId
    address: bytes
    signature: bytes
    nodeType: int
    lowestBlockNum: int
    def __init__(self, version: _Optional[int] = ..., timestamp: _Optional[int] = ..., genesisBlockId: _Optional[_Union[HelloMessage.BlockId, _Mapping]] = ..., solidBlockId: _Optional[_Union[HelloMessage.BlockId, _Mapping]] = ..., headBlockId: _Optional[_Union[HelloMessage.BlockId, _Mapping]] = ..., address: _Optional[bytes] = ..., signature: _Optional[bytes] = ..., nodeType: _Optional[int] = ..., lowestBlockNum: _Optional[int] = ..., **kwargs) -> None: ...

class InternalTransaction(_message.Message):
    __slots__ = ("hash", "caller_address", "transferTo_address", "callValueInfo", "note", "rejected", "extra")
    class CallValueInfo(_message.Message):
        __slots__ = ("callValue", "tokenId")
        CALLVALUE_FIELD_NUMBER: _ClassVar[int]
        TOKENID_FIELD_NUMBER: _ClassVar[int]
        callValue: int
        tokenId: str
        def __init__(self, callValue: _Optional[int] = ..., tokenId: _Optional[str] = ...) -> None: ...
    HASH_FIELD_NUMBER: _ClassVar[int]
    CALLER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TRANSFERTO_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CALLVALUEINFO_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    hash: bytes
    caller_address: bytes
    transferTo_address: bytes
    callValueInfo: _containers.RepeatedCompositeFieldContainer[InternalTransaction.CallValueInfo]
    note: bytes
    rejected: bool
    extra: str
    def __init__(self, hash: _Optional[bytes] = ..., caller_address: _Optional[bytes] = ..., transferTo_address: _Optional[bytes] = ..., callValueInfo: _Optional[_Iterable[_Union[InternalTransaction.CallValueInfo, _Mapping]]] = ..., note: _Optional[bytes] = ..., rejected: bool = ..., extra: _Optional[str] = ...) -> None: ...

class DelegatedResourceAccountIndex(_message.Message):
    __slots__ = ("account", "fromAccounts", "toAccounts", "timestamp")
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    FROMACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    TOACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    account: bytes
    fromAccounts: _containers.RepeatedScalarFieldContainer[bytes]
    toAccounts: _containers.RepeatedScalarFieldContainer[bytes]
    timestamp: int
    def __init__(self, account: _Optional[bytes] = ..., fromAccounts: _Optional[_Iterable[bytes]] = ..., toAccounts: _Optional[_Iterable[bytes]] = ..., timestamp: _Optional[int] = ...) -> None: ...

class NodeInfo(_message.Message):
    __slots__ = ("beginSyncNum", "block", "solidityBlock", "currentConnectCount", "activeConnectCount", "passiveConnectCount", "totalFlow", "peerInfoList", "configNodeInfo", "machineInfo", "cheatWitnessInfoMap")
    class CheatWitnessInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class PeerInfo(_message.Message):
        __slots__ = ("lastSyncBlock", "remainNum", "lastBlockUpdateTime", "syncFlag", "headBlockTimeWeBothHave", "needSyncFromPeer", "needSyncFromUs", "host", "port", "nodeId", "connectTime", "avgLatency", "syncToFetchSize", "syncToFetchSizePeekNum", "syncBlockRequestedSize", "unFetchSynNum", "blockInPorcSize", "headBlockWeBothHave", "isActive", "score", "nodeCount", "inFlow", "disconnectTimes", "localDisconnectReason", "remoteDisconnectReason")
        LASTSYNCBLOCK_FIELD_NUMBER: _ClassVar[int]
        REMAINNUM_FIELD_NUMBER: _ClassVar[int]
        LASTBLOCKUPDATETIME_FIELD_NUMBER: _ClassVar[int]
        SYNCFLAG_FIELD_NUMBER: _ClassVar[int]
        HEADBLOCKTIMEWEBOTHHAVE_FIELD_NUMBER: _ClassVar[int]
        NEEDSYNCFROMPEER_FIELD_NUMBER: _ClassVar[int]
        NEEDSYNCFROMUS_FIELD_NUMBER: _ClassVar[int]
        HOST_FIELD_NUMBER: _ClassVar[int]
        PORT_FIELD_NUMBER: _ClassVar[int]
        NODEID_FIELD_NUMBER: _ClassVar[int]
        CONNECTTIME_FIELD_NUMBER: _ClassVar[int]
        AVGLATENCY_FIELD_NUMBER: _ClassVar[int]
        SYNCTOFETCHSIZE_FIELD_NUMBER: _ClassVar[int]
        SYNCTOFETCHSIZEPEEKNUM_FIELD_NUMBER: _ClassVar[int]
        SYNCBLOCKREQUESTEDSIZE_FIELD_NUMBER: _ClassVar[int]
        UNFETCHSYNNUM_FIELD_NUMBER: _ClassVar[int]
        BLOCKINPORCSIZE_FIELD_NUMBER: _ClassVar[int]
        HEADBLOCKWEBOTHHAVE_FIELD_NUMBER: _ClassVar[int]
        ISACTIVE_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        NODECOUNT_FIELD_NUMBER: _ClassVar[int]
        INFLOW_FIELD_NUMBER: _ClassVar[int]
        DISCONNECTTIMES_FIELD_NUMBER: _ClassVar[int]
        LOCALDISCONNECTREASON_FIELD_NUMBER: _ClassVar[int]
        REMOTEDISCONNECTREASON_FIELD_NUMBER: _ClassVar[int]
        lastSyncBlock: str
        remainNum: int
        lastBlockUpdateTime: int
        syncFlag: bool
        headBlockTimeWeBothHave: int
        needSyncFromPeer: bool
        needSyncFromUs: bool
        host: str
        port: int
        nodeId: str
        connectTime: int
        avgLatency: float
        syncToFetchSize: int
        syncToFetchSizePeekNum: int
        syncBlockRequestedSize: int
        unFetchSynNum: int
        blockInPorcSize: int
        headBlockWeBothHave: str
        isActive: bool
        score: int
        nodeCount: int
        inFlow: int
        disconnectTimes: int
        localDisconnectReason: str
        remoteDisconnectReason: str
        def __init__(self, lastSyncBlock: _Optional[str] = ..., remainNum: _Optional[int] = ..., lastBlockUpdateTime: _Optional[int] = ..., syncFlag: bool = ..., headBlockTimeWeBothHave: _Optional[int] = ..., needSyncFromPeer: bool = ..., needSyncFromUs: bool = ..., host: _Optional[str] = ..., port: _Optional[int] = ..., nodeId: _Optional[str] = ..., connectTime: _Optional[int] = ..., avgLatency: _Optional[float] = ..., syncToFetchSize: _Optional[int] = ..., syncToFetchSizePeekNum: _Optional[int] = ..., syncBlockRequestedSize: _Optional[int] = ..., unFetchSynNum: _Optional[int] = ..., blockInPorcSize: _Optional[int] = ..., headBlockWeBothHave: _Optional[str] = ..., isActive: bool = ..., score: _Optional[int] = ..., nodeCount: _Optional[int] = ..., inFlow: _Optional[int] = ..., disconnectTimes: _Optional[int] = ..., localDisconnectReason: _Optional[str] = ..., remoteDisconnectReason: _Optional[str] = ...) -> None: ...
    class ConfigNodeInfo(_message.Message):
        __slots__ = ("codeVersion", "p2pVersion", "listenPort", "discoverEnable", "activeNodeSize", "passiveNodeSize", "sendNodeSize", "maxConnectCount", "sameIpMaxConnectCount", "backupListenPort", "backupMemberSize", "backupPriority", "dbVersion", "minParticipationRate", "supportConstant", "minTimeRatio", "maxTimeRatio", "allowCreationOfContracts", "allowAdaptiveEnergy")
        CODEVERSION_FIELD_NUMBER: _ClassVar[int]
        P2PVERSION_FIELD_NUMBER: _ClassVar[int]
        LISTENPORT_FIELD_NUMBER: _ClassVar[int]
        DISCOVERENABLE_FIELD_NUMBER: _ClassVar[int]
        ACTIVENODESIZE_FIELD_NUMBER: _ClassVar[int]
        PASSIVENODESIZE_FIELD_NUMBER: _ClassVar[int]
        SENDNODESIZE_FIELD_NUMBER: _ClassVar[int]
        MAXCONNECTCOUNT_FIELD_NUMBER: _ClassVar[int]
        SAMEIPMAXCONNECTCOUNT_FIELD_NUMBER: _ClassVar[int]
        BACKUPLISTENPORT_FIELD_NUMBER: _ClassVar[int]
        BACKUPMEMBERSIZE_FIELD_NUMBER: _ClassVar[int]
        BACKUPPRIORITY_FIELD_NUMBER: _ClassVar[int]
        DBVERSION_FIELD_NUMBER: _ClassVar[int]
        MINPARTICIPATIONRATE_FIELD_NUMBER: _ClassVar[int]
        SUPPORTCONSTANT_FIELD_NUMBER: _ClassVar[int]
        MINTIMERATIO_FIELD_NUMBER: _ClassVar[int]
        MAXTIMERATIO_FIELD_NUMBER: _ClassVar[int]
        ALLOWCREATIONOFCONTRACTS_FIELD_NUMBER: _ClassVar[int]
        ALLOWADAPTIVEENERGY_FIELD_NUMBER: _ClassVar[int]
        codeVersion: str
        p2pVersion: str
        listenPort: int
        discoverEnable: bool
        activeNodeSize: int
        passiveNodeSize: int
        sendNodeSize: int
        maxConnectCount: int
        sameIpMaxConnectCount: int
        backupListenPort: int
        backupMemberSize: int
        backupPriority: int
        dbVersion: int
        minParticipationRate: int
        supportConstant: bool
        minTimeRatio: float
        maxTimeRatio: float
        allowCreationOfContracts: int
        allowAdaptiveEnergy: int
        def __init__(self, codeVersion: _Optional[str] = ..., p2pVersion: _Optional[str] = ..., listenPort: _Optional[int] = ..., discoverEnable: bool = ..., activeNodeSize: _Optional[int] = ..., passiveNodeSize: _Optional[int] = ..., sendNodeSize: _Optional[int] = ..., maxConnectCount: _Optional[int] = ..., sameIpMaxConnectCount: _Optional[int] = ..., backupListenPort: _Optional[int] = ..., backupMemberSize: _Optional[int] = ..., backupPriority: _Optional[int] = ..., dbVersion: _Optional[int] = ..., minParticipationRate: _Optional[int] = ..., supportConstant: bool = ..., minTimeRatio: _Optional[float] = ..., maxTimeRatio: _Optional[float] = ..., allowCreationOfContracts: _Optional[int] = ..., allowAdaptiveEnergy: _Optional[int] = ...) -> None: ...
    class MachineInfo(_message.Message):
        __slots__ = ("threadCount", "deadLockThreadCount", "cpuCount", "totalMemory", "freeMemory", "cpuRate", "javaVersion", "osName", "jvmTotalMemory", "jvmFreeMemory", "processCpuRate", "memoryDescInfoList", "deadLockThreadInfoList")
        class MemoryDescInfo(_message.Message):
            __slots__ = ("name", "initSize", "useSize", "maxSize", "useRate")
            NAME_FIELD_NUMBER: _ClassVar[int]
            INITSIZE_FIELD_NUMBER: _ClassVar[int]
            USESIZE_FIELD_NUMBER: _ClassVar[int]
            MAXSIZE_FIELD_NUMBER: _ClassVar[int]
            USERATE_FIELD_NUMBER: _ClassVar[int]
            name: str
            initSize: int
            useSize: int
            maxSize: int
            useRate: float
            def __init__(self, name: _Optional[str] = ..., initSize: _Optional[int] = ..., useSize: _Optional[int] = ..., maxSize: _Optional[int] = ..., useRate: _Optional[float] = ...) -> None: ...
        class DeadLockThreadInfo(_message.Message):
            __slots__ = ("name", "lockName", "lockOwner", "state", "blockTime", "waitTime", "stackTrace")
            NAME_FIELD_NUMBER: _ClassVar[int]
            LOCKNAME_FIELD_NUMBER: _ClassVar[int]
            LOCKOWNER_FIELD_NUMBER: _ClassVar[int]
            STATE_FIELD_NUMBER: _ClassVar[int]
            BLOCKTIME_FIELD_NUMBER: _ClassVar[int]
            WAITTIME_FIELD_NUMBER: _ClassVar[int]
            STACKTRACE_FIELD_NUMBER: _ClassVar[int]
            name: str
            lockName: str
            lockOwner: str
            state: str
            blockTime: int
            waitTime: int
            stackTrace: str
            def __init__(self, name: _Optional[str] = ..., lockName: _Optional[str] = ..., lockOwner: _Optional[str] = ..., state: _Optional[str] = ..., blockTime: _Optional[int] = ..., waitTime: _Optional[int] = ..., stackTrace: _Optional[str] = ...) -> None: ...
        THREADCOUNT_FIELD_NUMBER: _ClassVar[int]
        DEADLOCKTHREADCOUNT_FIELD_NUMBER: _ClassVar[int]
        CPUCOUNT_FIELD_NUMBER: _ClassVar[int]
        TOTALMEMORY_FIELD_NUMBER: _ClassVar[int]
        FREEMEMORY_FIELD_NUMBER: _ClassVar[int]
        CPURATE_FIELD_NUMBER: _ClassVar[int]
        JAVAVERSION_FIELD_NUMBER: _ClassVar[int]
        OSNAME_FIELD_NUMBER: _ClassVar[int]
        JVMTOTALMEMORY_FIELD_NUMBER: _ClassVar[int]
        JVMFREEMEMORY_FIELD_NUMBER: _ClassVar[int]
        PROCESSCPURATE_FIELD_NUMBER: _ClassVar[int]
        MEMORYDESCINFOLIST_FIELD_NUMBER: _ClassVar[int]
        DEADLOCKTHREADINFOLIST_FIELD_NUMBER: _ClassVar[int]
        threadCount: int
        deadLockThreadCount: int
        cpuCount: int
        totalMemory: int
        freeMemory: int
        cpuRate: float
        javaVersion: str
        osName: str
        jvmTotalMemory: int
        jvmFreeMemory: int
        processCpuRate: float
        memoryDescInfoList: _containers.RepeatedCompositeFieldContainer[NodeInfo.MachineInfo.MemoryDescInfo]
        deadLockThreadInfoList: _containers.RepeatedCompositeFieldContainer[NodeInfo.MachineInfo.DeadLockThreadInfo]
        def __init__(self, threadCount: _Optional[int] = ..., deadLockThreadCount: _Optional[int] = ..., cpuCount: _Optional[int] = ..., totalMemory: _Optional[int] = ..., freeMemory: _Optional[int] = ..., cpuRate: _Optional[float] = ..., javaVersion: _Optional[str] = ..., osName: _Optional[str] = ..., jvmTotalMemory: _Optional[int] = ..., jvmFreeMemory: _Optional[int] = ..., processCpuRate: _Optional[float] = ..., memoryDescInfoList: _Optional[_Iterable[_Union[NodeInfo.MachineInfo.MemoryDescInfo, _Mapping]]] = ..., deadLockThreadInfoList: _Optional[_Iterable[_Union[NodeInfo.MachineInfo.DeadLockThreadInfo, _Mapping]]] = ...) -> None: ...
    BEGINSYNCNUM_FIELD_NUMBER: _ClassVar[int]
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    SOLIDITYBLOCK_FIELD_NUMBER: _ClassVar[int]
    CURRENTCONNECTCOUNT_FIELD_NUMBER: _ClassVar[int]
    ACTIVECONNECTCOUNT_FIELD_NUMBER: _ClassVar[int]
    PASSIVECONNECTCOUNT_FIELD_NUMBER: _ClassVar[int]
    TOTALFLOW_FIELD_NUMBER: _ClassVar[int]
    PEERINFOLIST_FIELD_NUMBER: _ClassVar[int]
    CONFIGNODEINFO_FIELD_NUMBER: _ClassVar[int]
    MACHINEINFO_FIELD_NUMBER: _ClassVar[int]
    CHEATWITNESSINFOMAP_FIELD_NUMBER: _ClassVar[int]
    beginSyncNum: int
    block: str
    solidityBlock: str
    currentConnectCount: int
    activeConnectCount: int
    passiveConnectCount: int
    totalFlow: int
    peerInfoList: _containers.RepeatedCompositeFieldContainer[NodeInfo.PeerInfo]
    configNodeInfo: NodeInfo.ConfigNodeInfo
    machineInfo: NodeInfo.MachineInfo
    cheatWitnessInfoMap: _containers.ScalarMap[str, str]
    def __init__(self, beginSyncNum: _Optional[int] = ..., block: _Optional[str] = ..., solidityBlock: _Optional[str] = ..., currentConnectCount: _Optional[int] = ..., activeConnectCount: _Optional[int] = ..., passiveConnectCount: _Optional[int] = ..., totalFlow: _Optional[int] = ..., peerInfoList: _Optional[_Iterable[_Union[NodeInfo.PeerInfo, _Mapping]]] = ..., configNodeInfo: _Optional[_Union[NodeInfo.ConfigNodeInfo, _Mapping]] = ..., machineInfo: _Optional[_Union[NodeInfo.MachineInfo, _Mapping]] = ..., cheatWitnessInfoMap: _Optional[_Mapping[str, str]] = ...) -> None: ...

class MetricsInfo(_message.Message):
    __slots__ = ("interval", "node", "blockchain", "net")
    class NodeInfo(_message.Message):
        __slots__ = ("ip", "nodeType", "version", "backupStatus")
        IP_FIELD_NUMBER: _ClassVar[int]
        NODETYPE_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        BACKUPSTATUS_FIELD_NUMBER: _ClassVar[int]
        ip: str
        nodeType: int
        version: str
        backupStatus: int
        def __init__(self, ip: _Optional[str] = ..., nodeType: _Optional[int] = ..., version: _Optional[str] = ..., backupStatus: _Optional[int] = ...) -> None: ...
    class BlockChainInfo(_message.Message):
        __slots__ = ("headBlockNum", "headBlockTimestamp", "headBlockHash", "forkCount", "failForkCount", "blockProcessTime", "tps", "transactionCacheSize", "missedTransaction", "witnesses", "failProcessBlockNum", "failProcessBlockReason", "dupWitness")
        class Witness(_message.Message):
            __slots__ = ("address", "version")
            ADDRESS_FIELD_NUMBER: _ClassVar[int]
            VERSION_FIELD_NUMBER: _ClassVar[int]
            address: str
            version: int
            def __init__(self, address: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...
        class DupWitness(_message.Message):
            __slots__ = ("address", "blockNum", "count")
            ADDRESS_FIELD_NUMBER: _ClassVar[int]
            BLOCKNUM_FIELD_NUMBER: _ClassVar[int]
            COUNT_FIELD_NUMBER: _ClassVar[int]
            address: str
            blockNum: int
            count: int
            def __init__(self, address: _Optional[str] = ..., blockNum: _Optional[int] = ..., count: _Optional[int] = ...) -> None: ...
        HEADBLOCKNUM_FIELD_NUMBER: _ClassVar[int]
        HEADBLOCKTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        HEADBLOCKHASH_FIELD_NUMBER: _ClassVar[int]
        FORKCOUNT_FIELD_NUMBER: _ClassVar[int]
        FAILFORKCOUNT_FIELD_NUMBER: _ClassVar[int]
        BLOCKPROCESSTIME_FIELD_NUMBER: _ClassVar[int]
        TPS_FIELD_NUMBER: _ClassVar[int]
        TRANSACTIONCACHESIZE_FIELD_NUMBER: _ClassVar[int]
        MISSEDTRANSACTION_FIELD_NUMBER: _ClassVar[int]
        WITNESSES_FIELD_NUMBER: _ClassVar[int]
        FAILPROCESSBLOCKNUM_FIELD_NUMBER: _ClassVar[int]
        FAILPROCESSBLOCKREASON_FIELD_NUMBER: _ClassVar[int]
        DUPWITNESS_FIELD_NUMBER: _ClassVar[int]
        headBlockNum: int
        headBlockTimestamp: int
        headBlockHash: str
        forkCount: int
        failForkCount: int
        blockProcessTime: MetricsInfo.RateInfo
        tps: MetricsInfo.RateInfo
        transactionCacheSize: int
        missedTransaction: MetricsInfo.RateInfo
        witnesses: _containers.RepeatedCompositeFieldContainer[MetricsInfo.BlockChainInfo.Witness]
        failProcessBlockNum: int
        failProcessBlockReason: str
        dupWitness: _containers.RepeatedCompositeFieldContainer[MetricsInfo.BlockChainInfo.DupWitness]
        def __init__(self, headBlockNum: _Optional[int] = ..., headBlockTimestamp: _Optional[int] = ..., headBlockHash: _Optional[str] = ..., forkCount: _Optional[int] = ..., failForkCount: _Optional[int] = ..., blockProcessTime: _Optional[_Union[MetricsInfo.RateInfo, _Mapping]] = ..., tps: _Optional[_Union[MetricsInfo.RateInfo, _Mapping]] = ..., transactionCacheSize: _Optional[int] = ..., missedTransaction: _Optional[_Union[MetricsInfo.RateInfo, _Mapping]] = ..., witnesses: _Optional[_Iterable[_Union[MetricsInfo.BlockChainInfo.Witness, _Mapping]]] = ..., failProcessBlockNum: _Optional[int] = ..., failProcessBlockReason: _Optional[str] = ..., dupWitness: _Optional[_Iterable[_Union[MetricsInfo.BlockChainInfo.DupWitness, _Mapping]]] = ...) -> None: ...
    class RateInfo(_message.Message):
        __slots__ = ("count", "meanRate", "oneMinuteRate", "fiveMinuteRate", "fifteenMinuteRate")
        COUNT_FIELD_NUMBER: _ClassVar[int]
        MEANRATE_FIELD_NUMBER: _ClassVar[int]
        ONEMINUTERATE_FIELD_NUMBER: _ClassVar[int]
        FIVEMINUTERATE_FIELD_NUMBER: _ClassVar[int]
        FIFTEENMINUTERATE_FIELD_NUMBER: _ClassVar[int]
        count: int
        meanRate: float
        oneMinuteRate: float
        fiveMinuteRate: float
        fifteenMinuteRate: float
        def __init__(self, count: _Optional[int] = ..., meanRate: _Optional[float] = ..., oneMinuteRate: _Optional[float] = ..., fiveMinuteRate: _Optional[float] = ..., fifteenMinuteRate: _Optional[float] = ...) -> None: ...
    class NetInfo(_message.Message):
        __slots__ = ("errorProtoCount", "api", "connectionCount", "validConnectionCount", "tcpInTraffic", "tcpOutTraffic", "disconnectionCount", "disconnectionDetail", "udpInTraffic", "udpOutTraffic", "latency")
        class ApiInfo(_message.Message):
            __slots__ = ("qps", "failQps", "outTraffic", "detail")
            class ApiDetailInfo(_message.Message):
                __slots__ = ("name", "qps", "failQps", "outTraffic")
                NAME_FIELD_NUMBER: _ClassVar[int]
                QPS_FIELD_NUMBER: _ClassVar[int]
                FAILQPS_FIELD_NUMBER: _ClassVar[int]
                OUTTRAFFIC_FIELD_NUMBER: _ClassVar[int]
                name: str
                qps: MetricsInfo.RateInfo
                failQps: MetricsInfo.RateInfo
                outTraffic: MetricsInfo.RateInfo
                def __init__(self, name: _Optional[str] = ..., qps: _Optional[_Union[MetricsInfo.RateInfo, _Mapping]] = ..., failQps: _Optional[_Union[MetricsInfo.RateInfo, _Mapping]] = ..., outTraffic: _Optional[_Union[MetricsInfo.RateInfo, _Mapping]] = ...) -> None: ...
            QPS_FIELD_NUMBER: _ClassVar[int]
            FAILQPS_FIELD_NUMBER: _ClassVar[int]
            OUTTRAFFIC_FIELD_NUMBER: _ClassVar[int]
            DETAIL_FIELD_NUMBER: _ClassVar[int]
            qps: MetricsInfo.RateInfo
            failQps: MetricsInfo.RateInfo
            outTraffic: MetricsInfo.RateInfo
            detail: _containers.RepeatedCompositeFieldContainer[MetricsInfo.NetInfo.ApiInfo.ApiDetailInfo]
            def __init__(self, qps: _Optional[_Union[MetricsInfo.RateInfo, _Mapping]] = ..., failQps: _Optional[_Union[MetricsInfo.RateInfo, _Mapping]] = ..., outTraffic: _Optional[_Union[MetricsInfo.RateInfo, _Mapping]] = ..., detail: _Optional[_Iterable[_Union[MetricsInfo.NetInfo.ApiInfo.ApiDetailInfo, _Mapping]]] = ...) -> None: ...
        class DisconnectionDetailInfo(_message.Message):
            __slots__ = ("reason", "count")
            REASON_FIELD_NUMBER: _ClassVar[int]
            COUNT_FIELD_NUMBER: _ClassVar[int]
            reason: str
            count: int
            def __init__(self, reason: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...
        class LatencyInfo(_message.Message):
            __slots__ = ("top99", "top95", "top75", "totalCount", "delay1S", "delay2S", "delay3S", "detail")
            class LatencyDetailInfo(_message.Message):
                __slots__ = ("witness", "top99", "top95", "top75", "count", "delay1S", "delay2S", "delay3S")
                WITNESS_FIELD_NUMBER: _ClassVar[int]
                TOP99_FIELD_NUMBER: _ClassVar[int]
                TOP95_FIELD_NUMBER: _ClassVar[int]
                TOP75_FIELD_NUMBER: _ClassVar[int]
                COUNT_FIELD_NUMBER: _ClassVar[int]
                DELAY1S_FIELD_NUMBER: _ClassVar[int]
                DELAY2S_FIELD_NUMBER: _ClassVar[int]
                DELAY3S_FIELD_NUMBER: _ClassVar[int]
                witness: str
                top99: int
                top95: int
                top75: int
                count: int
                delay1S: int
                delay2S: int
                delay3S: int
                def __init__(self, witness: _Optional[str] = ..., top99: _Optional[int] = ..., top95: _Optional[int] = ..., top75: _Optional[int] = ..., count: _Optional[int] = ..., delay1S: _Optional[int] = ..., delay2S: _Optional[int] = ..., delay3S: _Optional[int] = ...) -> None: ...
            TOP99_FIELD_NUMBER: _ClassVar[int]
            TOP95_FIELD_NUMBER: _ClassVar[int]
            TOP75_FIELD_NUMBER: _ClassVar[int]
            TOTALCOUNT_FIELD_NUMBER: _ClassVar[int]
            DELAY1S_FIELD_NUMBER: _ClassVar[int]
            DELAY2S_FIELD_NUMBER: _ClassVar[int]
            DELAY3S_FIELD_NUMBER: _ClassVar[int]
            DETAIL_FIELD_NUMBER: _ClassVar[int]
            top99: int
            top95: int
            top75: int
            totalCount: int
            delay1S: int
            delay2S: int
            delay3S: int
            detail: _containers.RepeatedCompositeFieldContainer[MetricsInfo.NetInfo.LatencyInfo.LatencyDetailInfo]
            def __init__(self, top99: _Optional[int] = ..., top95: _Optional[int] = ..., top75: _Optional[int] = ..., totalCount: _Optional[int] = ..., delay1S: _Optional[int] = ..., delay2S: _Optional[int] = ..., delay3S: _Optional[int] = ..., detail: _Optional[_Iterable[_Union[MetricsInfo.NetInfo.LatencyInfo.LatencyDetailInfo, _Mapping]]] = ...) -> None: ...
        ERRORPROTOCOUNT_FIELD_NUMBER: _ClassVar[int]
        API_FIELD_NUMBER: _ClassVar[int]
        CONNECTIONCOUNT_FIELD_NUMBER: _ClassVar[int]
        VALIDCONNECTIONCOUNT_FIELD_NUMBER: _ClassVar[int]
        TCPINTRAFFIC_FIELD_NUMBER: _ClassVar[int]
        TCPOUTTRAFFIC_FIELD_NUMBER: _ClassVar[int]
        DISCONNECTIONCOUNT_FIELD_NUMBER: _ClassVar[int]
        DISCONNECTIONDETAIL_FIELD_NUMBER: _ClassVar[int]
        UDPINTRAFFIC_FIELD_NUMBER: _ClassVar[int]
        UDPOUTTRAFFIC_FIELD_NUMBER: _ClassVar[int]
        LATENCY_FIELD_NUMBER: _ClassVar[int]
        errorProtoCount: int
        api: MetricsInfo.NetInfo.ApiInfo
        connectionCount: int
        validConnectionCount: int
        tcpInTraffic: MetricsInfo.RateInfo
        tcpOutTraffic: MetricsInfo.RateInfo
        disconnectionCount: int
        disconnectionDetail: _containers.RepeatedCompositeFieldContainer[MetricsInfo.NetInfo.DisconnectionDetailInfo]
        udpInTraffic: MetricsInfo.RateInfo
        udpOutTraffic: MetricsInfo.RateInfo
        latency: MetricsInfo.NetInfo.LatencyInfo
        def __init__(self, errorProtoCount: _Optional[int] = ..., api: _Optional[_Union[MetricsInfo.NetInfo.ApiInfo, _Mapping]] = ..., connectionCount: _Optional[int] = ..., validConnectionCount: _Optional[int] = ..., tcpInTraffic: _Optional[_Union[MetricsInfo.RateInfo, _Mapping]] = ..., tcpOutTraffic: _Optional[_Union[MetricsInfo.RateInfo, _Mapping]] = ..., disconnectionCount: _Optional[int] = ..., disconnectionDetail: _Optional[_Iterable[_Union[MetricsInfo.NetInfo.DisconnectionDetailInfo, _Mapping]]] = ..., udpInTraffic: _Optional[_Union[MetricsInfo.RateInfo, _Mapping]] = ..., udpOutTraffic: _Optional[_Union[MetricsInfo.RateInfo, _Mapping]] = ..., latency: _Optional[_Union[MetricsInfo.NetInfo.LatencyInfo, _Mapping]] = ...) -> None: ...
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    NODE_FIELD_NUMBER: _ClassVar[int]
    BLOCKCHAIN_FIELD_NUMBER: _ClassVar[int]
    NET_FIELD_NUMBER: _ClassVar[int]
    interval: int
    node: MetricsInfo.NodeInfo
    blockchain: MetricsInfo.BlockChainInfo
    net: MetricsInfo.NetInfo
    def __init__(self, interval: _Optional[int] = ..., node: _Optional[_Union[MetricsInfo.NodeInfo, _Mapping]] = ..., blockchain: _Optional[_Union[MetricsInfo.BlockChainInfo, _Mapping]] = ..., net: _Optional[_Union[MetricsInfo.NetInfo, _Mapping]] = ...) -> None: ...

class PBFTMessage(_message.Message):
    __slots__ = ("raw_data", "signature")
    class MsgType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VIEW_CHANGE: _ClassVar[PBFTMessage.MsgType]
        REQUEST: _ClassVar[PBFTMessage.MsgType]
        PREPREPARE: _ClassVar[PBFTMessage.MsgType]
        PREPARE: _ClassVar[PBFTMessage.MsgType]
        COMMIT: _ClassVar[PBFTMessage.MsgType]
    VIEW_CHANGE: PBFTMessage.MsgType
    REQUEST: PBFTMessage.MsgType
    PREPREPARE: PBFTMessage.MsgType
    PREPARE: PBFTMessage.MsgType
    COMMIT: PBFTMessage.MsgType
    class DataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BLOCK: _ClassVar[PBFTMessage.DataType]
        SRL: _ClassVar[PBFTMessage.DataType]
    BLOCK: PBFTMessage.DataType
    SRL: PBFTMessage.DataType
    class Raw(_message.Message):
        __slots__ = ("msg_type", "data_type", "view_n", "epoch", "data")
        MSG_TYPE_FIELD_NUMBER: _ClassVar[int]
        DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
        VIEW_N_FIELD_NUMBER: _ClassVar[int]
        EPOCH_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        msg_type: PBFTMessage.MsgType
        data_type: PBFTMessage.DataType
        view_n: int
        epoch: int
        data: bytes
        def __init__(self, msg_type: _Optional[_Union[PBFTMessage.MsgType, str]] = ..., data_type: _Optional[_Union[PBFTMessage.DataType, str]] = ..., view_n: _Optional[int] = ..., epoch: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...
    RAW_DATA_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    raw_data: PBFTMessage.Raw
    signature: bytes
    def __init__(self, raw_data: _Optional[_Union[PBFTMessage.Raw, _Mapping]] = ..., signature: _Optional[bytes] = ...) -> None: ...

class PBFTCommitResult(_message.Message):
    __slots__ = ("data", "signature")
    DATA_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    signature: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, data: _Optional[bytes] = ..., signature: _Optional[_Iterable[bytes]] = ...) -> None: ...

class SRL(_message.Message):
    __slots__ = ("srAddress",)
    SRADDRESS_FIELD_NUMBER: _ClassVar[int]
    srAddress: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, srAddress: _Optional[_Iterable[bytes]] = ...) -> None: ...
