def calculate_attendance_percentage(attendance):
    percentages = []
    for employee in attendance:
        attendance_days = sum(employee)
        percentage = (attendance_days / len(employee)) * 100
        percentages.append(percentage)
    return percentages


attendance = [
    [1, 1, 0, 1, 1],  # Employee 1
    [1, 0, 1, 1, 0],  # Employee 2
    [1, 1, 1, 1, 1]   # Employee 3
]
print("Attendance percentages:", calculate_attendance_percentage(attendance))