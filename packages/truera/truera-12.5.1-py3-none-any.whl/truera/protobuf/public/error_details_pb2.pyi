from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorDetails(_message.Message):
    __slots__ = ["trace_id", "source_service", "model_runner_job_id"]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SERVICE_FIELD_NUMBER: _ClassVar[int]
    MODEL_RUNNER_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    trace_id: str
    source_service: str
    model_runner_job_id: str
    def __init__(self, trace_id: _Optional[str] = ..., source_service: _Optional[str] = ..., model_runner_job_id: _Optional[str] = ...) -> None: ...
