from exceptions import InvalidAmountError


class Budget:
    def __init__(self, monthly_limit):
        self.__monthly_limit = monthly_limit

    def get_limit(self):
        return self.__monthly_limit

    def set_limit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Budget must be greater than 0.")
        self.__monthly_limit = amount

    def get_remaining(self, total_spent):
        return self.__monthly_limit - total_spent