from app.command import Command
from typing import List
from multiprocessing import Queue

class ArgCommand(Command):

    def execute(args: List, queue: Queue):
        queue.put(0)
        print(f"args: {args}")

    def menuText() -> str:
        return "Debugging plugin for testing args functionality"