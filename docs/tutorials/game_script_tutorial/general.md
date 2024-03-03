# Creating a game script

A game script is a function which will be executed by a server when a game is started.

Start by creating a new function

```python
def game_script(*args, **kwargs):
    pass
```

The `*args` and `**kwargs` are used to pass arguments to the game script.
Server is passing an information about the game previous state and the current state.
Without these arguments, the game script will not work.

Let's start by creating a main object `Game`. This object is used to create characters, set background and more.

```python
from nerfw import Game


def game_script(*args, **kwargs):
    app = Game(*args, **kwargs)
```

The `Game` object will be covered in more detail in later chapters of the tutorial.

Now that the `Game` object is created, we can start by creating a character.

```python
from nerfw import Game


def game_script(*args, **kwargs):
    app = Game(*args, **kwargs)
    character = app.create_character(
        "Coder",                    # Name of the character
        "path/to/image.png",        # Path to the image
        (255, 100, 100),            # Color of the character name
        (70, 10),                   # Position of the character in % of the screen
    )
```

The `create_character` method is used to create a character. The first argument is the name of the character,
the second is the path to the image, the third is the color of the character name
and the last is the position of the character in % of the screen.

We will cover more of character functionality in later chapters of the tutorial.

For now let's make the character say something.

```python
from nerfw import Game


def game_script(*args, **kwargs):
    app = Game(*args, **kwargs)
    character = app.create_character(
        "Coder",
        "path/to/image.png",
        (255, 100, 100),
        (70, 10),
    )
    character.say("Hello World!")
```

Now lets pass the game script to the server.

```python
import nerfw
from nerfw import Game


def game_script(*args, **kwargs):
    app = Game(*args, **kwargs)
    character = app.create_character(
        "Coder",
        "path/to/image.png",
        (255, 100, 100),
        (70, 10),
    )
    character.say("Hello World!")


if __name__ == "__main__":
    server = nerfw.NerFW()
    server.run(game_script)
```

This will create a server instance with default settings and run the game script.
Now you can navigate to `http://localhost:5000` and see the result.
