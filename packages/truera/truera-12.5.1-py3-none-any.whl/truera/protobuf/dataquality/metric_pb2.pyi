from truera.protobuf.dataquality import statistics_pb2 as _statistics_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MetricDefinition(_message.Message):
    __slots__ = ["metric_id", "metric_type_short_name", "metric_short_name", "metric_type_friendly_name", "metric_friendly_name", "scope_type", "column_name", "metric_type", "value_constraint"]
    class ScopeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNDEFINED_METRIC_SCOPE_TYPE: _ClassVar[MetricDefinition.ScopeType]
        TABLE: _ClassVar[MetricDefinition.ScopeType]
        COLUMN: _ClassVar[MetricDefinition.ScopeType]
    UNDEFINED_METRIC_SCOPE_TYPE: MetricDefinition.ScopeType
    TABLE: MetricDefinition.ScopeType
    COLUMN: MetricDefinition.ScopeType
    class MetricType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNDEFINED: _ClassVar[MetricDefinition.MetricType]
        ROW_COMPLETENESS: _ClassVar[MetricDefinition.MetricType]
        COLUMN_COMPLETENESS: _ClassVar[MetricDefinition.MetricType]
        DATATYPE_MATCH: _ClassVar[MetricDefinition.MetricType]
        UNIQUE_CATEGORICAL_VALUE: _ClassVar[MetricDefinition.MetricType]
        FLOATING_COMPLETENESS: _ClassVar[MetricDefinition.MetricType]
        FLOATING_FINITENESS: _ClassVar[MetricDefinition.MetricType]
        NUMERIC_VALUE_IN_RANGE: _ClassVar[MetricDefinition.MetricType]
    UNDEFINED: MetricDefinition.MetricType
    ROW_COMPLETENESS: MetricDefinition.MetricType
    COLUMN_COMPLETENESS: MetricDefinition.MetricType
    DATATYPE_MATCH: MetricDefinition.MetricType
    UNIQUE_CATEGORICAL_VALUE: MetricDefinition.MetricType
    FLOATING_COMPLETENESS: MetricDefinition.MetricType
    FLOATING_FINITENESS: MetricDefinition.MetricType
    NUMERIC_VALUE_IN_RANGE: MetricDefinition.MetricType
    class ValueConstraint(_message.Message):
        __slots__ = ["required_columns", "data_type", "numeric_range", "allowed_string_values"]
        class NumericRange(_message.Message):
            __slots__ = ["min_value", "max_value"]
            MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
            MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
            min_value: float
            max_value: float
            def __init__(self, min_value: _Optional[float] = ..., max_value: _Optional[float] = ...) -> None: ...
        REQUIRED_COLUMNS_FIELD_NUMBER: _ClassVar[int]
        DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
        NUMERIC_RANGE_FIELD_NUMBER: _ClassVar[int]
        ALLOWED_STRING_VALUES_FIELD_NUMBER: _ClassVar[int]
        required_columns: _containers.RepeatedScalarFieldContainer[str]
        data_type: _statistics_pb2.ColumnStatistics.DataType
        numeric_range: MetricDefinition.ValueConstraint.NumericRange
        allowed_string_values: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, required_columns: _Optional[_Iterable[str]] = ..., data_type: _Optional[_Union[_statistics_pb2.ColumnStatistics.DataType, str]] = ..., numeric_range: _Optional[_Union[MetricDefinition.ValueConstraint.NumericRange, _Mapping]] = ..., allowed_string_values: _Optional[_Iterable[str]] = ...) -> None: ...
    METRIC_ID_FIELD_NUMBER: _ClassVar[int]
    METRIC_TYPE_SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    METRIC_SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    METRIC_TYPE_FRIENDLY_NAME_FIELD_NUMBER: _ClassVar[int]
    METRIC_FRIENDLY_NAME_FIELD_NUMBER: _ClassVar[int]
    SCOPE_TYPE_FIELD_NUMBER: _ClassVar[int]
    COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    METRIC_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    metric_id: str
    metric_type_short_name: str
    metric_short_name: str
    metric_type_friendly_name: str
    metric_friendly_name: str
    scope_type: MetricDefinition.ScopeType
    column_name: str
    metric_type: MetricDefinition.MetricType
    value_constraint: MetricDefinition.ValueConstraint
    def __init__(self, metric_id: _Optional[str] = ..., metric_type_short_name: _Optional[str] = ..., metric_short_name: _Optional[str] = ..., metric_type_friendly_name: _Optional[str] = ..., metric_friendly_name: _Optional[str] = ..., scope_type: _Optional[_Union[MetricDefinition.ScopeType, str]] = ..., column_name: _Optional[str] = ..., metric_type: _Optional[_Union[MetricDefinition.MetricType, str]] = ..., value_constraint: _Optional[_Union[MetricDefinition.ValueConstraint, _Mapping]] = ...) -> None: ...

class MetricResult(_message.Message):
    __slots__ = ["metric_id", "split_id", "feature_name", "metric_type", "compliance_count", "compliance_ratio", "violation_count", "violation_ratio"]
    METRIC_ID_FIELD_NUMBER: _ClassVar[int]
    SPLIT_ID_FIELD_NUMBER: _ClassVar[int]
    FEATURE_NAME_FIELD_NUMBER: _ClassVar[int]
    METRIC_TYPE_FIELD_NUMBER: _ClassVar[int]
    COMPLIANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMPLIANCE_RATIO_FIELD_NUMBER: _ClassVar[int]
    VIOLATION_COUNT_FIELD_NUMBER: _ClassVar[int]
    VIOLATION_RATIO_FIELD_NUMBER: _ClassVar[int]
    metric_id: str
    split_id: str
    feature_name: str
    metric_type: MetricDefinition.MetricType
    compliance_count: int
    compliance_ratio: float
    violation_count: int
    violation_ratio: float
    def __init__(self, metric_id: _Optional[str] = ..., split_id: _Optional[str] = ..., feature_name: _Optional[str] = ..., metric_type: _Optional[_Union[MetricDefinition.MetricType, str]] = ..., compliance_count: _Optional[int] = ..., compliance_ratio: _Optional[float] = ..., violation_count: _Optional[int] = ..., violation_ratio: _Optional[float] = ...) -> None: ...
