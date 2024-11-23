# CLI application
def main():
    budget = float(input("Enter your budget: "))
    tracker = FinanceTracker(budget)

    while True:
        print("\nMenu:")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Check Budget Balance")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            category = input("Enter the category: ")
            description = input("Enter a description: ")
            amount = float(input("Enter the amount: "))
            print(tracker.add_transactions(date, category, description, amount))

        elif choice == "2":
            category = input("Enter a category to filter (or press Enter for all): ")
            print(tracker.get_transaction(category if category else None))

        elif choice == "3":
            print(tracker.get_budget_balance())

        elif choice == "4":
            print("Exiting. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()