# NumPy Marks Analyser
import numpy as np
# Marks of 10 students
marks = np.array([320, 280, 150, 400, 260, 210, 340, 290, 180, 370])
# Calculations
mean_marks = np.mean(marks)
highest_marks = np.max(marks)
lowest_marks = np.min(marks)
std_dev = np.std(marks)

# Pass marks = 250
passed_students = np.sum(marks >= 250)

# Summary Report
print("===== MARKS ANALYSIS REPORT =====")
print("Marks:", marks)
print("Average Marks:", round(mean_marks, 2))
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)
print("Standard Deviation:", round(std_dev, 2))
print("Number of Students Passed (>=250):", passed_students)
print("Number of Students Failed (<250):", len(marks) - passed_students)