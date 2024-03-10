import uuid

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.login
def test_login_unregistered(browser_chrome: webdriver, logger):
    """
    Test to access the login_register

    :param browser_chrome: Chrome browser instance
    :param logger: Logger instance
    """

    logger.info("Accessing the Login page")
    browser_chrome.get("http://nerfw_server:5000/Login")

    login = str(uuid.uuid4())
    password = str(uuid.uuid4())

    browser_chrome.find_element(By.ID, "Login").send_keys(login)
    browser_chrome.find_element(By.ID, "Password").send_keys(password)
    browser_chrome.find_element(By.ID, "Submit").click()

    logger.info("Accessing the Home page")
    assert (
        not browser_chrome.current_url == "http://nerfw_server:5000/"
    ), "The game was accessed successfully. It should not"
