import sys
from typing import Any

from unstract.sdk.tool.base import UnstractAbstractTool
from unstract.sdk.tool.entrypoint import ToolEntrypoint


# TODO: Rename tool's class
class ConcreteTool(UnstractAbstractTool):
    def run(
        self, params: dict[str, Any], settings: dict[str, Any], workflow_id: str
    ) -> None:
        # -------------- TODO: Add your code here ----------------
        return None


if __name__ == "__main__":
    args = sys.argv[1:]
    # TODO: Rename tool's class
    tool = ConcreteTool.from_tool_args(args=args)
    ToolEntrypoint.launch(tool=tool, args=args)
