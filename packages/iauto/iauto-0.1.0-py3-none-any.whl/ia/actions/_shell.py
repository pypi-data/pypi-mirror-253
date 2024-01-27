import os
import sys
import json
from typing import Any, Dict
from ._action import Action, ActionDef

from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

_platform = sys.platform
_env = {
    "SHELL": os.environ.get("SHELL"),
    "USER": os.environ.get("USER"),
    "HOME": os.environ.get("HOME"),
    "PWD": os.environ.get("PWD")
}

_definition = ActionDef.from_dict({
    "name": "shell_command",
    "description": f"""
Use this tool to execute Linux, macOS, and DOS commands and output the execution results.

Current OS: {_platform}
System Environments: {json.dumps(dict(_env), indent=4)}

Examples:
1. Get weather of beijing: curl -s https://wttr.in/beijing
2. open document: open {os.environ.get('HOME')}/Documents/Plans.docx
3. open website: open https://bing.com
    """,
    "arguments": [
        {
            "name": "command",
            "type": "string",
            "description": "Command and arguments",
            "required": True
        }
    ]
})


class ShellCommandAction(Action):
    def definition(self) -> ActionDef:
        return _definition

    def perform(self, **kwargs: Any) -> Any:
        cmd = kwargs.get('command')

        try:
            with os.popen(cmd=cmd) as p:
                return p.read()
        except Exception as e:
            return f"Execute `{cmd}` failed: {e}"


class PromptAction(Action):
    def __init__(self) -> None:
        super().__init__()
        self._history = InMemoryHistory()

    def definition(self) -> ActionDef:
        return super().definition()

    def perform(self, **args: Any) -> Dict:
        p = prompt("Human: ", history=self._history, auto_suggest=AutoSuggestFromHistory())
        return {"prompt": p}


class PrintAction(Action):
    def definition(self) -> ActionDef:
        return super().definition()

    def perform(self, message, begin=None, end="\n", **args: Any) -> Dict:
        if begin:
            print(begin, end='')
        print(message, end=end)
