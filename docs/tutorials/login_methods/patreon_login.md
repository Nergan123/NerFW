# Patreon Login Method

Patreon login method is a simple way to allow users to login to your application using their Patreon account.
This method is checking if the user is a patron of your Patreon campaign.

```{image} pics/login_patreon.png
:alt: Select Parameters
:width: 300px
:align: center
```

## Setup Patreon OAuth App

To use Patreon login method, you need to create a Patreon OAuth App. To create a Patreon OAuth App, follow the steps below:

1. Go to [Patreon Developer Portal](https://www.patreon.com/portal/registration/register-clients)
    and click on "Create Client" button.
2. Fill in the details for your application. In the field `Redirect URIs` enter `http://127.0.0.1:5000/patreon/callback`.
    In the field `Client API version` select `v2`.
3. After creating the app, you will get a `Client ID`, `Client Secret` and `Creators Access Token`.
    Save them as an environment variable in your application. For example, in a `.env` file:

    ```bash
    CLIENT_ID=your-client-id
    CLIENT_SECRET=your-client-secret
    CREATOR_TOKEN=your-creator-token
    ```

## Configure Patreon login method

To configure Patreon login method, you need to use the `set_login_method` method:

```python
import nerfw


if __name__ == "__main__":
    app = nerfw.NerFW()
    app.set_login_method("patreon")
```

With patreon login method you dont have to set a list of allowed users, because
the method is checking if the user is a patron of your Patreon campaign.



## Known Issues

Due to a bug in the Patreon API, if you (Creator of OAuth App) are
trying to login to your application, Patreon will reset your Creators Access Token. To test your application
you can use a different Patreon account.
