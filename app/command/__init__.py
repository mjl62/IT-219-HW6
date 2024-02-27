from abc import ABC, abstractmethod

class Command(ABC):

    @abstractmethod
    def execute():
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

    def runCommand(self, command_name: str):
        try:
            self.commands[command_name].execute()
        except KeyError:
            print("Unknown command: '" + command_name + "'")
    
