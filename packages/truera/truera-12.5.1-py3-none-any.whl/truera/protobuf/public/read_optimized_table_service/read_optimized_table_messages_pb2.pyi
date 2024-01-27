from google.protobuf import timestamp_pb2 as _timestamp_pb2
from protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2
from truera.protobuf.public import common_pb2 as _common_pb2
from truera.protobuf.public.common import data_kind_pb2 as _data_kind_pb2
from truera.protobuf.public.common import schema_pb2 as _schema_pb2
from truera.protobuf.public import qoi_pb2 as _qoi_pb2
from truera.protobuf.public import truera_custom_options_pb2 as _truera_custom_options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RotStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    INVALID: _ClassVar[RotStatus]
    IN_PROGRESS: _ClassVar[RotStatus]
    CANCELLED: _ClassVar[RotStatus]
    FAILURE: _ClassVar[RotStatus]
    SUCCESS: _ClassVar[RotStatus]
INVALID: RotStatus
IN_PROGRESS: RotStatus
CANCELLED: RotStatus
FAILURE: RotStatus
SUCCESS: RotStatus

class RotTableInfo(_message.Message):
    __slots__ = ["table_info", "snapshot_id"]
    TABLE_INFO_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    table_info: _common_pb2.TableInfo
    snapshot_id: str
    def __init__(self, table_info: _Optional[_Union[_common_pb2.TableInfo, _Mapping]] = ..., snapshot_id: _Optional[str] = ...) -> None: ...

class RotQueryMetadata(_message.Message):
    __slots__ = ["project_id", "data_collection_id", "split_id", "model_id"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    SPLIT_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    data_collection_id: str
    split_id: str
    model_id: str
    def __init__(self, project_id: _Optional[str] = ..., data_collection_id: _Optional[str] = ..., split_id: _Optional[str] = ..., model_id: _Optional[str] = ...) -> None: ...

class RotContentMetadata(_message.Message):
    __slots__ = ["data_kinds"]
    DATA_KINDS_FIELD_NUMBER: _ClassVar[int]
    data_kinds: _containers.RepeatedScalarFieldContainer[_data_kind_pb2.DataKindDescribed]
    def __init__(self, data_kinds: _Optional[_Iterable[_Union[_data_kind_pb2.DataKindDescribed, str]]] = ...) -> None: ...

class RotModelContentMetadata(_message.Message):
    __slots__ = ["score_types", "fi_hashes", "prediction_hashes"]
    SCORE_TYPES_FIELD_NUMBER: _ClassVar[int]
    FI_HASHES_FIELD_NUMBER: _ClassVar[int]
    PREDICTION_HASHES_FIELD_NUMBER: _ClassVar[int]
    score_types: _containers.RepeatedScalarFieldContainer[_qoi_pb2.QuantityOfInterest]
    fi_hashes: _containers.RepeatedScalarFieldContainer[str]
    prediction_hashes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, score_types: _Optional[_Iterable[_Union[_qoi_pb2.QuantityOfInterest, str]]] = ..., fi_hashes: _Optional[_Iterable[str]] = ..., prediction_hashes: _Optional[_Iterable[str]] = ...) -> None: ...

class RotMetadata(_message.Message):
    __slots__ = ["id", "query_metadata", "table_info", "content_metadata", "model_content_metadata"]
    ID_FIELD_NUMBER: _ClassVar[int]
    QUERY_METADATA_FIELD_NUMBER: _ClassVar[int]
    TABLE_INFO_FIELD_NUMBER: _ClassVar[int]
    CONTENT_METADATA_FIELD_NUMBER: _ClassVar[int]
    MODEL_CONTENT_METADATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    query_metadata: RotQueryMetadata
    table_info: RotTableInfo
    content_metadata: RotContentMetadata
    model_content_metadata: RotModelContentMetadata
    def __init__(self, id: _Optional[str] = ..., query_metadata: _Optional[_Union[RotQueryMetadata, _Mapping]] = ..., table_info: _Optional[_Union[RotTableInfo, _Mapping]] = ..., content_metadata: _Optional[_Union[RotContentMetadata, _Mapping]] = ..., model_content_metadata: _Optional[_Union[RotModelContentMetadata, _Mapping]] = ...) -> None: ...

