from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ResourceCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BANDWIDTH: _ClassVar[ResourceCode]
    ENERGY: _ClassVar[ResourceCode]
    TRON_POWER: _ClassVar[ResourceCode]
BANDWIDTH: ResourceCode
ENERGY: ResourceCode
TRON_POWER: ResourceCode
