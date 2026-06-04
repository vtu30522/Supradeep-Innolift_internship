import pandas as pd
import numpy as np
import os

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
folder = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(folder, "student-mat.csv")

df = pd.read_csv(csv_file, sep=";")

# Features and Target
X = df[["studytime", "failures", "absences", "age"]]
y = df["G3"]

# More than 10 test sizes
test_sizes = [0.10, 0.15, 0.20, 0.25, 0.30,
              0.35, 0.40, 0.45, 0.50, 0.55, 0.60]

best_r2 = -999
best_split = None

print("=" * 70)
print("Train-Test Split Explorer")
print("=" * 70)

for size in test_sizes:

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=size,
        random_state=42
    )

    # Train Model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict
    y_pred = model.predict(X_test)

    # Metrics
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    print(
        f"Test Size: {size:.2f} | "
        f"Train: {len(X_train):3d} | "
        f"Test: {len(X_test):3d} | "
        f"RMSE: {rmse:.3f} | "
        f"R²: {r2:.3f}"
    )

    if r2 > best_r2:
        best_r2 = r2
        best_split = size

print("\n" + "=" * 70)
print(f"Best Test Size : {best_split}")
print(f"Best R² Score  : {best_r2:.3f}")
print("=" * 70)