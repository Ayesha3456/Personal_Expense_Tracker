import json
import os

# Load expenses from a file
def load_expenses(filename="expenses.json"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return []  # Return an empty list if the file doesn't exist

# Save expenses to a file
def save_expenses(expenses, filename="expenses.json"):
    with open(filename, "w") as file:
        json.dump(expenses, file, indent=4)

# Add an expense
def add_expense(expenses):
    try:
        amount_rupees = float(input("Enter the expense amount in rupees: ₹"))
    except ValueError:
        print("Invalid input. Please enter a valid numeric amount.")
        return
    
    category = input("Enter the category (e.g., Food, Transport): ")
    
    expense = {
        "amount_rupees": amount_rupees,
        "category": category
    }
    
    expenses.append(expense)
    print("Expense added!")

# View total expenses and spending by category
def view_summary(expenses):
    total_spending_rupees = sum(expense['amount_rupees'] for expense in expenses)
    print(f"\nTotal Spending: ₹{total_spending_rupees:.2f}")
    
    print("\nSpending by Category:")
    category_summary = {}
    
    for expense in expenses:
        category = expense['category']
        if category not in category_summary:
            category_summary[category] = 0
        category_summary[category] += expense['amount_rupees']
    
    for category, total in category_summary.items():
        print(f"{category}: ₹{total:.2f}")

# Main function to run the program
def main():
    expenses = load_expenses()  # Load existing expenses from file

    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add an expense")
        print("2. View summary")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            add_expense(expenses)
            save_expenses(expenses)  # Save after adding an expense
        elif choice == '2':
            view_summary(expenses)
        elif choice == '3':
            save_expenses(expenses)  # Save before exiting
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

# Run the program
if __name__ == "__main__":
    main()
