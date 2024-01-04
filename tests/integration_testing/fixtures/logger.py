import logging
import pytest


@pytest.fixture()
def logger():
    """Fixture for creating a logger object."""

    logger_fixture = logging.getLogger(f"{__file__}.{__name__}")
    return logger_fixture
