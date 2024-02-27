from app.command import Command
from typing import List

class ArgCommand(Command):

    def execute(args: List):
        print(f"args: {args}")

    def menuText() -> str:
        return "Debugging plugin for testing args functionality"