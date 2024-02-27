from app.command import Command
from typing import List
import os
import signal
from multiprocessing import Queue

class ExitCommand(Command):
    
    def execute(args: List, queue: Queue):
        # exit main program thread
        queue.put("EXITCODE_0")

    def menuText() -> str:
        return "Exit the application"