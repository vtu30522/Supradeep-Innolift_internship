import pandas as pd
import numpy as np
import os

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load Dataset
folder = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(folder, "student-mat.csv")

df = pd.read_csv(csv_file, sep=";")

# Select all numeric columns
numeric_df = df.select_dtypes(include='number')

# Features (all numeric columns except G3)
X = numeric_df.drop("G3", axis=1)

# Target
y = numeric_df["G3"]

print("Features Used:")
print(list(X.columns))

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create Model
model = LinearRegression()

# Train Model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nModel Performance")
print("-" * 30)
print(f"RMSE : {rmse:.3f}")
print(f"R² Score : {r2:.3f}")

# Predict New Student
new_student = [[
    18,  # age
    2,   # Medu
    2,   # Fedu
    1,   # traveltime
    3,   # studytime
    0,   # failures
    10,  # famrel
    3,   # freetime
    3,   # goout
    1,   # Dalc
    1,   # Walc
    4,   # health
    2,   # absences
    12,  # G1
    13   # G2
]]

predicted_grade = model.predict(new_student)

print("\nPrediction for New Student")
print("-" * 30)
print(f"Predicted G3 Grade: {predicted_grade[0]:.2f}")