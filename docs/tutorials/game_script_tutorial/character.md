# Character object

The `Character` object is used to create a character in the game.
The object is created using the `create_character` method of the `Game` object.

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

## Say

The `say` method is used to make a character say something.

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
    character.say("Hello, World!")
```

## Move

The `move` method is used to move a character to a specific position.

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
    character.animation.move(
        50,                 # X position in % of the screen
        10,                 # Y position in % of the screen
        2                   # Duration of the animation in seconds
    )
```

## Show

The `show` method is used to show a character on a screen.

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
    character.show()
```

## Hide

The `hide` method is used to hide a character from the screen.

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
    character.hide()
```

## Scale

The `scale` method is used to scale a character to a specific size.

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
    character.scale(
        100,                        # Width of the character in px
        200,                        # Height of the character in px
    )
```