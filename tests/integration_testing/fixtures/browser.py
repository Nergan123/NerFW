import uuid

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# pylint: disable=redefined-outer-name

login = str(uuid.uuid4())


@pytest.fixture
def login_value():
    """
    Fixture to create a unique login

    :return: Unique login
    """

    return login


@pytest.fixture
def browser_chrome():
    """
    Fixture to create a Chrome browser instance

    :return: Chrome browser instance
    """

    chrome_options = Options()
    driver = webdriver.Remote("http://selenium-hub:4444/wd/hub", options=chrome_options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture
def register_browser_chrome(browser_chrome: webdriver, logger):
    """
    Fixture to register the browser instance

    :param browser_chrome: Chrome browser instance
    :param logger: Logger instance
    :return: Chrome browser instance
    """

    browser_chrome.get("http://nerfw_server:5000/Register")
    browser_chrome.find_element(By.ID, "Login").send_keys(login)
    browser_chrome.find_element(By.ID, "Password").send_keys("test")
    browser_chrome.find_element(By.ID, "Repeat_password").send_keys("test")
    browser_chrome.find_element(By.ID, "Submit").click()
    logger.info("Registered the test user")

    yield browser_chrome


@pytest.fixture
def browser_logged_in(register_browser_chrome: webdriver):
    """
    Fixture to login the user

    :param register_browser_chrome: Chrome browser instance
    :return: Chrome browser instance
    """

    register_browser_chrome.get("http://nerfw_server:5000/Login")
    register_browser_chrome.find_element(By.ID, "Login").send_keys(login)
    register_browser_chrome.find_element(By.ID, "Password").send_keys("test")
    register_browser_chrome.find_element(By.ID, "Submit").click()
    register_browser_chrome.delete_cookie("line")
    register_browser_chrome.delete_cookie("prev_line")

    yield register_browser_chrome
