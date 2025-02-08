def display_above_average_grades(grades):
    average = sum(grades) / len(grades)
    print("Grades above or equal to average:")
    for grade in grades:
        if grade >= average:
            print(grade)


grades = [85, 90, 78, 92, 88]
display_above_average_grades(grades)