from abc import ABC, abstractmethod
import multiprocessing
from typing import List

class Command(ABC):

    @abstractmethod
    def execute(args: List):
        pass

    @abstractmethod
    def menuText() -> str:
        return "NO_DESCRIPTION_GIVEN"


class CommandHandler:
    def __init__(self):
        self.commands = {}
        self.helpMenu = ""

    def registerCommand(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def createHelpMenu(self):
        for command in self.commands:
            self.helpMenu += f"  {command} ------ {self.commands[command].menuText()}\n"
        return self.helpMenu

    def runCommand(self, command_string: str):
        try:
            command_string = command_string.split()
            command_name = command_string[0]
            self.commands[command_name].execute(command_string[1:])
        except KeyError:
            print("Unknown command: '" + command_name + "'")
    
