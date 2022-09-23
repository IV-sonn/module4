
from selenium.webdriver.common.by import By


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    browser.implicitly_wait(5)
    login_link = browser.find_elements(By.CSS_SELECTOR, "#login_link")
    login_link[0].click()
    assert len(login_link) > 0, "login link not found"
