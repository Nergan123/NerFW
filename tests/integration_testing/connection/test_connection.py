import requests
import pytest


@pytest.mark.connection
@pytest.mark.parametrize(
    "endpoint, method, result",
    [
        ("/", "get", 200),
        ("/login", "post", 415),
        ("/login/register", "post", 415),
        ("/game", "get", 302),
        ("/game/forward", "post", 302),
        ("/game/backward", "post", 302),
        ("/game/load_game", "post", 302),
        ("/game/save", "post", 302),
    ],
)
def test_connection(logger, endpoint, method, result):
    """Tests the connection to the server at the specified
    endpoint using the specified HTTP method.

    This function sends a request to the server at the
    specified endpoint using the specified HTTP method,
    and checks if the status code of the response is equal to the expected result.

    Args:
        logger (Logger): The logger object used to log information about the test.
        endpoint (str): The endpoint to which the request is sent.
        method (str): The HTTP method of the request. Can be either 'get' or 'post'.
        result (int): The expected status code of the response.

    Raises:
        AssertionError: If the status code of the response is not equal to the expected result.
    """
    logger.info(f"Testing connection to nerfw_server {endpoint}")
    if method == "get":
        response = requests.get(
            f"http://nerfw_server:5000{endpoint}", allow_redirects=False
        )
    else:
        response = requests.post(
            f"http://nerfw_server:5000{endpoint}", allow_redirects=False
        )
    assert response.status_code == result
