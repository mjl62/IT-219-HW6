# Application
from app.command import CommandHandler, Command
import pkgutil
import importlib
from dotenv import load_dotenv
import os
import logging
from datetime import datetime

class App:

    def __init__(self):
        self.commandHandler = CommandHandler()
        if not load_dotenv():
            # do something
            os.environ['NO_ENV'] = True
            print("No .env file found, running in default mode")    
            os.environ['LOG_DIRECTORY'] = 'logs'
        try:
            os.mkdir(os.environ['LOG_DIRECTORY'])
        except(FileExistsError):
            pass
        # create a logfile named (current date and time)_log.txt
        log_timestamp = datetime.now().strftime("%m%d%Y_%H%M%S")
        os.environ['LOG_FILE'] = f"{os.environ['LOG_DIRECTORY']}/{log_timestamp}_log.txt"
        logging.basicConfig(filename=(os.environ['LOG_FILE']), level=logging.DEBUG)
        self.load_plugins()

    def load_plugins(self):
        # Loads any modules that exist in plugins directory
        plugins_folder = os.environ["PLUGINS_DIRECTORY"]
        loaded_plugins = 0
        for package in pkgutil.iter_modules([plugins_folder]):
            finder, name, ispkg = package
            if (ispkg):
                plugin = importlib.import_module(plugins_folder.replace("/", ".") + "." + name)
                for item_name in dir(plugin):
                    item = getattr(plugin, item_name)
                    try:
                        if issubclass(item, (Command, )) and item_name != "Command":
                            self.commandHandler.registerCommand(name, item)
                            loaded_plugins += 1
                    except TypeError:
                        continue
        os.environ["HELP_MENU"] = self.commandHandler.createHelpMenu()
        os.environ["PLUGIN_COUNT"] = str(loaded_plugins)
        print(os.environ["HELP_MENU"])
        return True
        

    def start(self):
        self.commandLoop()

    def commandLoop(self):
        user_in = input(">>> ")
        if not user_in:
            return self.commandLoop()

        self.commandHandler.runCommand(user_in)
        return self.commandLoop()
        