class CreateRotArgumentsWrapper(_message.Message):
    __slots__ = ["prediction_score_types", "options_hashes", "pre_column_details", "post_column_details", "extra_column_details", "start_timestamp", "end_timestamp", "tenant_id", "data_collection_id", "model_id", "split_id", "last_updated_timestamp", "mono_table_name", "iceberg_s3_path", "output_table_location_info"]
    PREDICTION_SCORE_TYPES_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_HASHES_FIELD_NUMBER: _ClassVar[int]
    PRE_COLUMN_DETAILS_FIELD_NUMBER: _ClassVar[int]
    POST_COLUMN_DETAILS_FIELD_NUMBER: _ClassVar[int]
    EXTRA_COLUMN_DETAILS_FIELD_NUMBER: _ClassVar[int]
    START_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    END_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    SPLIT_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    MONO_TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    ICEBERG_S3_PATH_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TABLE_LOCATION_INFO_FIELD_NUMBER: _ClassVar[int]
    prediction_score_types: _containers.RepeatedScalarFieldContainer[_qoi_pb2.QuantityOfInterest]
    options_hashes: _containers.RepeatedScalarFieldContainer[str]
    pre_column_details: _containers.RepeatedCompositeFieldContainer[_schema_pb2.ColumnDetails]
    post_column_details: _containers.RepeatedCompositeFieldContainer[_schema_pb2.ColumnDetails]
    extra_column_details: _containers.RepeatedCompositeFieldContainer[_schema_pb2.ColumnDetails]
    start_timestamp: _timestamp_pb2.Timestamp
    end_timestamp: _timestamp_pb2.Timestamp
    tenant_id: str
    data_collection_id: str
    model_id: str
    split_id: str
    last_updated_timestamp: _timestamp_pb2.Timestamp
    mono_table_name: str
    iceberg_s3_path: str
    output_table_location_info: _common_pb2.TableLocationInfo
    def __init__(self, prediction_score_types: _Optional[_Iterable[_Union[_qoi_pb2.QuantityOfInterest, str]]] = ..., options_hashes: _Optional[_Iterable[str]] = ..., pre_column_details: _Optional[_Iterable[_Union[_schema_pb2.ColumnDetails, _Mapping]]] = ..., post_column_details: _Optional[_Iterable[_Union[_schema_pb2.ColumnDetails, _Mapping]]] = ..., extra_column_details: _Optional[_Iterable[_Union[_schema_pb2.ColumnDetails, _Mapping]]] = ..., start_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., tenant_id: _Optional[str] = ..., data_collection_id: _Optional[str] = ..., model_id: _Optional[str] = ..., split_id: _Optional[str] = ..., last_updated_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., mono_table_name: _Optional[str] = ..., iceberg_s3_path: _Optional[str] = ..., output_table_location_info: _Optional[_Union[_common_pb2.TableLocationInfo, _Mapping]] = ...) -> None: ...

class RotOperationsMetadata(_message.Message):
    __slots__ = ["id", "rot_metadata_id", "split_id", "model_id", "status", "last_updated_timestamp", "temporal_workflow_id", "triggered_by"]
    ID_FIELD_NUMBER: _ClassVar[int]
    ROT_METADATA_ID_FIELD_NUMBER: _ClassVar[int]
    SPLIT_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TEMPORAL_WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    TRIGGERED_BY_FIELD_NUMBER: _ClassVar[int]
    id: str
    rot_metadata_id: str
    split_id: str
    model_id: str
    status: RotStatus
    last_updated_timestamp: _timestamp_pb2.Timestamp
    temporal_workflow_id: str
    triggered_by: str
    def __init__(self, id: _Optional[str] = ..., rot_metadata_id: _Optional[str] = ..., split_id: _Optional[str] = ..., model_id: _Optional[str] = ..., status: _Optional[_Union[RotStatus, str]] = ..., last_updated_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., temporal_workflow_id: _Optional[str] = ..., triggered_by: _Optional[str] = ...) -> None: ...
