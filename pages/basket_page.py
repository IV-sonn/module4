from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_basket_page(self):
        self.should_be_basket_form()

    def should_be_basket_url(self):
        assert "basket" in self.url, "Current url does not contain basket string"

    def should_be_basket_form(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_FORM), "Basket form is not presented"

    def should_be_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), "Basket does not is empty"
