# Default Login Method

Default login method is te simplest one to setup. It uses the default login form provided by the application.
The application will have a login endpoint that will provide a login form to the user.
The user will fill in the form and submit it. The application will then authenticate the user and
provide a session token.

```{image} pics/login_default_screen.png
:alt: Select Parameters
:width: 300px
:align: center
```


## Setup

```python
import nerfw


if __name__ == "__main__":
    app = nerfw.NerFW()

    app.set_login_method("default")
```

This step is optional as the default login method is already set by default.

In this method the application also allows users to register themselves.
The registration form is also provided by the application.

```{image} pics/register_screen.png
:alt: Select Parameters
:width: 300px
:align: center
```


If you want to allow only selected user to be registered you can use `set_allowed_users` method.

```python
import nerfw

if __name__ == "__main__":
    app = nerfw.NerFW()

    app.set_login_method("default")
    app.set_allowed_users(["user1", "user2"])
```

or you can provide a file containing the list of allowed users.

```python
import nerfw

if __name__ == "__main__":
    app = nerfw.NerFW()

    app.set_login_method("default")
    app.set_allowed_users("path/to/allowed_users.txt")
```