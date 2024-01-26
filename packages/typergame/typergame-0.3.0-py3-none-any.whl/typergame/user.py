from .functions import Functions

class User:

    def __init__(self, projectname: str, commands: list, defaultdelay: int, defaultnewline: bool):

        self.functions = Functions(defaultdelay, defaultnewline)
        self.projectname = projectname
        runningcommands = []
        for command in commands:
            runningcommands.append(command.lower())
        self.commands = runningcommands
        self.functions.clear()
        self.functions.write(f"Welcome to {self.projectname}", newline = True)
        self.username = self.functions.ask("Choose a username")
        self.stats = {}
        self.functions.clear()

    def addstats(self, stat: str):
        """Adds a user stat https://typergame.replit.app/docs?game.user.addstats()"""
        self.stats[stat.lower()] = 0

    def updatestats(self, stat: str, value: int):
        """Updates a user stat https://typergame.replit.app/docs?game.user.updatestats()"""
        self.stats[stat.lower()] += value

    def run(self):
        """Prompts user with list of commands and returns a user input, set as variable command https://typergame.replit.app/docs?game.user.run()"""
        command = self.functions.ask(f"Commands: {', '.join(self.commands)}")
        self.functions.clear()
        if command.lower() in self.commands:
            return command.lower()
        else:
            self.functions.write("That is not a valid option", newline = True)
            return
          
    def __str__(self):

        if len(self.stats) != 0:
            runningstats = ""
            for stat in list(self.stats.keys()):
                runningstats += f"{stat.lower()}: {self.stats[stat]}\n"
            return f"{self.username} - stats\n{(len(self.username) + 9) * '-'}\n{runningstats}"
        else:
            return f"{self.username} - stats\n{(len(self.username) + 9) * '-'}\nNo user stats available\n"
    
