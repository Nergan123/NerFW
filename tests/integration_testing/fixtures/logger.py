import logging
import pytest


@pytest.fixture()
def logger():
    """Fixture for creating a logger object."""

    logger_fixture = logging.getLogger(f"{__file__}.{__name__}")
    logger_fixture.setLevel(logging.INFO)
    return logger_fixture
