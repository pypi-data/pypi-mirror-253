from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from truera.protobuf.public import qoi_pb2 as _qoi_pb2
from truera.protobuf.public import truera_custom_options_pb2 as _truera_custom_options_pb2
from truera.protobuf.public.common import metric_pb2 as _metric_pb2
from truera.protobuf.public.common import embedding_pb2 as _embedding_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PingRequest(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class PingResponse(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class IngestPointRequest(_message.Message):
    __slots__ = ["project_id", "data_collection_id", "split_id", "model_id", "score_type", "id", "timestamp", "data", "label", "extra", "prediction_score", "options_hash", "tags", "tokens", "embedding"]
    class DataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
    class ExtraEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    SPLIT_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    PREDICTION_SCORE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_HASH_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    EMBEDDING_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    data_collection_id: str
    split_id: str
    model_id: str
    score_type: _qoi_pb2.QuantityOfInterest
    id: str
    timestamp: str
    data: _containers.MessageMap[str, _struct_pb2.Value]
    label: _struct_pb2.Value
    extra: _containers.MessageMap[str, _struct_pb2.Value]
    prediction_score: _struct_pb2.Value
    options_hash: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    tokens: _containers.RepeatedScalarFieldContainer[str]
    embedding: _embedding_pb2.Embedding
    def __init__(self, project_id: _Optional[str] = ..., data_collection_id: _Optional[str] = ..., split_id: _Optional[str] = ..., model_id: _Optional[str] = ..., score_type: _Optional[_Union[_qoi_pb2.QuantityOfInterest, str]] = ..., id: _Optional[str] = ..., timestamp: _Optional[str] = ..., data: _Optional[_Mapping[str, _struct_pb2.Value]] = ..., label: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., extra: _Optional[_Mapping[str, _struct_pb2.Value]] = ..., prediction_score: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., options_hash: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., tokens: _Optional[_Iterable[str]] = ..., embedding: _Optional[_Union[_embedding_pb2.Embedding, _Mapping]] = ...) -> None: ...

class IngestPointResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class BulkPoint(_message.Message):
    __slots__ = ["id", "timestamp", "score_type", "data", "label", "extra", "prediction_score", "tags", "tokens", "embedding"]
    class DataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
    class ExtraEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SCORE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    PREDICTION_SCORE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    EMBEDDING_FIELD_NUMBER: _ClassVar[int]
    id: str
    timestamp: str
    score_type: _qoi_pb2.QuantityOfInterest
    data: _containers.MessageMap[str, _struct_pb2.Value]
    label: _struct_pb2.Value
    extra: _containers.MessageMap[str, _struct_pb2.Value]
    prediction_score: _struct_pb2.Value
    tags: _containers.RepeatedScalarFieldContainer[str]
    tokens: _containers.RepeatedScalarFieldContainer[str]
    embedding: _embedding_pb2.Embedding
    def __init__(self, id: _Optional[str] = ..., timestamp: _Optional[str] = ..., score_type: _Optional[_Union[_qoi_pb2.QuantityOfInterest, str]] = ..., data: _Optional[_Mapping[str, _struct_pb2.Value]] = ..., label: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., extra: _Optional[_Mapping[str, _struct_pb2.Value]] = ..., prediction_score: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., tags: _Optional[_Iterable[str]] = ..., tokens: _Optional[_Iterable[str]] = ..., embedding: _Optional[_Union[_embedding_pb2.Embedding, _Mapping]] = ...) -> None: ...

class IngestBulkRequest(_message.Message):
    __slots__ = ["project_id", "data_collection_id", "split_id", "model_id", "points", "options_hash"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    SPLIT_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_HASH_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    data_collection_id: str
    split_id: str
    model_id: str
    points: _containers.RepeatedCompositeFieldContainer[BulkPoint]
    options_hash: str
    def __init__(self, project_id: _Optional[str] = ..., data_collection_id: _Optional[str] = ..., split_id: _Optional[str] = ..., model_id: _Optional[str] = ..., points: _Optional[_Iterable[_Union[BulkPoint, _Mapping]]] = ..., options_hash: _Optional[str] = ...) -> None: ...

class IngestBulkResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class IngestMetricRequest(_message.Message):
    __slots__ = ["project_id", "model_id", "timestamp", "metrics", "point_id"]
    class MetricsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float
        def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    POINT_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    model_id: str
    timestamp: str
    metrics: _containers.ScalarMap[str, float]
    point_id: str
    def __init__(self, project_id: _Optional[str] = ..., model_id: _Optional[str] = ..., timestamp: _Optional[str] = ..., metrics: _Optional[_Mapping[str, float]] = ..., point_id: _Optional[str] = ...) -> None: ...

class IngestMetricResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
