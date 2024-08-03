from selenium.webdriver.common.by import By


class LoginPageLocators:
    CUSTOMER_LOGIN = (By.CSS_SELECTOR, 'button[ng-click*="customer"]')
    USER_SELECT = (By.ID, 'userSelect')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')


class AccountPageLocators:
    TRANSACTIONS_BUTTON = (By.CSS_SELECTOR, 'button[ng-click*="transactions"]')
    DEPOSIT_BUTTON = (By.CSS_SELECTOR, 'button[ng-click*="deposit"]')
    WITHDRAWL_BUTTON = (By.CSS_SELECTOR, 'button[ng-click*="withdrawl"]')
    AMOUNT_INPUT = (By.CSS_SELECTOR, 'input[type="number"]')
    OPERATION_RESULT_TEXT = (By.CSS_SELECTOR, 'span[ng-show="message"]')
    BALANCE_AMOUNT = (By.XPATH, '(//div[@ng-hide="noAccount"]/text()[2]//following::strong[@class="ng-binding"])[1]')


class TransactionPageLocators:
    BACK_BUTTON = (By.CSS_SELECTOR, 'button[ng-click*="back"]')
    ROWS = (By.XPATH, "//table/tbody/tr")
    CELLS = (By.TAG_NAME, "td")
