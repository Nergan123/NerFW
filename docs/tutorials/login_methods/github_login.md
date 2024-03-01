# GitHub Login Method

GitHub login method is a simple way to allow users to login to your application using their GitHub account.
On login user will be shown a GitHub login button. When the user clicks on the button,
the user will be redirected to GitHub's login page.



The answer is to use MyST. This Sphinx parser allows a richer syntax in markdown and specifically the image tag

```{image} pics/login_github.png
:alt: Select Parameters
:width: 300px
:align: center
```


After successful login, the user will be redirected back to the application with a session token.