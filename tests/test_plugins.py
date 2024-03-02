from multiprocessing import Queue
import os
from app.plugins.add import AddCommand
from app.plugins.menu import MenuCommand


queue = Queue()

def test_add(capfd):
    AddCommand.execute([12, 12], queue)
    captured = capfd.readouterr()
    assert int(queue.get()) == 0\
    and int(captured.out[0:2]) == 24\
    and str(AddCommand.menuText())\
    and str(AddCommand.usage())
