"""Typergame module https://typergame.replit.app"""

from .functions import Functions
from .user import User
from .inventory import Inventory

class Typergame:
    """Initialization of module, set as variable game https://typergame.replit.app/docs?class=game"""
    def __init__(self, projectname: str, commands: list, defaultdelay: int = 0.02, defaultnewline: bool = True):

        self.functions = Functions(defaultdelay, defaultnewline)
        """Class for basic functions https://typergame.replit.app/docs?class=functions"""
        self.user = User(projectname, commands, defaultdelay, defaultnewline)
        """Class for user operations https://typergame.replit.app/docs?class=user"""
        self.inventory = Inventory(self.user.username)
        """Class for inventory operations https://typergame.replit.app/docs?class=inventory"""

