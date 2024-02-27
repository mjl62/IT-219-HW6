from app.command import Command
from typing import List
import os
from multiprocessing import Queue

class MenuCommand(Command):

    def execute(args: List, queue: Queue):
        queue.put(0)
        print(os.environ["HELP_MENU"])

    def menuText() -> str:
        return "Prints all currently loaded commands and some information about them"

    