import pytest
from selene.support.shared import browser
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def config_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 2.0
    browser.driver.set_window_size(1200, 1080)

    yield

    browser.quit()
