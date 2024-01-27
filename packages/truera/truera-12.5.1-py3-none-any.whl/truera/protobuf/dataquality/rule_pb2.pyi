from truera.protobuf.dataquality import metric_pb2 as _metric_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RuleDefinition(_message.Message):
    __slots__ = ["rule_id", "rule_type_short_name", "rule_short_name", "rule_type_friendly_name", "rule_friendly_name", "metric_definition", "match_type", "operator", "violation_threshold", "violation_threshold_range"]
    class MatchType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNDEFINED_MATCH_TYPE: _ClassVar[RuleDefinition.MatchType]
        COMPLIANCE_COUNT: _ClassVar[RuleDefinition.MatchType]
        COMPLIANCE_RATIO: _ClassVar[RuleDefinition.MatchType]
        VIOLATION_COUNT: _ClassVar[RuleDefinition.MatchType]
        VIOLATION_RATIO: _ClassVar[RuleDefinition.MatchType]
    UNDEFINED_MATCH_TYPE: RuleDefinition.MatchType
    COMPLIANCE_COUNT: RuleDefinition.MatchType
    COMPLIANCE_RATIO: RuleDefinition.MatchType
    VIOLATION_COUNT: RuleDefinition.MatchType
    VIOLATION_RATIO: RuleDefinition.MatchType
    class Operator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNDEFINED_OPERATOR: _ClassVar[RuleDefinition.Operator]
        EQUALS: _ClassVar[RuleDefinition.Operator]
        LESS_THAN: _ClassVar[RuleDefinition.Operator]
        LESS_THAN_OR_EQUAL: _ClassVar[RuleDefinition.Operator]
        GREATER_THAN: _ClassVar[RuleDefinition.Operator]
        GREATER_THAN_OR_EQUAL: _ClassVar[RuleDefinition.Operator]
        IN_RANGE: _ClassVar[RuleDefinition.Operator]
    UNDEFINED_OPERATOR: RuleDefinition.Operator
    EQUALS: RuleDefinition.Operator
    LESS_THAN: RuleDefinition.Operator
    LESS_THAN_OR_EQUAL: RuleDefinition.Operator
    GREATER_THAN: RuleDefinition.Operator
    GREATER_THAN_OR_EQUAL: RuleDefinition.Operator
    IN_RANGE: RuleDefinition.Operator
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    RULE_TYPE_SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    RULE_SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    RULE_TYPE_FRIENDLY_NAME_FIELD_NUMBER: _ClassVar[int]
    RULE_FRIENDLY_NAME_FIELD_NUMBER: _ClassVar[int]
    METRIC_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    MATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    VIOLATION_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    VIOLATION_THRESHOLD_RANGE_FIELD_NUMBER: _ClassVar[int]
    rule_id: str
    rule_type_short_name: str
    rule_short_name: str
    rule_type_friendly_name: str
    rule_friendly_name: str
    metric_definition: _metric_pb2.MetricDefinition
    match_type: RuleDefinition.MatchType
    operator: RuleDefinition.Operator
    violation_threshold: float
    violation_threshold_range: _metric_pb2.MetricDefinition.ValueConstraint.NumericRange
    def __init__(self, rule_id: _Optional[str] = ..., rule_type_short_name: _Optional[str] = ..., rule_short_name: _Optional[str] = ..., rule_type_friendly_name: _Optional[str] = ..., rule_friendly_name: _Optional[str] = ..., metric_definition: _Optional[_Union[_metric_pb2.MetricDefinition, _Mapping]] = ..., match_type: _Optional[_Union[RuleDefinition.MatchType, str]] = ..., operator: _Optional[_Union[RuleDefinition.Operator, str]] = ..., violation_threshold: _Optional[float] = ..., violation_threshold_range: _Optional[_Union[_metric_pb2.MetricDefinition.ValueConstraint.NumericRange, _Mapping]] = ...) -> None: ...

class RuleEvaluationResult(_message.Message):
    __slots__ = ["rule_id", "split_id", "metric_result", "value", "is_violation"]
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    SPLIT_ID_FIELD_NUMBER: _ClassVar[int]
    METRIC_RESULT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    IS_VIOLATION_FIELD_NUMBER: _ClassVar[int]
    rule_id: str
    split_id: str
    metric_result: _metric_pb2.MetricResult
    value: float
    is_violation: bool
    def __init__(self, rule_id: _Optional[str] = ..., split_id: _Optional[str] = ..., metric_result: _Optional[_Union[_metric_pb2.MetricResult, _Mapping]] = ..., value: _Optional[float] = ..., is_violation: bool = ...) -> None: ...

class DataCollectionRuleDefinitionRecord(_message.Message):
    __slots__ = ["id", "project_id", "model_id", "data_collection_id", "split_id", "rule_definition"]
    ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    SPLIT_ID_FIELD_NUMBER: _ClassVar[int]
    RULE_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    id: str
    project_id: str
    model_id: str
    data_collection_id: str
    split_id: str
    rule_definition: _containers.RepeatedCompositeFieldContainer[RuleDefinition]
    def __init__(self, id: _Optional[str] = ..., project_id: _Optional[str] = ..., model_id: _Optional[str] = ..., data_collection_id: _Optional[str] = ..., split_id: _Optional[str] = ..., rule_definition: _Optional[_Iterable[_Union[RuleDefinition, _Mapping]]] = ...) -> None: ...

class SplitRuleEvaluationsResultRecord(_message.Message):
    __slots__ = ["id", "project_id", "data_collection_id", "split_id", "rule_evaluation_result"]
    ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    SPLIT_ID_FIELD_NUMBER: _ClassVar[int]
    RULE_EVALUATION_RESULT_FIELD_NUMBER: _ClassVar[int]
    id: str
    project_id: str
    data_collection_id: str
    split_id: str
    rule_evaluation_result: _containers.RepeatedCompositeFieldContainer[RuleEvaluationResult]
    def __init__(self, id: _Optional[str] = ..., project_id: _Optional[str] = ..., data_collection_id: _Optional[str] = ..., split_id: _Optional[str] = ..., rule_evaluation_result: _Optional[_Iterable[_Union[RuleEvaluationResult, _Mapping]]] = ...) -> None: ...
