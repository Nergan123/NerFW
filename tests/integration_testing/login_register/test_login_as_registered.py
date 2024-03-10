import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.game
def test_login_as_registered(register_browser_chrome: webdriver, logger):
    """
    Test to access the login_register

    :param register_browser_chrome: Chrome browser instance
    :param logger: Logger instance
    """

    logger.info("Accessing the Login page")
    register_browser_chrome.get("http://nerfw_server:5000/Login")

    register_browser_chrome.find_element(By.ID, "Login").send_keys("test")
    register_browser_chrome.find_element(By.ID, "Password").send_keys("test")
    register_browser_chrome.find_element(By.ID, "Submit").click()

    logger.info("Accessing the Home page")
    assert register_browser_chrome.find_element(
        By.CLASS_NAME, "MenuScreen"
    ), "The login_register was not accessed successfully"
