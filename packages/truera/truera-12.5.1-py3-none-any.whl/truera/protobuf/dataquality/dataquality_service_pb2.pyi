from google.api import annotations_pb2 as _annotations_pb2
from truera.protobuf.dataquality import rule_pb2 as _rule_pb2
from truera.protobuf.dataquality import metric_pb2 as _metric_pb2
from truera.protobuf.dataquality import statistics_pb2 as _statistics_pb2
from truera.protobuf.dataquality import computation_pb2 as _computation_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetAllRuleDefinitionsRequest(_message.Message):
    __slots__ = ["project_id", "data_collection_id"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    data_collection_id: str
    def __init__(self, project_id: _Optional[str] = ..., data_collection_id: _Optional[str] = ...) -> None: ...

class GetAllRuleDefinitionsResponse(_message.Message):
    __slots__ = ["rule_definition", "computation_status", "compute_operation_id"]
    RULE_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    COMPUTATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    rule_definition: _containers.RepeatedCompositeFieldContainer[_rule_pb2.RuleDefinition]
    computation_status: _computation_pb2.DataQualityComputationStatus
    compute_operation_id: str
    def __init__(self, rule_definition: _Optional[_Iterable[_Union[_rule_pb2.RuleDefinition, _Mapping]]] = ..., computation_status: _Optional[_Union[_computation_pb2.DataQualityComputationStatus, str]] = ..., compute_operation_id: _Optional[str] = ...) -> None: ...

class RuleDefinitionConstraint(_message.Message):
    __slots__ = ["match_type", "operator", "violation_threshold", "violation_threshold_range"]
    MATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    VIOLATION_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    VIOLATION_THRESHOLD_RANGE_FIELD_NUMBER: _ClassVar[int]
    match_type: _rule_pb2.RuleDefinition.MatchType
    operator: _rule_pb2.RuleDefinition.Operator
    violation_threshold: float
    violation_threshold_range: _metric_pb2.MetricDefinition.ValueConstraint.NumericRange
    def __init__(self, match_type: _Optional[_Union[_rule_pb2.RuleDefinition.MatchType, str]] = ..., operator: _Optional[_Union[_rule_pb2.RuleDefinition.Operator, str]] = ..., violation_threshold: _Optional[float] = ..., violation_threshold_range: _Optional[_Union[_metric_pb2.MetricDefinition.ValueConstraint.NumericRange, _Mapping]] = ...) -> None: ...

class UpdateRuleDefinitionRequest(_message.Message):
    __slots__ = ["project_id", "data_collection_id", "rule_id", "updated_constraint"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATED_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    data_collection_id: str
    rule_id: str
    updated_constraint: RuleDefinitionConstraint
    def __init__(self, project_id: _Optional[str] = ..., data_collection_id: _Optional[str] = ..., rule_id: _Optional[str] = ..., updated_constraint: _Optional[_Union[RuleDefinitionConstraint, _Mapping]] = ...) -> None: ...

class UpdateRuleDefinitionResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MetricDefinitionConstraint(_message.Message):
    __slots__ = ["scope_type", "column_name", "metric_type", "updated_value_constraint"]
    SCOPE_TYPE_FIELD_NUMBER: _ClassVar[int]
    COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    METRIC_TYPE_FIELD_NUMBER: _ClassVar[int]
    UPDATED_VALUE_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    scope_type: _metric_pb2.MetricDefinition.ScopeType
    column_name: str
    metric_type: _metric_pb2.MetricDefinition.MetricType
    updated_value_constraint: _metric_pb2.MetricDefinition.ValueConstraint
    def __init__(self, scope_type: _Optional[_Union[_metric_pb2.MetricDefinition.ScopeType, str]] = ..., column_name: _Optional[str] = ..., metric_type: _Optional[_Union[_metric_pb2.MetricDefinition.MetricType, str]] = ..., updated_value_constraint: _Optional[_Union[_metric_pb2.MetricDefinition.ValueConstraint, _Mapping]] = ...) -> None: ...

class UpdateMetricDefinitionRequest(_message.Message):
    __slots__ = ["project_id", "data_collection_id", "rule_id", "metric_id", "updated_constraint"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    METRIC_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATED_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    data_collection_id: str
    rule_id: str
    metric_id: str
    updated_constraint: MetricDefinitionConstraint
    def __init__(self, project_id: _Optional[str] = ..., data_collection_id: _Optional[str] = ..., rule_id: _Optional[str] = ..., metric_id: _Optional[str] = ..., updated_constraint: _Optional[_Union[MetricDefinitionConstraint, _Mapping]] = ...) -> None: ...

class UpdateMetricDefinitionResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetSplitRuleEvaluationResultsRequest(_message.Message):
    __slots__ = ["project_id", "data_collection_id", "split_id"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    SPLIT_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    data_collection_id: str
    split_id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, project_id: _Optional[str] = ..., data_collection_id: _Optional[str] = ..., split_id: _Optional[_Iterable[str]] = ...) -> None: ...

class GetSplitRuleEvaluationResultsResponse(_message.Message):
    __slots__ = ["split_rule_evaluation_result"]
    SPLIT_RULE_EVALUATION_RESULT_FIELD_NUMBER: _ClassVar[int]
    split_rule_evaluation_result: _containers.RepeatedCompositeFieldContainer[SplitRuleEvaluationResult]
    def __init__(self, split_rule_evaluation_result: _Optional[_Iterable[_Union[SplitRuleEvaluationResult, _Mapping]]] = ...) -> None: ...

class SplitRuleEvaluationResult(_message.Message):
    __slots__ = ["split_id", "rule_evaluation_result", "row_count", "computation_status", "compute_operation_id"]
    SPLIT_ID_FIELD_NUMBER: _ClassVar[int]
    RULE_EVALUATION_RESULT_FIELD_NUMBER: _ClassVar[int]
    ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMPUTATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    split_id: str
    rule_evaluation_result: _containers.RepeatedCompositeFieldContainer[_rule_pb2.RuleEvaluationResult]
    row_count: int
    computation_status: _computation_pb2.DataQualityComputationStatus
    compute_operation_id: str
    def __init__(self, split_id: _Optional[str] = ..., rule_evaluation_result: _Optional[_Iterable[_Union[_rule_pb2.RuleEvaluationResult, _Mapping]]] = ..., row_count: _Optional[int] = ..., computation_status: _Optional[_Union[_computation_pb2.DataQualityComputationStatus, str]] = ..., compute_operation_id: _Optional[str] = ...) -> None: ...

class GetSplitStatisticsRequest(_message.Message):
    __slots__ = ["project_id", "data_collection_id", "split_id"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    SPLIT_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    data_collection_id: str
    split_id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, project_id: _Optional[str] = ..., data_collection_id: _Optional[str] = ..., split_id: _Optional[_Iterable[str]] = ...) -> None: ...

class GetSplitStatisticsResponse(_message.Message):
    __slots__ = ["split_statistics", "computation_status", "compute_operation_id"]
    SPLIT_STATISTICS_FIELD_NUMBER: _ClassVar[int]
    COMPUTATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    split_statistics: _containers.RepeatedCompositeFieldContainer[_statistics_pb2.DataSplitStatistics]
    computation_status: _computation_pb2.DataQualityComputationStatus
    compute_operation_id: str
    def __init__(self, split_statistics: _Optional[_Iterable[_Union[_statistics_pb2.DataSplitStatistics, _Mapping]]] = ..., computation_status: _Optional[_Union[_computation_pb2.DataQualityComputationStatus, str]] = ..., compute_operation_id: _Optional[str] = ...) -> None: ...

class GenerateRuleDefinitionFromSplitRequest(_message.Message):
    __slots__ = ["project_id", "data_collection_id", "split_id", "overwrite_existing_rule"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    SPLIT_ID_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_EXISTING_RULE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    data_collection_id: str
    split_id: str
    overwrite_existing_rule: bool
    def __init__(self, project_id: _Optional[str] = ..., data_collection_id: _Optional[str] = ..., split_id: _Optional[str] = ..., overwrite_existing_rule: bool = ...) -> None: ...

class GenerateRuleDefinitionFromSplitResponse(_message.Message):
    __slots__ = ["warning", "rule_definition", "computation_status", "compute_operation_id"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNDEFINED_STATUS: _ClassVar[GenerateRuleDefinitionFromSplitResponse.Status]
        SUCCESS: _ClassVar[GenerateRuleDefinitionFromSplitResponse.Status]
        ERROR_RULES_EXIST: _ClassVar[GenerateRuleDefinitionFromSplitResponse.Status]
    UNDEFINED_STATUS: GenerateRuleDefinitionFromSplitResponse.Status
    SUCCESS: GenerateRuleDefinitionFromSplitResponse.Status
    ERROR_RULES_EXIST: GenerateRuleDefinitionFromSplitResponse.Status
    WARNING_FIELD_NUMBER: _ClassVar[int]
    RULE_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    COMPUTATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    warning: str
    rule_definition: _containers.RepeatedCompositeFieldContainer[_rule_pb2.RuleDefinition]
    computation_status: _computation_pb2.DataQualityComputationStatus
    compute_operation_id: str
    def __init__(self, warning: _Optional[str] = ..., rule_definition: _Optional[_Iterable[_Union[_rule_pb2.RuleDefinition, _Mapping]]] = ..., computation_status: _Optional[_Union[_computation_pb2.DataQualityComputationStatus, str]] = ..., compute_operation_id: _Optional[str] = ...) -> None: ...

class CheckRuleDefinitionExistsRequest(_message.Message):
    __slots__ = ["project_id", "data_collection_id"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    data_collection_id: str
    def __init__(self, project_id: _Optional[str] = ..., data_collection_id: _Optional[str] = ...) -> None: ...

class CheckRuleDefinitionExistsResponse(_message.Message):
    __slots__ = ["rules_exist"]
    RULES_EXIST_FIELD_NUMBER: _ClassVar[int]
    rules_exist: bool
    def __init__(self, rules_exist: bool = ...) -> None: ...

class CheckComputationStatusRequest(_message.Message):
    __slots__ = ["compute_operation_id"]
    COMPUTE_OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    compute_operation_id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, compute_operation_id: _Optional[_Iterable[str]] = ...) -> None: ...

class CheckComputationStatusResponse(_message.Message):
    __slots__ = ["computation_status_entry"]
    COMPUTATION_STATUS_ENTRY_FIELD_NUMBER: _ClassVar[int]
    computation_status_entry: _containers.RepeatedCompositeFieldContainer[ComputationStatusEntry]
    def __init__(self, computation_status_entry: _Optional[_Iterable[_Union[ComputationStatusEntry, _Mapping]]] = ...) -> None: ...

class ComputationStatusEntry(_message.Message):
    __slots__ = ["computation_status", "compute_operation_id"]
    COMPUTATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    computation_status: _computation_pb2.DataQualityComputationStatus
    compute_operation_id: str
    def __init__(self, computation_status: _Optional[_Union[_computation_pb2.DataQualityComputationStatus, str]] = ..., compute_operation_id: _Optional[str] = ...) -> None: ...
