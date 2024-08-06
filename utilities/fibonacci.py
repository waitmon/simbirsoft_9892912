import datetime
from datetime import datetime

import allure


class FibonacciNumber:

    @property
    def current_day(self) -> int:
        return int(datetime.today().strftime('%d'))

    @allure.step('Generate number from fibonacci sequence')
    def get_fibonacci(self, current_day: int) -> int:
        if current_day == 1:
            return 0
        elif current_day in [2, 3]:
            return 1
        return self.get_fibonacci(current_day - 1) + self.get_fibonacci(current_day - 2)
