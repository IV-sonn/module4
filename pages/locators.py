from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_FORM_INVALID = (By.CSS_SELECTOR, "#login_form_inc")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_INVALID = (By.CSS_SELECTOR, "#register_form_inc")


class ProductPageLocators:
    SUBMIT_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form  button")
    BASKET_FORM = (By.CSS_SELECTOR, "#add_to_basket_form")
    NAME_BOOK = (By.CSS_SELECTOR, "h1:nth-child(1)")
    PRICE_BOOK = (By.CSS_SELECTOR, ".col-sm-6  .price_color")
    BASKET_TOTAL = (By.CSS_SELECTOR, "div[class='alertinner '] p strong")
    NAME_BOOK_IN_BASKET = (By.CSS_SELECTOR, "#messages>div:nth-child(1)>div>strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
