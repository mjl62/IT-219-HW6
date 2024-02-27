from app.command import Command

class ExitCommand(Command):
    
    def execute():
        exit()

    def menuText() -> str:
        return "Exit the application"