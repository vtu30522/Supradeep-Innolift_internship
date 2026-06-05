import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Get current folder (final_project)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Correct CSV path
csv_path = os.path.join(BASE_DIR, "creditcard.csv")

# Load dataset
df = pd.read_csv(csv_path)

print("Dataset loaded successfully!")
print("Shape:", df.shape)

# Features and target
X = df.drop("Class", axis=1)
y = df["Class"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Accuracy
accuracy = model.score(X_test, y_test)
print("Accuracy:", accuracy)

# Save model
model_path = os.path.join(BASE_DIR, "model.pkl")
with open(model_path, "wb") as f:
    pickle.dump(model, f)

print("Model saved successfully!")