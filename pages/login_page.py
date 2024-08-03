import allure
from selenium.webdriver.support.ui import Select

from locators.locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step('Login as customer')
    def login_as_customer(self):
        self.find_to_be_clickable(*LoginPageLocators.CUSTOMER_LOGIN).click()

    @allure.step('Select username')
    def select_user(self, username):
        select = Select(self.find_to_be_clickable(*LoginPageLocators.USER_SELECT))
        select.select_by_visible_text(username)
