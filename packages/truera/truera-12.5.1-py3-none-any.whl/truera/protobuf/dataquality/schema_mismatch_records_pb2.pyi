from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RowsetSchemaMismatchRecords(_message.Message):
    __slots__ = ["rowset_id", "total_row_count", "feature_names", "schema_mismatch_rows"]
    ROWSET_ID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    FEATURE_NAMES_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_MISMATCH_ROWS_FIELD_NUMBER: _ClassVar[int]
    rowset_id: str
    total_row_count: int
    feature_names: _containers.RepeatedScalarFieldContainer[str]
    schema_mismatch_rows: _containers.RepeatedCompositeFieldContainer[SchemaMismatchRow]
    def __init__(self, rowset_id: _Optional[str] = ..., total_row_count: _Optional[int] = ..., feature_names: _Optional[_Iterable[str]] = ..., schema_mismatch_rows: _Optional[_Iterable[_Union[SchemaMismatchRow, _Mapping]]] = ...) -> None: ...

class SchemaMismatchRow(_message.Message):
    __slots__ = ["row_timestamp", "row_string", "schema_mismatch_feature_index", "schema_mismatch_feature_name"]
    ROW_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ROW_STRING_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_MISMATCH_FEATURE_INDEX_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_MISMATCH_FEATURE_NAME_FIELD_NUMBER: _ClassVar[int]
    row_timestamp: _timestamp_pb2.Timestamp
    row_string: _containers.RepeatedScalarFieldContainer[str]
    schema_mismatch_feature_index: _containers.RepeatedScalarFieldContainer[int]
    schema_mismatch_feature_name: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, row_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., row_string: _Optional[_Iterable[str]] = ..., schema_mismatch_feature_index: _Optional[_Iterable[int]] = ..., schema_mismatch_feature_name: _Optional[_Iterable[str]] = ...) -> None: ...
