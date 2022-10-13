import pytest


@pytest.fixture(scope="function", autouse=True)
def driver():
    driver = ""
    return driver
