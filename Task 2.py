def calculate_total_expenses(expenses):
   
    total = 0
    for i in range(7):  
        total += expenses[i]
    return total


if __name__ == "__main__":
   
    daily_expenses = []

    print("Enter your daily expenses for the last 10 days:")
    for day in range(10):  
        expense = float(input(f"Enter expense for Day {day + 1}: "))
        daily_expenses.append(expense)

    total_expenses = calculate_total_expenses(daily_expenses)

    print(f"\nDaily Expenses: {daily_expenses}")
    print(f"Total Expenses for the First 7 Days: {total_expenses}")