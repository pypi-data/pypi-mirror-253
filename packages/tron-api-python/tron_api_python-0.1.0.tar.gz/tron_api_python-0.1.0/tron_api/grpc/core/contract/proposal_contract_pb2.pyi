from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ProposalApproveContract(_message.Message):
    __slots__ = ("owner_address", "proposal_id", "is_add_approval")
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PROPOSAL_ID_FIELD_NUMBER: _ClassVar[int]
    IS_ADD_APPROVAL_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    proposal_id: int
    is_add_approval: bool
    def __init__(self, owner_address: _Optional[bytes] = ..., proposal_id: _Optional[int] = ..., is_add_approval: bool = ...) -> None: ...

class ProposalCreateContract(_message.Message):
    __slots__ = ("owner_address", "parameters")
    class ParametersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    parameters: _containers.ScalarMap[int, int]
    def __init__(self, owner_address: _Optional[bytes] = ..., parameters: _Optional[_Mapping[int, int]] = ...) -> None: ...

class ProposalDeleteContract(_message.Message):
    __slots__ = ("owner_address", "proposal_id")
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PROPOSAL_ID_FIELD_NUMBER: _ClassVar[int]
    owner_address: bytes
    proposal_id: int
    def __init__(self, owner_address: _Optional[bytes] = ..., proposal_id: _Optional[int] = ...) -> None: ...
