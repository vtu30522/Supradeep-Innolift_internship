import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.model_selection import (
    train_test_split,
    cross_val_score,
    GridSearchCV
)

from sklearn.metrics import (
    f1_score,
    classification_report
)

# Load Dataset
df = pd.read_csv(
    r"C:\Users\supradeep\OneDrive\Desktop\python_internship\final_project\day7\creditcard.csv"
)

print("Dataset Loaded Successfully")

# Features and Target
X = df.drop("Class", axis=1)
y = df["Class"]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Data Split Completed")

# Load Previous Model
model = joblib.load(
    r"C:\Users\supradeep\OneDrive\Desktop\python_internship\final_project\day7\best_model.pkl"
)

print("Best Model Loaded Successfully")

# Baseline Score
baseline_pred = model.predict(X_test)

baseline_score = f1_score(
    y_test,
    baseline_pred,
    average="weighted"
)

print("\nBaseline F1 Weighted Score:")
print(baseline_score)

# Cross Validation
cv_scores = cross_val_score(
    model,
    X_train,
    y_train,
    cv=3,
    scoring="f1_weighted"
)

print("\nCross Validation Scores:")
print(cv_scores)

print("\nMean CV Score:")
print(cv_scores.mean())

print("\nStandard Deviation:")
print(cv_scores.std())

# Hyperparameter Tuning
param_grid = {
    "n_estimators": [50, 100],
    "max_depth": [5, 10],
    "min_samples_split": [2, 5]
}

print("\nRunning GridSearchCV...")

grid = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    cv=3,
    scoring="f1_weighted",
    n_jobs=-1
)

grid.fit(X_train, y_train)

print("\nBest Parameters:")
print(grid.best_params_)

print("\nBest CV Score:")
print(grid.best_score_)

# Tuned Model
tuned_model = grid.best_estimator_

tuned_pred = tuned_model.predict(X_test)

tuned_score = f1_score(
    y_test,
    tuned_pred,
    average="weighted"
)

print("\nTuned Model F1 Score:")
print(tuned_score)

print("\nClassification Report:")
print(classification_report(
    y_test,
    tuned_pred
))

# Comparison Report
comparison_df = pd.DataFrame({
    "Model": ["Default Model", "Tuned Model"],
    "F1 Score": [baseline_score, tuned_score]
})

print("\n")
print("=" * 50)
print("MODEL COMPARISON REPORT")
print("=" * 50)
print(comparison_df)

improvement = tuned_score - baseline_score

print("\nImprovement:", improvement)

if tuned_score > baseline_score:
    print("Result: Tuned Model performed better.")
elif tuned_score < baseline_score:
    print("Result: Default Model performed better.")
else:
    print("Result: Both models performed equally.")

# Validation Curve
results = pd.DataFrame(grid.cv_results_)

validation_data = results.groupby(
    "param_n_estimators"
)["mean_test_score"].mean()

plt.figure(figsize=(8, 5))

plt.plot(
    validation_data.index,
    validation_data.values,
    marker="o"
)

plt.title("Validation Curve - Random Forest")
plt.xlabel("n_estimators")
plt.ylabel("Mean Cross Validation Score")
plt.grid(True)

plt.savefig(
    r"C:\Users\supradeep\OneDrive\Desktop\python_internship\final_project\day7\validation_curve.png"
)

plt.show()

print("\nValidation Curve Saved Successfully")

# Save Tuned Model
joblib.dump(
    tuned_model,
    r"C:\Users\supradeep\OneDrive\Desktop\python_internship\final_project\day7\tuned_model.pkl"
)

print("\nTuned Model Saved Successfully")