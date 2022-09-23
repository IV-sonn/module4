
from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser=browser, url=link)
    page.open()
    browser.implicitly_wait(5)
    page.go_to_login_page()
