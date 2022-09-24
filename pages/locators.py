from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "a[class='btn btn-default']")
    BASKET_LINK_INVALID = (By.CSS_SELECTOR, "a[class='btn btn-default']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner>p>a")
    BASKET_EMPTY_INVALID = (By.CSS_SELECTOR, "#div[id='content_inner'] p a_inc")
    BASKET_FORM = (By.CSS_SELECTOR, "#content_inner")
    BASKET_FORM_EMPTY = (By.CSS_SELECTOR, "#content_inner_inc")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_FORM_INVALID = (By.CSS_SELECTOR, "#login_form_inc")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[name='login_submit']")

    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_INVALID = (By.CSS_SELECTOR, "#register_form_inc")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators:
    SUBMIT_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form  button")
    BASKET_FORM = (By.CSS_SELECTOR, "#add_to_basket_form")
    NAME_BOOK = (By.CSS_SELECTOR, "h1:nth-child(1)")
    PRICE_BOOK = (By.CSS_SELECTOR, ".col-sm-6  .price_color")
    BASKET_TOTAL = (By.CSS_SELECTOR, "div[class='alertinner '] p strong")
    NAME_BOOK_IN_BASKET = (By.CSS_SELECTOR, "#messages>div:nth-child(1)>div>strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
