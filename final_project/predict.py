import pickle
import pandas as pd
import os

# Get correct folder (final_project)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Correct file paths
model_path = os.path.join(BASE_DIR, "model.pkl")
csv_path = os.path.join(BASE_DIR, "creditcard.csv")

# Load model
with open(model_path, "rb") as f:
    model = pickle.load(f)

# Load dataset
df = pd.read_csv(csv_path)

X = df.drop("Class", axis=1)

# Predict multiple cases
num_cases = 20
sample_data = X.sample(num_cases, random_state=42)

print("\n========== FRAUD DETECTION RESULTS ==========\n")

for i in range(num_cases):
    input_data = sample_data.iloc[i].values.reshape(1, -1)
    prediction = model.predict(input_data)[0]

    if prediction == 0:
        result = "NORMAL TRANSACTION"
    else:
        result = "⚠ FRAUD DETECTED ⚠"

    print(f"Case {i+1}: {result}")

print("\nPrediction completed successfully!")