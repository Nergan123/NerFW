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

## Server settings

1. **Debug or Production mode**

   You can set the server to run in debug mode by setting the `debug` parameter to `True` when creating the server
   instance.

    ```python
    server = nerfw.NerFW(debug=True)
    ```

   This will enable the debug mode, which will show you detailed error messages and stack traces in the browser.
   This mode is enabled by default. To switch to a production mode, set the `debug` parameter to `False`.

    ```python
    server = nerfw.NerFW(debug=False)
    ```


2. **Set name of the server**

   You can set the name of the server by setting the `name` parameter when creating the server instance.

    ```python
    server.set_name("MyServer")
    ```

   This will set the name of the server to `MyServer`.


3. **Set login method**

   You can set the login method by setting the `login_method` parameter when creating the server instance.

    ```python
    server.set_login_method("default")
    ```

   This will set the login method to `default`. The available login methods are `default`, `github` and `patreon`.

   We will cover the GitHub and Patreon login methods in the next section since they require additional actions.
   Default login does not.


4. **Set allowed users**

   With `Default` or `GitHub` selected you can provide a list of allowed users.
   You can either provide a list of usernames or path to a file containing usernames.

    ```python
    server.set_allowed_users(["user1", "user2"])
    ```
   or

    ```python
    server.set_allowed_users("path/to/file.txt")
    ```

5. **Set menu background**

   In NerFW you can set a background image for the menu. You can do this by calling the `set_menu_background` method.
   This method takes the path to the image as a parameter.

    ```python
    server.set_menu_background("path/to/image.jpg")
    ```