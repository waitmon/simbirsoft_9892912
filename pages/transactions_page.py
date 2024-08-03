import csv
import datetime

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
    def get_transaction_list(self):
        transactions_table_rows = self.find_all_elements(*TransactionPageLocators.ROWS)
        transactions = []
        for element in transactions_table_rows:
            cells = element.find_elements(*TransactionPageLocators.CELLS)
            amount = int(cells[1].text)
            transaction_type = cells[2].text
            transactions.append(amount)
            transactions.append(transaction_type)
        return transactions

    @allure.step('Generate csv report')
    def generate_csv_report(self):
        transactions = self.find_all_elements(*TransactionPageLocators.ROWS)
        file_name = 'csv_report.csv'

        with open(file_name, 'w', encoding="utf-8", newline='') as file:
            writer = csv.writer(file, delimiter=';')

            headers = ["Дата-времяТранзакции", "Сумма", "ТипТранзакции"]
            writer.writerow(headers)

            for transaction in transactions:
                transaction_info = transaction.find_elements(*TransactionPageLocators.CELLS)
                date_time_str, amount, transaction_type = transaction_info
                date_time = datetime.datetime.strptime(date_time_str.text, "%b %d, %Y %H:%M:%S %p")
                report_data = [date_time.strftime('%d %B %Y %H:%M:%S'), amount.text, transaction_type.text]
                writer.writerow(report_data)

            return file_name
