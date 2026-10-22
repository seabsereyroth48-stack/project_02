from exceptions import BudgetExceededError

class ExpenseTracker:
    def __init__(self, budget):
        self.expenses = []
        self.budget = budget

    def add_expense(self, expense):
        amount = expense.get_amount()
        total = self.get_total_spent()
        budget_limit = self.budget.get_limit()

        if total + amount > budget_limit:
            print("\nSorry, this expense would exceed your monthly budget.")
            print(
                f"Budget: ${budget_limit:.2f} | "
                f"Spent: ${total:.2f} | "
                f"Remaining: ${budget_limit - total:.2f}"
            )
            return

        self.expenses.append(expense)
        print("\nExpense added successfully.")

    def show_expenses(self):
        if len(self.expenses) == 0:
            print("\nNo expenses yet.")
            return

        for expense in self.expenses:
            expense.display_info()
            print("--------------------")

    def show_by_category(self, category):
        for expense in self.expenses:
            if expense.get_category().lower() == category.lower():
                expense.display_info()
                print("--------------------")

    def update_expense(self, expense_id, new_amount):
        for expense in self.expenses:
            if expense.expense_id == expense_id:
                expense.set_amount(new_amount)
                print("\nExpense updated successfully.")
                return
            print("\nExpense ID not found.")

    def get_total_spent(self):
        total = 0

        for expense in self.expenses:
            if hasattr(expense, "get_final_amount"):
                total += expense.get_final_amount()
            else:
                total += expense.get_amount()

        return total

    def show_budget(self):
        total = self.get_total_spent()
        remaining = self.budget.get_remaining(total)
        print("\n=== Showing Budget ===")
        print("Total spent:", total)
        print("Budget limit:", self.budget.get_limit())
        print("Remaining budget:", remaining)