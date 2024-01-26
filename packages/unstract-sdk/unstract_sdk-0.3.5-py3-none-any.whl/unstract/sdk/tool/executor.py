import argparse
from json import JSONDecodeError, loads
from typing import Any, Optional

from dotenv import load_dotenv
from jsonschema import ValidationError, validate
from unstract.sdk.constants import Command
from unstract.sdk.tool.base import UnstractAbstractTool


class ToolExecutor:
    """Takes care of executing a tool's intended command."""

    def __init__(self, tool: UnstractAbstractTool) -> None:
        self.tool = tool

    @staticmethod
    def load_environment(path: Optional[str] = None) -> None:
        """Loads env variables with python-dotenv.

        Args:
            path (Optional[str], optional): Path to the env file to load.
                Defaults to None.
        """
        if path is None:
            load_dotenv()
        else:
            load_dotenv(path)

    def validate_and_get_settings(
        self, args: argparse.Namespace
    ) -> dict[str, Any]:
        """Validates and obtains settings for a tool.

        Validation is done against the tool's settings based
        on its declared SPEC.

        Args:
            args (argparse.Namespace): Parsed arguments for a tool

        Returns:
            dict[str, Any]: Settings JSON for a tool
        """
        settings = {}
        if args.settings is None:
            self.tool.stream_error_and_exit(
                "--settings are required for RUN command"
            )
        try:
            settings = loads(args.settings)
            spec_schema = loads(self.tool.spec())
            validate(instance=settings, schema=spec_schema)
        except JSONDecodeError as e:
            self.tool.stream_error_and_exit(
                f"Settings are not a valid JSON: {str(e)}"
            )
        except ValidationError as e:
            self.tool.stream_error_and_exit(f"Invalid settings: {str(e)}")
        return settings

    def validate_and_get_params(
        self, args: argparse.Namespace
    ) -> dict[str, Any]:
        """Validates and obtains params for a tool.

        Validation is done against the tool's params based
        on its declared PROPERTIES.

        Args:
            args (argparse.Namespace): Parsed arguments for a tool

        Returns:
            dict[str, Any]: Params JSON for a tool
        """
        params = {}
        if args.params is None:
            self.tool.stream_error_and_exit(
                "--params are required for RUN command"
            )
        try:
            params = loads(args.params)
            properties_schema = loads(self.tool.properties())
            # TODO: Use JSON Schema for properties too and then validate
            validate(instance=params, schema=properties_schema)
        except JSONDecodeError as e:
            self.tool.stream_error_and_exit(
                f"Params are not a valid JSON: {str(e)}"
            )
        except ValidationError as e:
            self.tool.stream_error_and_exit(f"Invalid params: {str(e)}")
        return params

    def execute(self, args: argparse.Namespace) -> None:
        """Executes the tool with the passed arguments.

        Args:
            args (argparse.Namespace): Parsed arguments to execute with
        """
        ToolExecutor.load_environment(args.env)
        command = str.upper(args.command)

        if command in Command.static_commands():
            self.tool.handle_static_command(command)
        elif command == Command.RUN:
            params = self.validate_and_get_params(args=args)
            settings = self.validate_and_get_settings(args=args)

            if args.workflow_id is None:
                self.tool.stream_error_and_exit(
                    "--workflow-id is required for RUN command"
                )

            self.tool.stream_log(
                f"Running tool for workflow {args.workflow_id}"
            )
            self.tool.stream_log(
                f"Running tool for execution{args.execution_id}"
            )
            self.tool.run(params, settings, args.workflow_id, args.execution_id)
        else:
            self.tool.stream_error_and_exit("Command not supported")
