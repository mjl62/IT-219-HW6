from app.command import Command
from typing import List
import os

class MenuCommand(Command):

    def execute(args: List):
        print(os.environ["HELP_MENU"])

    def menuText() -> str:
        return "Prints all currently loaded commands and some information about them"

    