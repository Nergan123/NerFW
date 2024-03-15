import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.game
@pytest.mark.parametrize(
    "steps",
    [1, 2, 3]
)
def test_game_forward(logger, browser_logged_in: webdriver, steps):
    """
    Test the ability of the game to progress forward

    :param logger: Logger fixture
    :param browser_logged_in: register browser fixture
    :param steps: Number of steps to progress
    :return: None
    """

    logger.info("Accessing the game")
    browser_logged_in.get("http://nerfw_server:5000/Game")
    first_page = browser_logged_in.find_element(By.ID, "body_element").get_attribute('innerHTML')

    logger.info("Progressing to the next Frame")
    for _ in range(steps):
        browser_logged_in.find_element(By.ID, "next").click()
        browser_logged_in.implicitly_wait(10)
    second_page = browser_logged_in.find_element(By.ID, "body_element").get_attribute('innerHTML')

    assert first_page != second_page, "Got same page"
