from typing import List, Union

import allure

from locators.locators import AccountPageLocators, TransactionPageLocators
from pages.base_page import BasePage


class TransactionsPage(BasePage):

    @allure.step('Go to transactions list')
    def go_to_transactions_list(self):
        self.find_to_be_clickable(*AccountPageLocators.TRANSACTIONS_BUTTON).click()
        self.find_to_be_clickable(*TransactionPageLocators.BACK_BUTTON).click()
        self.find_to_be_clickable(*AccountPageLocators.TRANSACTIONS_BUTTON).click()

    @allure.step('Get transaction list')
    def get_transaction_list(self) -> List[Union[int, str]]:
        transactions_table_rows = self.find_all_elements(*TransactionPageLocators.ROWS)
        transactions = []
        for element in transactions_table_rows:
            cells = element.find_elements(*TransactionPageLocators.CELLS)
            amount = int(cells[1].text)
            transaction_type = cells[2].text
            transactions.append(amount)
            transactions.append(transaction_type)
        return transactions

