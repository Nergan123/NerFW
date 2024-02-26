# Server Setup

Before start make sure you have followed all steps in the [installation guide](installation.md) and 
have your environment activated.

## Create main.py

Create a new file called `main.py` in your project folder. This file will be the entry point of your server.

Import the `nerfw` package.
```python
import nerfw
```

In the end of the file, add the following code.
```python
import nerfw


if __name__ == "__main__":
    """Your code here"""
```

This is done to prevent the code from running when the file is imported as a module. It is a good practice in python
to have this part in your main file due to the way python handles imports.

## Create a server

Under the `if __name__ == "__main__":` line, create a instance of `NerFW` class.

```python
import nerfw


if __name__ == "__main__":
    server = nerfw.NerFW()
```

This will create a server instance with default settings.
You can access it by going to `http://localhost:5000` in your browser.