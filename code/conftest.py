import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture(scope="session")
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == "edge":
        d = webdriver.Edge()
    else:
        d = webdriver.Chrome()
    d.maximize_window()
    yield d
    d.quit()