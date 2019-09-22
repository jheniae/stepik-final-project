from .base_page import BasePage
from .locators import BaseBasketLocators


class BacketPage(BasePage):

    def should_be_basket_empty(self):
        assert self.is_not_element_present(*BaseBasketLocators.PRODUCT_PRESENT_IN_BASKET), \
            "Basket is not empty"
    
    def gues_must_see_text_empty(self):
        text_message = self.browser.find_element(*BaseBasketLocators.BASKET_TEXT_EMPTY).text
        assert text_message == 'Ваша корзина пуста', "Text not found"