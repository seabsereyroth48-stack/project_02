class Expense:
    def __init__(self, description, expense_id, date, amount):
        self.description = description
        self.expense_id = expense_id
        self.date = date
        self.__amount = amount

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        if amount > 0:
            self.__amount = amount
        else:
            print("Amount must be greater than 0.")

    def get_category(self):
        return "General"

    def display_info(self):
        print(self.description, self.date, f"${self.get_amount():.2f}")

#food
class FoodExpense(Expense):
    def __init__(self, description, expense_id, date, amount, meal_type):
        super().__init__(description, expense_id, date, amount)
        self.meal_type = meal_type

    def get_category(self):
        return "Food"

    def display_info(self):
        super().display_info()
        print("Meal type:", self.meal_type)

#tranportation
class TransportExpense(Expense):
    def __init__(self, description, expense_id, date, amount, transport_type, distance_km):
        super().__init__(description, expense_id, date, amount)
        self.transport_type = transport_type
        self.distance_km = distance_km

    def get_category(self):
        return "Transport"

    def display_info(self):
        super().display_info()
        print("Transport type:", self.transport_type)
        print("Distance:", self.distance_km, "km")

#bill
class BillExpense(Expense):
    def __init__(self, description, expense_id, date, amount, bill_type, is_late):
        super().__init__(description, expense_id, date, amount)
        self.bill_type = bill_type
        self.is_late = is_late

    def get_category(self):
        return "Bills"

    def get_final_amount(self):
        amount = self.get_amount()
        if self.is_late:
            amount = amount * 1.05
        return amount

    def display_info(self):
        super().display_info()
        print("Bill type:", self.bill_type)
        print("Late:", self.is_late)