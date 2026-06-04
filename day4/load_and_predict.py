import pickle
import os

# Load Saved Model
folder = os.path.dirname(os.path.abspath(__file__))
model_file = os.path.join(folder, "student_grade_model.pkl")

with open(model_file, "rb") as file:
    model = pickle.load(file)

print("Model loaded successfully!\n")

# 3 New Students
students = [
    [3, 0, 2, 17],  # Student 1
    [2, 1, 8, 18],  # Student 2
    [4, 0, 0, 16]   # Student 3
]

# Predict
predictions = model.predict(students)

for i, grade in enumerate(predictions, start=1):
    print(f"Student {i}")
    print(f"Predicted Grade: {grade:.2f}")
    print("-" * 25)