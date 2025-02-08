def calculate_category_totals(expenses):
    category_totals = [sum(category) for category in expenses]
    return category_totals


expenses = [
    [20, 30, 15],  # Food
    [50, 10, 25],  # Travel
    [40, 20, 10]   # Utilities
]
print("Total expenses by category:", calculate_category_totals(expenses))