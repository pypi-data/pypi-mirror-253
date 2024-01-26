from enum import Enum


class PlatformServiceKeys:
    PLATFORM_API_KEY = "PLATFORM_SERVICE_API_KEY"
    PLATFORM_HOST = "PLATFORM_SERVICE_HOST"
    PLATFORM_PORT = "PLATFORM_SERVICE_PORT"


class ConnectorKeys:
    ID = "id"
    PROJECT_ID = "project_id"
    CONNECTOR_ID = "connector_id"
    TOOL_INSTANCE_ID = "tool_instance_id"
    CONNECTOR_METADATA = "connector_metadata"
    CONNECTOR_TYPE = "connector_type"


class AdapterKeys:
    ADAPTER_INSTANCE_ID = "adapter_instance_id"


class PromptStudioKeys:
    PROMPT_REGISTRY_ID = "prompt_registry_id"


class ConnectorType:
    INPUT = "INPUT"
    OUTPUT = "OUTPUT"


class LogType:
    LOG = "LOG"
    UPDATE = "UPDATE"


class LogStage:
    TOOL_RUN = "TOOL_RUN"


class LogState:
    """State of logs INPUT_UPDATE tag for update the FE input component
    OUTPUT_UPDATE tag for update the FE output component."""

    INPUT_UPDATE = "INPUT_UPDATE"
    OUTPUT_UPDATE = "OUTPUT_UPDATE"


class Connector:
    FILE_SYSTEM = "FILE_SYSTEM"
    DATABASE = "DATABASE"


class Command:
    SPEC = "SPEC"
    PROPERTIES = "PROPERTIES"
    ICON = "ICON"
    RUN = "RUN"
    VARIABLES = "VARIABLES"

    @classmethod
    def static_commands(cls) -> set[str]:
        return {cls.SPEC, cls.PROPERTIES, cls.ICON, cls.VARIABLES}


class UsageType:
    LLM_COMPLETE = "LLM_COMPLETE"
    RAG = "RAG"
    INDEXER = "INDEXER"


class LogLevel(Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"
    FATAL = "FATAL"
