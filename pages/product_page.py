from .base_page import BasePage
from .locators import ProductPageLocator


class ProductPage(BasePage):

    def should_be_product_on_basket(self):
        self.should_message_basket()
        self.should_price_equal()

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocator.ADD_TO_BASKET)
        button.click()

    def should_message_basket(self):
        product_name = self.browser.find_element(*ProductPageLocator.NAME_PRODUCT).text
        product_name_in_message = self.browser.find_element(*ProductPageLocator.NAME_PRODUCT_IN_ALERT).text
        assert product_name == product_name_in_message, f"Product name mast be {product_name} but is {product_name_in_message}"
 
    def should_price_equal(self):
        product_price = self.browser.find_element(*ProductPageLocator.PRICE_PRODUCT)
        product_price_in_alert = self.browser.find_element(*ProductPageLocator.COST_PRODUCT_IN_BASKET)
        assert product_price.text == product_price_in_alert.text, "Product price not equal"
    

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocator.SUCCESS_MESSAGE), "Success message is present, but not should be"

    def must_disappear(self):
        assert self.is_disappeared(*ProductPageLocator.SUCCESS_MESSAGE), "Appeared"