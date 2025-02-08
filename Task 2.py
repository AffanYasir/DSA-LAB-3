def calculate_weekly_expenses(expenses):
    weekly_expenses = sum(expenses[:7])
    return weekly_expenses


daily_expenses = [20.5, 100.75, 50, 30, 15, 25, 40, 60, 10]
print("Total expenses for the first 7 days:", calculate_weekly_expenses(daily_expenses))