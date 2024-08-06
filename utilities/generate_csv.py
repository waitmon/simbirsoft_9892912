import csv
import datetime

import allure

from locators.locators import TransactionPageLocators
from pages.base_page import BasePage


class GenerateCsvReport(BasePage):
    @allure.step('Generate csv report')
    def generate_csv_report(self) -> str:
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
