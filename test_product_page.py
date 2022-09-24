from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser=browser, url=link)
    page.open()
    page.should_be_product_page()
    page.go_to_button_add_basket()
    page.solve_quiz_and_get_code()
