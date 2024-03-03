# Game object

The `Game` object is the main object of the library. It is used to manage the game state. The object should be created
in the `game_script` function.
Pass `*args` and `**kwargs` to the `Game` object for the server to be able to track the state and progress.

```python
from nerfw import Game


def game_script(*args, **kwargs):
    app = Game(*args, **kwargs)
```

## Create a character

The `create_character` method is used to create a character. Method returns a character object.

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

You can create multiple characters and use them as parameters for other methods.

## Set background

The `set_background` method is used to set the background of the game.

```python
from nerfw import Game


def game_script(*args, **kwargs):
    app = Game(*args, **kwargs)
    app.set_background("path/to/image.png")
```

## Play audio

The `play_audio` method is used to play audio.

```python
from nerfw import Game


def game_script(*args, **kwargs):
    app = Game(*args, **kwargs)
    app.play_audio("path/to/audio.mp3")
```

This method can be used to play background music or sound effects.
You can set the audio on repeat by passing `repeat=True` as a parameter. This argument if `False` by default.

```python
from nerfw import Game


def game_script(*args, **kwargs):
    app = Game(*args, **kwargs)
    app.play_audio("path/to/audio.mp3", repeat=True)
```

## Stop audio

The `stop_audio` method is used to stop audio.
Pass the file path to the song you want to stop from playing as a parameter.

```python
from nerfw import Game


def game_script(*args, **kwargs):
    app = Game(*args, **kwargs)
    app.play_audio("path/to/audio.mp3", repeat=True)
    app.stop_audio("path/to/audio.mp3")
```

## Unlock scene

You might have noticed Gallery in the main menu of your app. This is where all the unlocked scenes are stored.
Create an unlockable scene by using the `unlock_scene` method.

```python
from nerfw import Game


def game_script(*args, **kwargs):
    app = Game(*args, **kwargs)
    app.unlock_scene("path/to/image.png", label="Scene 1", category="Category 1")
```

`label` should be unique identifier for every scene and `category` is used to group scenes in the gallery.
After the player will reach this line `path/to/image.png` will be unlocked in the gallery.

## Choice

The `choice` method is used to create a choice for the player.
The method returns a list of booleans representing player answer.

```python
from nerfw import Game


def game_script(*args, **kwargs):
    app = Game(*args, **kwargs)
    choices = ["Red", "Blue", "Green"]
    choice = app.choice(choices)
```

After that, the player will be able to choose between "Red", "Blue" and "Green".
Answer will be stored in the `choice` variable. It will be a list of booleans. It will look like this:
`[True, False, False]` if the player chooses "Red".

## String input

The `string_input` method is used to create a string input for the player.
The return value will be the string that the player entered.

```python
from nerfw import Game


def game_script(*args, **kwargs):
    app = Game(*args, **kwargs)
    answer = app.string_input("Enter your name")
```

This method will display a message `Enter your name` to the player.
After that, the player will be able to enter a string. The string will be stored in the `answer` variable.