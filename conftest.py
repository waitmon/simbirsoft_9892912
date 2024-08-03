import pytest
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium import webdriver
import config

browser_options = {
    'chrome': ChromeOptions,
    'firefox': FFOptions,
    'edge': EdgeOptions,
}


def get_browser_options(browser):
    options = browser_options[browser]()
    # options.add_argument('--start-fullscreen')
    options.add_argument("--no-sandbox")
    options.add_argument('--headless')
    return options


def get_driver(browser_name):
    driver = webdriver.Remote(
        command_executor=config.GRID_HUB,
        options=get_browser_options(browser_name),
    )
    driver.browser_name = browser_name
    return driver


@pytest.fixture(scope='session', params=browser_options.keys(), ids=[key for key in browser_options])
def browser(request):
    driver = get_driver(request.param)
    yield driver
    driver.quit()
