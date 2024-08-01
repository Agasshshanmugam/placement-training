def add_expense(expenses, description, amount):
    expenses.append({'description': description, 'amount': amount})

def view_expenses(expenses):
    total = 0
    for expense in expenses:
        print(f"{expense['description']}: ${expense['amount']:.2f}")
        total += expense['amount']
    print(f"Total expenses: ${total:.2f}")

def main():
    expenses = []
    while True:
        print("1. Add expense")
        print("2. View expenses")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            add_expense(expenses, description, amount)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            break

if __name__ == '__main__':
    main()
