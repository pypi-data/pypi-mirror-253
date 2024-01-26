class Inventory:

    def __init__(self, username: str):
        
        self.username = username
        self.inventory = {}

    def additems(self, item: str, value: int):
        """Adds a inventory item https://typergame.replit.app/docs?game.inventory.additems()"""
        self.inventory[item] = value

    def removeitems(self, item: str):
        """Removes a inventory item https://typergame.replit.app/docs?game.inventory.removeitems()"""
        self.inventory.pop(item)

    def __str__(self):
        
        if len(self.inventory) != 0:
            runninginventory = ""
            for item in list(self.inventory.keys()):
                runninginventory += f"{item.lower()}: {self.inventory[item]}\n"
            return f"{self.username} - inventory\n{(len(self.username) + 13) * '-'}\n{runninginventory}"
        else:
            return f"{self.username} - inventory\n{(len(self.username) + 13) * '-'}\nInventory is empty\n"
    
