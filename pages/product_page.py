from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_product_page(self):
        self.should_be_button_add_basket()
        self.should_be_name_product()
        self.should_be_price_product()
        self.should_be_basket_total()
        self.should_be_price_product_in_basket()

    def go_to_button_add_basket(self):
        button_add_basket = self.browser.find_element(*ProductPageLocators.SUBMIT_BASKET)
        button_add_basket.click()

    def should_be_button_add_basket(self):
        assert self.is_element_present(*ProductPageLocators.SUBMIT_BASKET), "Submit basket is not presented"

    def should_be_name_product(self):
        assert self.is_element_present(*ProductPageLocators.NAME_BOOK), "Name book is not presented"

    def should_be_price_product(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_BOOK), "Price book is not presented"

    def should_be_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL), "Basket total is not presented"

    def should_be_price_product_in_basket(self):
        assert self.should_be_basket_total() == self.should_be_price_product(), \
            "Price cart does not is same as price of product"
