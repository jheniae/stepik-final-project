from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in str(self.browser.current_url), 'Login url is not present'
    
    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"
        
    def register_new_user(self, email, password):
        self.email = email
        self.password = password
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_CONFIRM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER).click()


    
    
