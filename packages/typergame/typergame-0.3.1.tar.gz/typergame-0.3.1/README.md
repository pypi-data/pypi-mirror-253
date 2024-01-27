# Typergame.py

### By @drooler (https://bit.ly/drooler)

Current version: V0.3.1

## Update logs

- V0.1.0 - First build

- V0.1.1 to V0.1.2 - Bug fixes

- V0.2.1 - Added costum user stats

- V0.2.2 to V0.2.6 - Bug fixes

- V0.2.7 - Added syntax documentation

- V0.3.0 - Added inventory system

- V0.3.1 - Bug fixes

## How to set up

### 1- Install with pip

Run `pip install typergame`

### 2- Create a .py and paste in the template code

Template code:
```py
import typergame

game = typergame.Typergame("Project name", ["exit"])

running = True

while running:

    command = game.user.run()

    if command == "exit":

        running = False
        game.functions.write("Press enter to exit")

    input()
    game.functions.clear()
```

### 3- Build your game: add commands, add user stats,...

## Links

- Website: https://typergame.replit.app
- Github: https://github.com/bijenmanlol/typergame
- Pypi: https://pypi.org/project/typergame
- Documentation: https://typergame.replit.app/docs