import pandas as pd
import numpy as np
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

# Features to Compare
features = ["studytime", "failures", "absences", "G1"]

# Target
y = df["G3"]

results = []

print("=" * 80)
print("FEATURE COMPARISON USING LINEAR REGRESSION")
print("=" * 80)

for feature in features:

    print(f"\nAnalyzing Feature: {feature}")
    print("-" * 50)

    # Single Feature
    X = df[[feature]]

    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )

    # Create Model
    model = LinearRegression()

    # Train
    model.fit(X_train, y_train)

    # Predict
    y_pred = model.predict(X_test)

    # Metrics
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # Model Details
    coef = model.coef_[0]
    intercept = model.intercept_

    # Save Results
    results.append([
        feature,
        rmse,
        mae,
        mse,
        r2,
        coef,
        intercept
    ])

    print(f"Train Samples : {len(X_train)}")
    print(f"Test Samples  : {len(X_test)}")
    print(f"MSE           : {mse:.3f}")
    print(f"RMSE          : {rmse:.3f}")
    print(f"MAE           : {mae:.3f}")
    print(f"R² Score      : {r2:.3f}")
    print(f"Coefficient   : {coef:.3f}")
    print(f"Intercept     : {intercept:.3f}")

    # Sample Prediction
    sample_value = [[X_test.iloc[0, 0]]]
    predicted = model.predict(sample_value)

    print(f"Sample Input  : {sample_value[0][0]}")
    print(f"Prediction    : {predicted[0]:.2f}")

# Results DataFrame
result_df = pd.DataFrame(
    results,
    columns=[
        "Feature",
        "RMSE",
        "MAE",
        "MSE",
        "R2",
        "Coefficient",
        "Intercept"
    ]
)

# Sort by RMSE
result_df = result_df.sort_values("RMSE")

print("\n")
print("=" * 80)
print("FEATURE RANKING (BEST TO WORST)")
print("=" * 80)

print(result_df)

# Best Feature
best_feature = result_df.iloc[0]

print("\n")
print("=" * 80)
print("BEST SINGLE FEATURE")
print("=" * 80)

print(f"Feature : {best_feature['Feature']}")
print(f"RMSE    : {best_feature['RMSE']:.3f}")
print(f"R²      : {best_feature['R2']:.3f}")

# Save Results
result_df.to_csv(
    os.path.join(folder, "feature_comparison_results.csv"),
    index=False
)

print("\nResults saved to feature_comparison_results.csv")