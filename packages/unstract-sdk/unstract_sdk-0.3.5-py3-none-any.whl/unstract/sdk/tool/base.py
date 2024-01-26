import datetime
from abc import ABC, abstractmethod
from typing import Any

from unstract.sdk.constants import LogLevel
from unstract.sdk.tool.parser import ToolArgsParser
from unstract.sdk.tool.stream import StreamableBaseTool


class UnstractAbstractTool(ABC, StreamableBaseTool):
    """Abstract class for Unstract tools."""

    def __init__(self, log_level: str = LogLevel.INFO) -> None:
        """Creates an UnstractTool.

        Args:
            log_level (str): Log level for the tool
                Can be one of INFO, DEBUG, WARN, ERROR, FATAL.
        """
        self.start_time = datetime.datetime.now()
        self.workflow_id = ""
        self.execution_id = ""
        super().__init__(log_level=log_level)

    def elapsed_time(self) -> float:
        """Returns the elapsed time since the tool was created."""
        return (datetime.datetime.now() - self.start_time).total_seconds()

    @classmethod
    def from_tool_args(cls, args: list[str]) -> "UnstractAbstractTool":
        """Builder method to create a tool from args passed to a tool.

        Refer the tool's README to know more about the possible args

        Args:
            args (List[str]): Arguments passed to a tool

        Returns:
            UnstractAbstractTool: Abstract base tool class
        """
        log_level = ToolArgsParser.get_log_level(args)
        return cls(log_level=log_level)

    @abstractmethod
    def run(
        self,
        params: dict[str, Any],
        settings: dict[str, Any],
        workflow_id: str,
        execution_id: str,
    ) -> None:
        """Implements RUN command for the tool.

        Args:
            params (dict[str, Any]): Params for the tool
            settings (dict[str, Any]): Settings for the tool
            workflow_id (str): Project GUID used during workflow execution
        """
        pass
