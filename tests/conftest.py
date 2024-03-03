from selene import browser
import pytest
from pathlib import Path


def path(file_name):
    return str(Path(__file__).parent.joinpath(f'resources/{file_name}'))


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()
