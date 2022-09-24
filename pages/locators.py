from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    SUBMIT_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form  button")
    BASKET_FORM = (By.CSS_SELECTOR, "#add_to_basket_form")
    NAME_BOOK = (By.CSS_SELECTOR, "h1:nth-child(1)")
    PRICE_BOOK = (By.CSS_SELECTOR, ".col-sm-6  .price_color")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".basket-mini>strong")
