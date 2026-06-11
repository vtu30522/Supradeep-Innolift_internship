import pandas as pd
import matplotlib.pyplot as plt
import os

# Get the folder where this script is located
current_folder = os.path.dirname(os.path.abspath(__file__))

# Path to CSV file
csv_file = os.path.join(current_folder, "creditcard.csv")

# Check if file exists
if not os.path.exists(csv_file):
    print("ERROR: creditcard.csv not found!")
    print("Place creditcard.csv in the same folder as visualization.py")
    print("Current folder:", current_folder)
    exit()

# Load dataset
df = pd.read_csv(csv_file)

print("Dataset loaded successfully!")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# -----------------------------------
# 1. Fraud vs Non-Fraud Distribution
# -----------------------------------
plt.figure(figsize=(6, 4))

df["Class"].value_counts().plot(kind="bar")

plt.title("Fraud vs Non-Fraud Transactions")
plt.xlabel("Class (0 = Non-Fraud, 1 = Fraud)")
plt.ylabel("Number of Transactions")
plt.tight_layout()

plt.savefig(os.path.join(current_folder, "fraud_distribution.png"))
plt.close()

# -----------------------------------
# 2. Top 10 Features vs Fraud Target
# -----------------------------------
correlations = df.corr()["Class"].drop("Class")

top_features = correlations.abs().sort_values(ascending=False).head(10)

plt.figure(figsize=(8, 5))

top_features.plot(kind="bar")

plt.title("Top 10 Features Correlated with Fraud")
plt.xlabel("Features")
plt.ylabel("Absolute Correlation")
plt.tight_layout()

plt.savefig(os.path.join(current_folder, "top_features_vs_fraud.png"))
plt.close()

# -----------------------------------
# 3. Correlation Heatmap
# -----------------------------------
plt.figure(figsize=(12, 10))

corr_matrix = df.corr()

plt.imshow(corr_matrix, cmap="coolwarm", aspect="auto")
plt.colorbar()

plt.title("Correlation Heatmap")
plt.xlabel("Features")
plt.ylabel("Features")

plt.tight_layout()

plt.savefig(os.path.join(current_folder, "correlation_heatmap.png"))
plt.close()

print("\nVisualization files created successfully:")
print("1. fraud_distribution.png")
print("2. top_features_vs_fraud.png")
print("3. correlation_heatmap.png")