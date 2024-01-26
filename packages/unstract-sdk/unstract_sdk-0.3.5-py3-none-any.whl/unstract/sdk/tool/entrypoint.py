from unstract.sdk.tool.base import UnstractAbstractTool
from unstract.sdk.tool.executor import ToolExecutor
from unstract.sdk.tool.parser import ToolArgsParser


class ToolEntrypoint:
    """Class that contains methods for the entrypoint for a tool."""

    @staticmethod
    def launch(tool: UnstractAbstractTool, args: list[str]) -> None:
        """Entrypoint function for a tool.

        It parses the arguments passed to a tool and executes
        the intended command.

        Args:
            tool (UnstractAbstractTool): Tool to execute
            args (List[str]): Arguments passed to a tool
        """
        executor = ToolExecutor(tool=tool)
        parsed_args = ToolArgsParser.parse_args(args)
        executor.execute(parsed_args)
