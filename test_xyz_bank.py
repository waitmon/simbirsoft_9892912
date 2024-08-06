import allure
import pytest
from allure import severity, severity_level

from config import BASE_DIR
from locators.locators import AccountPageLocators
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from pages.transactions_page import TransactionsPage
from utilities.fibonacci import FibonacciNumber
from utilities.generate_csv import GenerateCsvReport


@allure.feature('Bank operations features: deposit, withdrawal & transactions extraction')
class TestBankOperations:
    @allure.title("Bank operations")
    @severity(severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_user_makes_deposit_and_withdrawal_and_checks_transactions_list(self, browser):
        login = LoginPage(browser)
        account = AccountPage(browser)
        transactions = TransactionsPage(browser)
        fib = FibonacciNumber()
        csv = GenerateCsvReport(browser)

        login.open()
        login.login_as_customer()
        login.select_user(username='Harry Potter')
        login.click_submit()

        account.click_deposit_button()
        current_day = fib.current_day
        fibonacci_num = fib.get_fibonacci(current_day)
        account.input_amount(fibonacci_num)
        account.click_submit()
        account.assert_element_text(AccountPageLocators.OPERATION_RESULT_TEXT, 'Deposit Successful')

        account.click_withdrawl()
        account.input_amount(fibonacci_num)
        account.click_submit()
        account.assert_element_text(AccountPageLocators.OPERATION_RESULT_TEXT, 'Transaction successful')

        current_balance = account.get_element_text(AccountPageLocators.BALANCE_AMOUNT)
        assert float(current_balance) == 0, 'Balance has not changed after withdrawal'

        transactions.go_to_transactions_list()
        transaction_lst = transactions.get_transaction_list()
        credit_value, debit_value = transaction_lst[0], transaction_lst[2]
        assert credit_value == fibonacci_num, f'Expected value for Credit: {fibonacci_num}, got instead:{credit_value}'
        assert debit_value == fibonacci_num, f'Expected value for Debit: {fibonacci_num}, got instead: {debit_value}'

        file_name = csv.generate_csv_report()

        allure.attach.file(
            source=BASE_DIR,
            name=file_name,
            attachment_type=allure.attachment_type.CSV,
        )
