# GitHub Login Method

GitHub login method is a simple way to allow users to login to your application using their GitHub account.
On login user will be shown a GitHub login button. When the user clicks on the button,
the user will be redirected to GitHub's login page.

```{image} pics/login_github.png
:alt: Select Parameters
:width: 300px
:align: center
```


After successful login, the user will be redirected back to the application with a session token.

## Setup GitHub authentication

To use GitHub login method, you need to create a GitHub OAuth App. To create a GitHub OAuth App, follow the steps below:

1. Go to [GitHub Developer Settings](https://github.com/settings/developers) and click on "New OAuth App" button.
2. Fill in the details for your application. In the field `Homepage URL` enter `http://127.0.0.1:500`.
In the field `Authorization callback URL` enter `http://127.0.0.1:5000/github/callback`.
3. After creating the app, you will get a `Client ID` and `Client Secret`. Save them as an environment variable in
your application. For example, in a `.env` file:

    ```bash
    GITHUB_CLIENT_ID=your-client-id
    GITHUB_CLIENT_SECRET=your-client-secret
    ```

## Configure GitHub login method

To configure GitHub login method, you need to use the `set_login_method` method:

```python
import nerfw


if __name__ == "__main__":
    app = nerfw.NerFW()
    app.set_login_method("github")
```

## GitHub login method parameters

If you want to set a list of allowed users, you can use the `set_allowed_users` method:

```python
import nerfw


if __name__ == "__main__":
    app = nerfw.NerFW()
    app.set_login_method("github")
    app.set_allowed_users(["user1", "user2"])
```

User will be rejected if their GitHub username is not in the list of allowed users.
