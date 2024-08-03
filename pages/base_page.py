import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators.locators import LoginPageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
        self.wait = WebDriverWait(driver, 30, poll_frequency=1)

    @allure.step('Open base url')
    def open(self):
        self.driver.get(self.url)

    def find_to_be_clickable(self, how, what):
        try:
            element = self.wait.until(EC.element_to_be_clickable((how, what)))
        except Exception as error:
            allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
            raise Exception(f'Element is not clickable, error message: {error}')
        return element

    @allure.step('Submit form')
    def click_submit(self):
        self.find_to_be_clickable(*LoginPageLocators.SUBMIT_BUTTON).click()

    @allure.step('Check element text')
    def assert_element_text(self, element, text):
        assert self.driver.find_element(*element).text == text, \
            f'Expected text: "{text}", got text instead: "{self.driver.find_element(*element).text}"'

    @allure.step('Get text from element')
    def get_element_text(self, locator):
        return self.driver.find_element(*locator).text

    def find_all_elements(self, how, what):
        elements = self.driver.find_elements(how, what)
        if not elements:
            allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
            raise Exception('No elements were found')
        return elements
