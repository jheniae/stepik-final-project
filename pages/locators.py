from selenium.webdriver.common.by import By


class MainPageLocator():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")


class ProductPageLocator():
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    NAME_PRODUCT = (By.CSS_SELECTOR, '.product_main>h1')
    NAME_PRODUCT_IN_ALERT = (By.CSS_SELECTOR, '.alert-success>.alertinner strong')
    PRICE_PRODUCT = (By.CSS_SELECTOR, '.product_main>.price_color')
    COST_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '.alert-info .alertinner p strong')