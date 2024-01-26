import argparse
from typing import Optional

from dotenv import find_dotenv
from unstract.sdk.constants import LogLevel


class ToolArgsParser:
    """Class to help with parsing arguments to a tool."""

    @staticmethod
    def parse_args(args_to_parse: list[str]) -> argparse.Namespace:
        """Helps parse arguments to a tool.

        Args:
            args_to_parse (List[str]): Command line arguments received by a tool

        Returns:
            argparse.Namespace: Parsed arguments
        """
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--command", type=str, help="Command to execute", required=True
        )
        parser.add_argument(
            "--params",
            type=str,
            help="Parameters to use in RUN command",
            required=False,
        )
        parser.add_argument(
            "--settings", type=str, help="Settings to be used", required=False
        )
        parser.add_argument(
            "--workflow-id", type=str, help="Project GUID", required=False
        )
        parser.add_argument(
            "--execution-id", type=str, help="Execution Id", required=False
        )
        parser.add_argument(
            "--log-level",
            type=LogLevel,
            help="Log level",
            required=False,
            default=LogLevel.ERROR,
        )
        parser.add_argument(
            "--env",
            type=str,
            help="Env file to load environment from",
            required=False,
            default=find_dotenv(usecwd=True),
        )
        return parser.parse_args(args_to_parse)

    @classmethod
    def get_log_level(cls, args: list[str]) -> Optional[str]:
        """Returns the log level for a tool.

        If its not present in the parsed arguments, `None` is returned.

        Args:
            args (List[str]): Command line arguments received by a tool

        Returns:
            Optional[str]: Log level of either INFO, DEBUG, WARN, ERROR,
              FATAL if present in the args. Otherwise returns `None`.
        """
        parsed_args = cls.parse_args(args)
        if hasattr(parsed_args, "log_level"):
            return parsed_args.log_level
        return None
