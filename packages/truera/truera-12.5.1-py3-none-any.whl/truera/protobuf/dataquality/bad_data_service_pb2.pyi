from google.api import annotations_pb2 as _annotations_pb2
from truera.protobuf.dataquality import schema_mismatch_records_pb2 as _schema_mismatch_records_pb2
from truera.protobuf.public.common import data_kind_pb2 as _data_kind_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetSchemaMismatchRowsRequest(_message.Message):
    __slots__ = ["project_id", "split_id", "data_kind"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SPLIT_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_KIND_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    split_id: str
    data_kind: _data_kind_pb2.DataKindDescribed
    def __init__(self, project_id: _Optional[str] = ..., split_id: _Optional[str] = ..., data_kind: _Optional[_Union[_data_kind_pb2.DataKindDescribed, str]] = ...) -> None: ...

class GetSchemaMismatchRowsResponse(_message.Message):
    __slots__ = ["split_id", "total_row_count", "feature_names", "schema_mismatch_row", "data_kind"]
    SPLIT_ID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    FEATURE_NAMES_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_MISMATCH_ROW_FIELD_NUMBER: _ClassVar[int]
    DATA_KIND_FIELD_NUMBER: _ClassVar[int]
    split_id: str
    total_row_count: int
    feature_names: _containers.RepeatedScalarFieldContainer[str]
    schema_mismatch_row: _containers.RepeatedCompositeFieldContainer[_schema_mismatch_records_pb2.SchemaMismatchRow]
    data_kind: _data_kind_pb2.DataKindDescribed
    def __init__(self, split_id: _Optional[str] = ..., total_row_count: _Optional[int] = ..., feature_names: _Optional[_Iterable[str]] = ..., schema_mismatch_row: _Optional[_Iterable[_Union[_schema_mismatch_records_pb2.SchemaMismatchRow, _Mapping]]] = ..., data_kind: _Optional[_Union[_data_kind_pb2.DataKindDescribed, str]] = ...) -> None: ...

class GetSchemaMismatchRowStatsRequest(_message.Message):
    __slots__ = ["project_id", "split_id", "data_kind"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SPLIT_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_KIND_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    split_id: str
    data_kind: _data_kind_pb2.DataKindDescribed
    def __init__(self, project_id: _Optional[str] = ..., split_id: _Optional[str] = ..., data_kind: _Optional[_Union[_data_kind_pb2.DataKindDescribed, str]] = ...) -> None: ...

class GetSchemaMismatchRowStatsResponse(_message.Message):
    __slots__ = ["split_id", "total_row_count", "schema_mismatch_row_count", "feature_schema_mismatch_row_stats", "data_kind"]
    SPLIT_ID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_MISMATCH_ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    FEATURE_SCHEMA_MISMATCH_ROW_STATS_FIELD_NUMBER: _ClassVar[int]
    DATA_KIND_FIELD_NUMBER: _ClassVar[int]
    split_id: str
    total_row_count: int
    schema_mismatch_row_count: int
    feature_schema_mismatch_row_stats: _containers.RepeatedCompositeFieldContainer[FeatureSchemaMismatchRowStats]
    data_kind: _data_kind_pb2.DataKindDescribed
    def __init__(self, split_id: _Optional[str] = ..., total_row_count: _Optional[int] = ..., schema_mismatch_row_count: _Optional[int] = ..., feature_schema_mismatch_row_stats: _Optional[_Iterable[_Union[FeatureSchemaMismatchRowStats, _Mapping]]] = ..., data_kind: _Optional[_Union[_data_kind_pb2.DataKindDescribed, str]] = ...) -> None: ...

class FeatureSchemaMismatchRowStats(_message.Message):
    __slots__ = ["feature_name", "schema_mismatch_row_ratio", "schema_mismatch_row_count", "sample_values"]
    FEATURE_NAME_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_MISMATCH_ROW_RATIO_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_MISMATCH_ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_VALUES_FIELD_NUMBER: _ClassVar[int]
    feature_name: str
    schema_mismatch_row_ratio: float
    schema_mismatch_row_count: int
    sample_values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, feature_name: _Optional[str] = ..., schema_mismatch_row_ratio: _Optional[float] = ..., schema_mismatch_row_count: _Optional[int] = ..., sample_values: _Optional[_Iterable[str]] = ...) -> None: ...
