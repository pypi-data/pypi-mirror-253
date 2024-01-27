from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DataSplitStatistics(_message.Message):
    __slots__ = ["split_id", "common_statistics", "column_statistics"]
    class ColumnStatisticsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ColumnStatistics
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ColumnStatistics, _Mapping]] = ...) -> None: ...
    SPLIT_ID_FIELD_NUMBER: _ClassVar[int]
    COMMON_STATISTICS_FIELD_NUMBER: _ClassVar[int]
    COLUMN_STATISTICS_FIELD_NUMBER: _ClassVar[int]
    split_id: str
    common_statistics: CommonStatistics
    column_statistics: _containers.MessageMap[str, ColumnStatistics]
    def __init__(self, split_id: _Optional[str] = ..., common_statistics: _Optional[_Union[CommonStatistics, _Mapping]] = ..., column_statistics: _Optional[_Mapping[str, ColumnStatistics]] = ...) -> None: ...

class ColumnStatistics(_message.Message):
    __slots__ = ["column_name", "data_type", "num_stats", "string_stats"]
    class DataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNDEFINED_DATA_TYPE: _ClassVar[ColumnStatistics.DataType]
        BOOLEAN: _ClassVar[ColumnStatistics.DataType]
        INTEGRAL: _ClassVar[ColumnStatistics.DataType]
        FRACTIONAL: _ClassVar[ColumnStatistics.DataType]
        CATEGORICAL: _ClassVar[ColumnStatistics.DataType]
    UNDEFINED_DATA_TYPE: ColumnStatistics.DataType
    BOOLEAN: ColumnStatistics.DataType
    INTEGRAL: ColumnStatistics.DataType
    FRACTIONAL: ColumnStatistics.DataType
    CATEGORICAL: ColumnStatistics.DataType
    COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    NUM_STATS_FIELD_NUMBER: _ClassVar[int]
    STRING_STATS_FIELD_NUMBER: _ClassVar[int]
    column_name: str
    data_type: ColumnStatistics.DataType
    num_stats: NumericStatistics
    string_stats: StringStatistics
    def __init__(self, column_name: _Optional[str] = ..., data_type: _Optional[_Union[ColumnStatistics.DataType, str]] = ..., num_stats: _Optional[_Union[NumericStatistics, _Mapping]] = ..., string_stats: _Optional[_Union[StringStatistics, _Mapping]] = ...) -> None: ...

class CommonStatistics(_message.Message):
    __slots__ = ["num_non_missing", "num_missing"]
    NUM_NON_MISSING_FIELD_NUMBER: _ClassVar[int]
    NUM_MISSING_FIELD_NUMBER: _ClassVar[int]
    num_non_missing: int
    num_missing: int
    def __init__(self, num_non_missing: _Optional[int] = ..., num_missing: _Optional[int] = ...) -> None: ...

class NumericStatistics(_message.Message):
    __slots__ = ["common_statistics", "mean", "std_dev", "min", "max", "value_range_1_std_dev_ratio", "value_range_2_std_dev_ratio", "value_range_3_std_dev_ratio", "quantiles", "num_infinity_ratio", "num_nan_ratio", "num_real_number_ratio"]
    class Quantile(_message.Message):
        __slots__ = ["quantile", "value"]
        QUANTILE_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        quantile: float
        value: float
        def __init__(self, quantile: _Optional[float] = ..., value: _Optional[float] = ...) -> None: ...
    COMMON_STATISTICS_FIELD_NUMBER: _ClassVar[int]
    MEAN_FIELD_NUMBER: _ClassVar[int]
    STD_DEV_FIELD_NUMBER: _ClassVar[int]
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    VALUE_RANGE_1_STD_DEV_RATIO_FIELD_NUMBER: _ClassVar[int]
    VALUE_RANGE_2_STD_DEV_RATIO_FIELD_NUMBER: _ClassVar[int]
    VALUE_RANGE_3_STD_DEV_RATIO_FIELD_NUMBER: _ClassVar[int]
    QUANTILES_FIELD_NUMBER: _ClassVar[int]
    NUM_INFINITY_RATIO_FIELD_NUMBER: _ClassVar[int]
    NUM_NAN_RATIO_FIELD_NUMBER: _ClassVar[int]
    NUM_REAL_NUMBER_RATIO_FIELD_NUMBER: _ClassVar[int]
    common_statistics: CommonStatistics
    mean: float
    std_dev: float
    min: float
    max: float
    value_range_1_std_dev_ratio: float
    value_range_2_std_dev_ratio: float
    value_range_3_std_dev_ratio: float
    quantiles: _containers.RepeatedCompositeFieldContainer[NumericStatistics.Quantile]
    num_infinity_ratio: float
    num_nan_ratio: float
    num_real_number_ratio: float
    def __init__(self, common_statistics: _Optional[_Union[CommonStatistics, _Mapping]] = ..., mean: _Optional[float] = ..., std_dev: _Optional[float] = ..., min: _Optional[float] = ..., max: _Optional[float] = ..., value_range_1_std_dev_ratio: _Optional[float] = ..., value_range_2_std_dev_ratio: _Optional[float] = ..., value_range_3_std_dev_ratio: _Optional[float] = ..., quantiles: _Optional[_Iterable[_Union[NumericStatistics.Quantile, _Mapping]]] = ..., num_infinity_ratio: _Optional[float] = ..., num_nan_ratio: _Optional[float] = ..., num_real_number_ratio: _Optional[float] = ...) -> None: ...

class StringStatistics(_message.Message):
    __slots__ = ["common_statistics", "values"]
    COMMON_STATISTICS_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    common_statistics: CommonStatistics
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, common_statistics: _Optional[_Union[CommonStatistics, _Mapping]] = ..., values: _Optional[_Iterable[str]] = ...) -> None: ...

class BooleanStatistics(_message.Message):
    __slots__ = ["common_statistics"]
    COMMON_STATISTICS_FIELD_NUMBER: _ClassVar[int]
    common_statistics: CommonStatistics
    def __init__(self, common_statistics: _Optional[_Union[CommonStatistics, _Mapping]] = ...) -> None: ...

class SplitStatisticsRecord(_message.Message):
    __slots__ = ["id", "split_statistics"]
    ID_FIELD_NUMBER: _ClassVar[int]
    SPLIT_STATISTICS_FIELD_NUMBER: _ClassVar[int]
    id: str
    split_statistics: DataSplitStatistics
    def __init__(self, id: _Optional[str] = ..., split_statistics: _Optional[_Union[DataSplitStatistics, _Mapping]] = ...) -> None: ...
