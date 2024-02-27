from app.command import Command
from typing import List

class ExitCommand(Command):
    
    def execute(args: List):
        exit()

    def menuText() -> str:
        return "Exit the application"