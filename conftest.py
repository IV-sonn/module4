import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: en or ...")


@pytest.fixture(scope="function")
def language(request):
    return request.config.getoption("--language")


@pytest.fixture(scope="function")
def browser(language):
    print("\nstart browser for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
