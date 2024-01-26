import os, sys, time

class Functions:

    def __init__(self, defaultdelay: int, defaultnewline: bool):

        self.defaultdelay = defaultdelay
        self.defaultnewline = defaultnewline

    def clear(self):
        """Clears the console https://typergame.replit.app/docs?game.functions.clear()"""
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def pause(self, delay: int):
        """Delays the action coming after it https://typergame.replit.app/docs?game.functions.pause()"""
        time.sleep(delay)

    def write(self, text: str, delay: int = None, newline: bool = None):
        """Writes the text arg out character by character https://typergame.replit.app/docs?game.functions.write()"""
        if delay == None:
            runningdelay = self.defaultdelay
        else:
            runningdelay = delay
        if newline == None:
            runningnewline = self.defaultnewline
        else:
            runningnewline = newline
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            self.pause(runningdelay)
        if runningnewline:
            print()

    def ask(self, question: str, delay: int = None):
        """Prints out question arg with the write function and returns a user input https://typergame.replit.app/docs?game.functions.ask()"""
        self.write(question, delay, True)
        return input("> ")

