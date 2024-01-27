from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DataQualityComputationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    UNDEFINED_STATUS: _ClassVar[DataQualityComputationStatus]
    SUCCESS: _ClassVar[DataQualityComputationStatus]
    FAILURE: _ClassVar[DataQualityComputationStatus]
    PENDING: _ClassVar[DataQualityComputationStatus]
    RUNNING: _ClassVar[DataQualityComputationStatus]
UNDEFINED_STATUS: DataQualityComputationStatus
SUCCESS: DataQualityComputationStatus
FAILURE: DataQualityComputationStatus
PENDING: DataQualityComputationStatus
RUNNING: DataQualityComputationStatus
