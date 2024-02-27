from app.command import Command
from typing import List

class TestCommand(Command):

    def execute(args: List):
        print("Test Command Executed")

    def menuText() -> str:
        return "Example command for testing implementation."