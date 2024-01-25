from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuthenticationPath(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedScalarFieldContainer[bool]
    def __init__(self, value: _Optional[_Iterable[bool]] = ...) -> None: ...

class MerklePath(_message.Message):
    __slots__ = ("authentication_paths", "index", "rt")
    AUTHENTICATION_PATHS_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    RT_FIELD_NUMBER: _ClassVar[int]
    authentication_paths: _containers.RepeatedCompositeFieldContainer[AuthenticationPath]
    index: _containers.RepeatedScalarFieldContainer[bool]
    rt: bytes
    def __init__(self, authentication_paths: _Optional[_Iterable[_Union[AuthenticationPath, _Mapping]]] = ..., index: _Optional[_Iterable[bool]] = ..., rt: _Optional[bytes] = ...) -> None: ...

class OutputPoint(_message.Message):
    __slots__ = ("hash", "index")
    HASH_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    hash: bytes
    index: int
    def __init__(self, hash: _Optional[bytes] = ..., index: _Optional[int] = ...) -> None: ...

class OutputPointInfo(_message.Message):
    __slots__ = ("out_points", "block_num")
    OUT_POINTS_FIELD_NUMBER: _ClassVar[int]
    BLOCK_NUM_FIELD_NUMBER: _ClassVar[int]
    out_points: _containers.RepeatedCompositeFieldContainer[OutputPoint]
    block_num: int
    def __init__(self, out_points: _Optional[_Iterable[_Union[OutputPoint, _Mapping]]] = ..., block_num: _Optional[int] = ...) -> None: ...

class PedersenHash(_message.Message):
    __slots__ = ("content",)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: bytes
    def __init__(self, content: _Optional[bytes] = ...) -> None: ...

class IncrementalMerkleTree(_message.Message):
    __slots__ = ("left", "right", "parents")
    LEFT_FIELD_NUMBER: _ClassVar[int]
    RIGHT_FIELD_NUMBER: _ClassVar[int]
    PARENTS_FIELD_NUMBER: _ClassVar[int]
    left: PedersenHash
    right: PedersenHash
    parents: _containers.RepeatedCompositeFieldContainer[PedersenHash]
    def __init__(self, left: _Optional[_Union[PedersenHash, _Mapping]] = ..., right: _Optional[_Union[PedersenHash, _Mapping]] = ..., parents: _Optional[_Iterable[_Union[PedersenHash, _Mapping]]] = ...) -> None: ...

class IncrementalMerkleVoucher(_message.Message):
    __slots__ = ("tree", "filled", "cursor", "cursor_depth", "rt", "output_point")
    TREE_FIELD_NUMBER: _ClassVar[int]
    FILLED_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    CURSOR_DEPTH_FIELD_NUMBER: _ClassVar[int]
    RT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_POINT_FIELD_NUMBER: _ClassVar[int]
    tree: IncrementalMerkleTree
    filled: _containers.RepeatedCompositeFieldContainer[PedersenHash]
    cursor: IncrementalMerkleTree
    cursor_depth: int
    rt: bytes
    output_point: OutputPoint
    def __init__(self, tree: _Optional[_Union[IncrementalMerkleTree, _Mapping]] = ..., filled: _Optional[_Iterable[_Union[PedersenHash, _Mapping]]] = ..., cursor: _Optional[_Union[IncrementalMerkleTree, _Mapping]] = ..., cursor_depth: _Optional[int] = ..., rt: _Optional[bytes] = ..., output_point: _Optional[_Union[OutputPoint, _Mapping]] = ...) -> None: ...

class IncrementalMerkleVoucherInfo(_message.Message):
    __slots__ = ("vouchers", "paths")
    VOUCHERS_FIELD_NUMBER: _ClassVar[int]
    PATHS_FIELD_NUMBER: _ClassVar[int]
    vouchers: _containers.RepeatedCompositeFieldContainer[IncrementalMerkleVoucher]
    paths: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, vouchers: _Optional[_Iterable[_Union[IncrementalMerkleVoucher, _Mapping]]] = ..., paths: _Optional[_Iterable[bytes]] = ...) -> None: ...

class SpendDescription(_message.Message):
    __slots__ = ("value_commitment", "anchor", "nullifier", "rk", "zkproof", "spend_authority_signature")
    VALUE_COMMITMENT_FIELD_NUMBER: _ClassVar[int]
    ANCHOR_FIELD_NUMBER: _ClassVar[int]
    NULLIFIER_FIELD_NUMBER: _ClassVar[int]
    RK_FIELD_NUMBER: _ClassVar[int]
    ZKPROOF_FIELD_NUMBER: _ClassVar[int]
    SPEND_AUTHORITY_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    value_commitment: bytes
    anchor: bytes
    nullifier: bytes
    rk: bytes
    zkproof: bytes
    spend_authority_signature: bytes
    def __init__(self, value_commitment: _Optional[bytes] = ..., anchor: _Optional[bytes] = ..., nullifier: _Optional[bytes] = ..., rk: _Optional[bytes] = ..., zkproof: _Optional[bytes] = ..., spend_authority_signature: _Optional[bytes] = ...) -> None: ...

class ReceiveDescription(_message.Message):
    __slots__ = ("value_commitment", "note_commitment", "epk", "c_enc", "c_out", "zkproof")
    VALUE_COMMITMENT_FIELD_NUMBER: _ClassVar[int]
    NOTE_COMMITMENT_FIELD_NUMBER: _ClassVar[int]
    EPK_FIELD_NUMBER: _ClassVar[int]
    C_ENC_FIELD_NUMBER: _ClassVar[int]
    C_OUT_FIELD_NUMBER: _ClassVar[int]
    ZKPROOF_FIELD_NUMBER: _ClassVar[int]
    value_commitment: bytes
    note_commitment: bytes
    epk: bytes
    c_enc: bytes
    c_out: bytes
    zkproof: bytes
    def __init__(self, value_commitment: _Optional[bytes] = ..., note_commitment: _Optional[bytes] = ..., epk: _Optional[bytes] = ..., c_enc: _Optional[bytes] = ..., c_out: _Optional[bytes] = ..., zkproof: _Optional[bytes] = ...) -> None: ...

class ShieldedTransferContract(_message.Message):
    __slots__ = ("transparent_from_address", "from_amount", "spend_description", "receive_description", "binding_signature", "transparent_to_address", "to_amount")
    TRANSPARENT_FROM_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    FROM_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    SPEND_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RECEIVE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BINDING_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    TRANSPARENT_TO_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TO_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    transparent_from_address: bytes
    from_amount: int
    spend_description: _containers.RepeatedCompositeFieldContainer[SpendDescription]
    receive_description: _containers.RepeatedCompositeFieldContainer[ReceiveDescription]
    binding_signature: bytes
    transparent_to_address: bytes
    to_amount: int
    def __init__(self, transparent_from_address: _Optional[bytes] = ..., from_amount: _Optional[int] = ..., spend_description: _Optional[_Iterable[_Union[SpendDescription, _Mapping]]] = ..., receive_description: _Optional[_Iterable[_Union[ReceiveDescription, _Mapping]]] = ..., binding_signature: _Optional[bytes] = ..., transparent_to_address: _Optional[bytes] = ..., to_amount: _Optional[int] = ...) -> None: ...
