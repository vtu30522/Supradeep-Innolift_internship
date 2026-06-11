import pandas as pd
import pickle
import os

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Load Dataset
folder = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(folder, "student-mat.csv")

df = pd.read_csv(csv_file, sep=";")

# Best Features
X = df[["studytime", "failures", "absences", "age"]]
y = df["G3"]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
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
model_file = os.path.join(folder, "student_grade_model.pkl")

with open(model_file, "wb") as file:
    pickle.dump(model, file)

print("\nModel saved successfully!")
print("File: student_grade_model.pkl")