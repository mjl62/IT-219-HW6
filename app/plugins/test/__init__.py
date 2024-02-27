from app.command import Command

class TestCommand(Command):

    def execute():
        print("Test Command Executed")

    def menuText() -> str:
        return "Example command for testing implementation."