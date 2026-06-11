import pandas as pd
import numpy as np
import pickle
import os

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load Dataset
folder = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(folder, "student-mat.csv")

df = pd.read_csv(csv_file, sep=";")

# Features and Target
X = df[["studytime", "failures", "absences", "age"]]
y = df["G3"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"RMSE : {rmse:.3f}")
print(f"R²   : {r2:.3f}")

# Save Model
model_path = os.path.join(folder, "student_grade_model.pkl")

with open(model_path, "wb") as file:
    pickle.dump(model, file)

print("\nModel saved successfully!")

# Load Model
with open(model_path, "rb") as file:
    loaded_model = pickle.load(file)

print("Model loaded successfully!")

# Predict for 3 Students
students = [
    [3, 0, 2, 17],  # studytime, failures, absences, age
    [2, 1, 8, 18],
    [4, 0, 0, 16]
]

predictions = loaded_model.predict(students)

print("\nPredictions")
print("-" * 30)

for i, grade in enumerate(predictions, start=1):
    print(f"Student {i}: {grade:.2f}")