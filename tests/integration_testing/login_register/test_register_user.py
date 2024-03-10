import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# pylint: disable=too-many-arguments


@pytest.mark.login
@pytest.mark.parametrize(
    "login, password, repeat_password, expected",
    [
        ("test1", "test", "test", True),
        ("test2", "test", "test", True),
        ("test3", "test", "test2", False),
    ],
)
def test_register_user(
    browser_chrome: webdriver, logger, login, password, repeat_password, expected
):
    """
    Test to register a user

    :param browser_chrome: Chrome browser instance
    :param logger: Logger instance
    :param login: User login
    :param password: User password
    :param repeat_password: User repeat password
    :param expected: Expected to have access to the game
    """

    logger.info("Accessing the Register page")
    browser_chrome.get("http://nerfw_server:5000/Register")

    logger.info("Filling in forms with the user data")
    browser_chrome.find_element(By.ID, "Login").send_keys(login)
    browser_chrome.find_element(By.ID, "Password").send_keys(password)
    browser_chrome.find_element(By.ID, "Repeat_password").send_keys(repeat_password)
    logger.info(f"Registering the {login} user")
    browser_chrome.find_element(By.ID, "Submit").click()

    if not expected:
        logger.info("Checking if the user was not registered")
        assert (
            browser_chrome.current_url.lower() == "http://nerfw_server:5000/register"
        ), "The user was registered successfully"

        return

    logger.info("Accessing the Login page")
    browser_chrome.get("http://nerfw_server:5000/Login")
    browser_chrome.find_element(By.ID, "Login").send_keys(login)
    browser_chrome.find_element(By.ID, "Password").send_keys(password)
    browser_chrome.find_element(By.ID, "Submit").click()

    logger.info("Checking if the user was registered")
    assert (
        browser_chrome.current_url.lower() == "http://nerfw_server:5000/" and expected
    ), "The user was not registered successfully"
