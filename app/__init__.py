# Application
from app.command import CommandHandler, Command
import pkgutil
import importlib
from dotenv import load_dotenv
import os

class App:

    def __init__(self):
        self.commandHandler = CommandHandler()
        if not load_dotenv():
            # do something
            print("No .env file found, running in some mode I havent decided yet")
        self.load_plugins()

    def load_plugins(self):
        # Loads any modules that exist in plugins directory
        plugins_folder = os.environ["PLUGINS_DIRECTORY"]
        for package in pkgutil.iter_modules([plugins_folder]):
            finder, name, ispkg = package
            if (ispkg):
                print(f"Importing Package: {name}...")
                plugin = importlib.import_module(plugins_folder.replace("/", ".") + "." + name)
                for item_name in dir(plugin):
                    item = getattr(plugin, item_name)
                    try:
                        if issubclass(item, (Command, )) and item_name != "Command":
                            self.commandHandler.registerCommand(name, item)
                    except TypeError:
                        continue
        os.environ["HELP_MENU"] = self.commandHandler.createHelpMenu()
        print(os.environ["HELP_MENU"])
        

    def start(self):
        self.commandLoop()

    def commandLoop(self):
        user_in = input(">>> ")
        if not user_in:
            return self.commandLoop()

        self.commandHandler.runCommand(user_in)
        return self.commandLoop()
    