import allure
import pytest
from selenium import webdriver

from utils.utils import read_env_config


def pytest_addoption(parser):
    parser.addoption("--browser", default="Chrome", action="store", help="Browser name (Chrome, Firefox, Edge)")


@pytest.fixture()
@allure.title("--- Open browser ---")
def setup(request):
    url = str(read_env_config("QA", "url"))
    implicit_wait = read_env_config("QA", "implicit_wait")
    browser = request.config.getoption("--browser")
    driver = None
    if browser in ("Chrome", "chrome"):
        driver = webdriver.Chrome()
    elif browser in ("Firefox", "firefox"):
        driver = webdriver.Firefox()
    elif browser in ("Edge", "edge"):
        driver = webdriver.Edge()
    else:
        print("Invalid browser")

    driver.implicitly_wait(implicit_wait)
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()
