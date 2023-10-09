
from pages.main_page import MainPage
from .base_page import BasePage
from .locators import LoginPageLocators 


class LoginPage(BasePage):
    #def test_guest_can_go_to_login_page(browser):
    #    link = "http://selenium1py.pythonanywhere.com"
    #    page = MainPage(browser, link)
    #    page.open()
    #    page.go_to_login_page()
    #    login_page = LoginPage(browser, browser.current_url)
    #    login_page.should_be_login_page()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Invalid URL"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login link is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register link is not presented"