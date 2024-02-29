from abc import ABC, abstractmethod
from multiprocessing import Queue, Process
from typing import List

class Command(ABC):

    '''
        executes a command
        takes:
            args - A list of arguments after the command is entered
            queue - Handles communication between main program and processes
    '''
    @abstractmethod
    def execute(args: List, queue: Queue):
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
            queue = Queue()
            command_string = command_string.split()
            command_name = command_string[0]
            # TODO exit command kills thread, figure this out
            process = Process(target=self.commands[command_name].execute, args=[command_string[1:], queue])
            process.start()
            self.checkProcessCode(queue.get())
            process.join()
        except KeyError:
            print("Unknown command: '" + command_name + "'")

    def checkProcessCode(self, process_code):
        if process_code == "EXITCODE_0":
            exit(0)
        elif process_code == "EXITCODE_1":
            exit(1)
    
