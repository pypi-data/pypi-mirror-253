from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AssetIssueContract(_message.Message):
    __slots__ = ("id", "owner_address", "name", "abbr", "total_supply", "frozen_supply", "trx_num", "precision", "num", "start_time", "end_time", "order", "vote_score", "description", "url", "free_asset_net_limit", "public_free_asset_net_limit", "public_free_asset_net_usage", "public_latest_free_net_time")
    class FrozenSupply(_message.Message):
        __slots__ = ("frozen_amount", "frozen_days")
        FROZEN_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        FROZEN_DAYS_FIELD_NUMBER: _ClassVar[int]
        frozen_amount: int
        frozen_days: int
        def __init__(self, frozen_amount: _Optional[int] = ..., frozen_days: _Optional[int] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ABBR_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SUPPLY_FIELD_NUMBER: _ClassVar[int]
    FROZEN_SUPPLY_FIELD_NUMBER: _ClassVar[int]
    TRX_NUM_FIELD_NUMBER: _ClassVar[int]
    PRECISION_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    VOTE_SCORE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    FREE_ASSET_NET_LIMIT_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FREE_ASSET_NET_LIMIT_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FREE_ASSET_NET_USAGE_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_LATEST_FREE_NET_TIME_FIELD_NUMBER: _ClassVar[int]
    id: str
    owner_address: bytes
    name: bytes
    abbr: bytes
    total_supply: int
    frozen_supply: _containers.RepeatedCompositeFieldContainer[AssetIssueContract.FrozenSupply]
    trx_num: int
    precision: int
    num: int
    start_time: int
    end_time: int
    order: int
    vote_score: int
    description: bytes
    url: bytes
    free_asset_net_limit: int
    public_free_asset_net_limit: int
    public_free_asset_net_usage: int
    public_latest_free_net_time: int
    def __init__(self, id: _Optional[str] = ..., owner_address: _Optional[bytes] = ..., name: _Optional[bytes] = ..., abbr: _Optional[bytes] = ..., total_supply: _Optional[int] = ..., frozen_supply: _Optional[_Iterable[_Union[AssetIssueContract.FrozenSupply, _Mapping]]] = ..., trx_num: _Optional[int] = ..., precision: _Optional[int] = ..., num: _Optional[int] = ..., start_time: _Optional[int] = ..., end_time: _Optional[int] = ..., order: _Optional[int] = ..., vote_score: _Optional[int] = ..., description: _Optional[bytes] = ..., url: _Optional[bytes] = ..., free_asset_net_limit: _Optional[int] = ..., public_free_asset_net_limit: _Optional[int] = ..., public_free_asset_net_usage: _Optional[int] = ..., public_latest_free_net_time: _Optional[int] = ...) -> None: ...

class TransferAssetContract(_message.Message):
    __slots__ = ("asset_name", "owner_address", "to_address", "amount")
    ASSET_NAME_FIELD_NUMBER: _ClassVar[int]
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TO_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    asset_name: bytes
    owner_address: bytes
    to_address: bytes
    amount: int
    def __init__(self, asset_name: _Optional[bytes] = ..., owner_address: _Optional[bytes] = ..., to_address: _Optional[bytes] = ..., amount: _Optional[int] = ...) -> None: ...

class UnfreezeAssetContract(_message.Message):
    __slots__ = ("owner_address",)
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    def __init__(self, owner_address: _Optional[bytes] = ...) -> None: ...

class UpdateAssetContract(_message.Message):
    __slots__ = ("owner_address", "description", "url", "new_limit", "new_public_limit")
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    NEW_LIMIT_FIELD_NUMBER: _ClassVar[int]
    NEW_PUBLIC_LIMIT_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    description: bytes
    url: bytes
    new_limit: int
    new_public_limit: int
    def __init__(self, owner_address: _Optional[bytes] = ..., description: _Optional[bytes] = ..., url: _Optional[bytes] = ..., new_limit: _Optional[int] = ..., new_public_limit: _Optional[int] = ...) -> None: ...

class ParticipateAssetIssueContract(_message.Message):
    __slots__ = ("owner_address", "to_address", "asset_name", "amount")
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TO_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ASSET_NAME_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    to_address: bytes
    asset_name: bytes
    amount: int
    def __init__(self, owner_address: _Optional[bytes] = ..., to_address: _Optional[bytes] = ..., asset_name: _Optional[bytes] = ..., amount: _Optional[int] = ...) -> None: ...
