from app.command import Command
import os

class MenuCommand(Command):

    def execute():
        print(os.environ["HELP_MENU"])

    def menuText() -> str:
        return "Prints all currently loaded commands and some information about them"

    