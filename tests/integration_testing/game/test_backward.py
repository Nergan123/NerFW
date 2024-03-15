import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.game
def test_game_forward(logger, browser_logged_in: webdriver):
    """
    Test the ability of the game to progress forward

    :param logger: Logger fixture
    :param browser_logged_in: register browser fixture
    :return: None
    """

    logger.info("Accessing the game")
    browser_logged_in.get("http://nerfw_server:5000/Game")

    browser_logged_in.find_element(By.ID, "next").click()
    browser_logged_in.implicitly_wait(10)
    second_page = browser_logged_in.find_element(By.ID, "show-data").get_attribute('innerHTML')
    browser_logged_in.find_element(By.ID, "next").click()
    browser_logged_in.implicitly_wait(10)

    logger.info("Going a step back")
    browser_logged_in.find_element(By.ID, "back").click()
    browser_logged_in.implicitly_wait(10)
    first_page = browser_logged_in.find_element(By.ID, "show-data").get_attribute('innerHTML')

    assert first_page == second_page, "Pages aren't the same"
