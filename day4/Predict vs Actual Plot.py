import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    r2_score
)

# Load Dataset
folder = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(folder, "student-mat.csv")

df = pd.read_csv(csv_file, sep=";")

# Features and Target
X = df[["studytime", "failures", "absences", "age"]]
y = df["G3"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# Create Model
model = LinearRegression()

# Train Model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Metrics
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("=" * 50)
print("MODEL PERFORMANCE")
print("=" * 50)
print(f"MSE  : {mse:.3f}")
print(f"RMSE : {rmse:.3f}")
print(f"MAE  : {mae:.3f}")
print(f"R²   : {r2:.3f}")

# Scatter Plot
plt.figure(figsize=(8, 6))

plt.scatter(
    y_test,
    y_pred,
    alpha=0.7,
    label="Predictions"
)

# Perfect Prediction Line
min_val = min(min(y_test), min(y_pred))
max_val = max(max(y_test), max(y_pred))

plt.plot(
    [min_val, max_val],
    [min_val, max_val],
    'r--',
    linewidth=2,
    label="Perfect Prediction"
)

# Titles and Labels
plt.title("Actual vs Predicted G3 Grades", fontsize=14)
plt.xlabel("Actual G3 Grades", fontsize=12)
plt.ylabel("Predicted G3 Grades", fontsize=12)

# Grid
plt.grid(True, linestyle="--", alpha=0.6)

# Legend
plt.legend()

# Tight Layout
plt.tight_layout()

# Save Plot
plt.savefig(
    os.path.join(folder, "predict_vs_actual_plot.png"),
    dpi=300
)

# Show Plot
plt.show()

print("\nPlot saved as: predict_vs_actual_plot.png")