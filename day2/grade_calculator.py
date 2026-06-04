def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 45:
        return "D"
    else:
        return "F"

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = float(input("Enter student marks: "))

    grade = get_grade(marks)

    print("Name:", name)
    print("Marks:", marks)
    print("Grade:", grade)
    print("-" * 20)