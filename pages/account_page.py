import allure
from selenium.webdriver.support import expected_conditions as EC

from locators.locators import LoginPageLocators, AccountPageLocators
from pages.base_page import BasePage


class AccountPage(BasePage):

    @allure.step('Click Deposit')
    def click_deposit_button(self):
        self.find_to_be_clickable(*AccountPageLocators.DEPOSIT_BUTTON).click()
        self.wait.until(EC.text_to_be_present_in_element(LoginPageLocators.SUBMIT_BUTTON, text_='Deposit'))

    @allure.step('Input transaction amount')
    def input_amount(self, amount: int):
        self.find_to_be_clickable(*AccountPageLocators.AMOUNT_INPUT).send_keys(str(amount))

    @allure.step('Click Withdrawl')
    def click_withdrawl(self):
        self.find_to_be_clickable(*AccountPageLocators.WITHDRAWL_BUTTON).click()
        self.wait.until(EC.text_to_be_present_in_element(LoginPageLocators.SUBMIT_BUTTON, text_='Withdraw'))
