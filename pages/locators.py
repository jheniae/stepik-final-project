from selenium.webdriver.common.by import By


class MainPageLocator():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR '[name="registration-email"]')
    REGISTER_FORM_PASSWORD = (By.CSS_SELECTOR, '[name="registration-password1"]')
    REGISTER_FORM_PASSWORD_CONFIRM = (By.CSS_SELECTOR, '[name="registration-password2"]')
    BUTTON_REGISTER = (By.CSS_SELECTOR, '[name="registration_submit"]')

class ProductPageLocator():
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    NAME_PRODUCT = (By.CSS_SELECTOR, '.product_main>h1')
    NAME_PRODUCT_IN_ALERT = (By.CSS_SELECTOR, '.alert-success>.alertinner strong')
    PRICE_PRODUCT = (By.CSS_SELECTOR, '.product_main>.price_color')
    COST_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '.alert-info .alertinner p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success.alert-success')
    


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BaseBasketLocators():
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group> .btn-default')
    PRODUCT_PRESENT_IN_BASKET = (By.CSS_SELECTOR, '.basket-title.hidden-xs')
    BASKET_TEXT_EMPTY = (By.CSS_SELECTOR, '.content>#content_inner>p')