from app.command import Command
from typing import List
from multiprocessing import Queue

class TestCommand(Command):

    def execute(args: List, queue: Queue):
        queue.put(0)
        print("Test Command Executed")

    def menuText() -> str:
        return "Example command for testing implementation."