from expense import FoodExpense
from exceptions import BudgetExceededError
from budget import Budget
from tracker import ExpenseTracker
from expense import TransportExpense
from expense import BillExpense

budget = Budget(100)
tracker = ExpenseTracker(budget)

while True:
    print("\n===== Expense Tracker Menu =====")
    print("1. Add food expense")
    print("2. Add transport expense")
    print("3. Add bill expense")
    print("4. Show all expenses")
    print("5. Show expenses by category")
    print("6. Update expense amount")
    print("7. Remove expense")
    print("8. Set monthly budget")
    print("9. Show summary")
    print("10. Exit")
    choice = input("Please choose an option: ")

   #food
    if choice == "1":
        expense_id = input("Enter expense ID: ")
        description = input("Enter description: ")
        date = input("Enter date: ")
        amount = float(input("Enter amount: "))
        meal_type = input("Enter meal type: ")
        food = FoodExpense(description, expense_id, date, amount, meal_type)
        tracker.add_expense(food)
   
   #transport
    elif choice == "2":
        expense_id = input("Enter expense ID: ")
        description = input("Enter description: ")
        date = input("Enter date: ")
        amount = float(input("Enter amount: "))
        transport_type = input("Enter transport type: ")
        distance = float(input("Enter distance in km: "))
        transport = TransportExpense(description, expense_id, date, amount,transport_type, distance)
        tracker.add_expense(transport)

#bill
    elif choice == "3":
        expense_id = input("Enter expense ID: ")
        description = input("Enter description: ")
        date = input("Enter date: ")
        amount = float(input("Enter amount: "))
        is_late = input("Is the bill late? (yes/no): ").lower() == "yes"
        bill_type = input("Enter bill type: ")
        bill = BillExpense(
        description, expense_id, date, amount, bill_type, is_late
        )
        tracker.add_expense(bill)
   
#showexp
    elif choice == "4":
        tracker.show_expenses()
    
#showbycategory
    elif choice == "5":
        category = input("Enter category (food/transport/bill): ")
        tracker.show_by_category(category)

#update 
    elif choice == "6":
        expense_id = input("Enter expense ID to update: ")
        new_amount = float(input("Enter new amount: "))
        tracker.update_expense(expense_id, new_amount)

#removeexp
    elif choice == "6":
        expense_id = input("Enter expense ID to update: ")
        new_amount = float(input("Enter new amount: "))
        tracker.update_expense(expense_id, new_amount)

#monthlybudget
    elif choice == "8":
        amount = float(input("Enter monthly budget: "))
        budget.set_limit(amount)
        print("Monthly budget updated.")

#showbudget
    elif choice == "9":
        tracker.show_budget()
    
    elif choice == "10":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")