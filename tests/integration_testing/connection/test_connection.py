import time

import requests
import pytest


@pytest.mark.connection
@pytest.mark.parametrize(
    "endpoint, method, result",
    [
        ("/", "get", 200),
        ("/api/authorize", "post", 415),
        ("/api/register", "post", 415),
        ("/api/forward", "post", 302),
        ("/api/backward", "post", 302),
        ("/api/get_saves", "post", 302),
        ("/api/save", "post", 302),
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
    wait_for_server(logger)
    logger.info(f"Testing connection to nerfw_server {endpoint}")
    if method == "get":
        response = requests.get(
            f"http://nerfw_server:5000{endpoint}", allow_redirects=False, timeout=10
        )
    else:
        response = requests.post(
            f"http://nerfw_server:5000{endpoint}", allow_redirects=False, timeout=10
        )
    assert response.status_code == result


def wait_for_server(logger, retry_interval=5, max_retries=5):
    """Wait for the server to be ready.

    This function sends a request to the server and waits for a successful response.
    If the server is not ready, it waits for a specified interval and then retries.
    It does this for a maximum number of retries.

    Args:
        logger (Logger): The logger object used to log information about the test.
        retry_interval (int): The number of seconds to wait between retries.
        max_retries (int): The maximum number of retries.

    Raises:
        RuntimeError: If the server is not ready after the maximum number of retries.
    """
    for i in range(max_retries):
        try:
            response = requests.get("http://nerfw_server:5000/", allow_redirects=False, timeout=10)
            if response.status_code == 200:
                logger.info("Server is ready.")
                return
        except requests.exceptions.RequestException:
            logger.info(f"Server is not ready. Retry {i+1}/{max_retries}.")
            time.sleep(retry_interval)
    raise RuntimeError("Server is not ready.")
