import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score

# Load dataset
df = pd.read_csv(
    r"C:\Users\supradeep\OneDrive\Desktop\python_internship\final_project\day7\creditcard.csv"
)

print("Dataset Loaded Successfully")
print(df.shape)

# Features and Target
X = df.drop("Class", axis=1)
y = df["Class"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Data Split Completed")

# Train Random Forest Model
model = RandomForestClassifier(
    random_state=42
)

model.fit(X_train, y_train)

print("Model Training Completed")

# Prediction
y_pred = model.predict(X_test)

# F1 Score
score = f1_score(
    y_test,
    y_pred,
    average="weighted"
)

print("F1 Weighted Score:", score)

# Save Model
joblib.dump(
    model,
    r"C:\Users\supradeep\OneDrive\Desktop\python_internship\final_project\day7\best_model.pkl"
)

print("Model saved as best_model.pkl")