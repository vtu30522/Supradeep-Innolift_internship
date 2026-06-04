import pandas as pd

# Create DataFrame
data = {
    "name": ["Rahul", "Priya", "Arjun", "Sneha", "Kiran"],
    "age": [20, 21, 19, 22, 20],
    "city": ["Chennai", "Bangalore", "Hyderabad", "Mumbai", "Delhi"],
    "marks": [85, 45, 72, 38, 90]
}

df = pd.DataFrame(data)

# Display DataFrame
print("===== STUDENT DATA =====")
print(df)

# Head
print("\nFirst 5 Rows:")
print(df.head())

# Shape
print("\nShape:")
print(df.shape)

# Data Types
print("\nData Types:")
print(df.dtypes)

# Column Names
print("\nColumn Names:")
print(df.columns)

# Summary Statistics
print("\nStatistics:")
print(df.describe())

# Maximum Marks
print("\nHighest Marks:")
print(df["marks"].max())

# Minimum Marks
print("\nLowest Marks:")
print(df["marks"].min())

# Average Marks
print("\nAverage Marks:")
print(df["marks"].mean())

# Sort by Marks
print("\nSorted by Marks:")
print(df.sort_values(by="marks", ascending=False))

# Add Result Column
df["result"] = df["marks"].apply(lambda x: "Pass" if x >= 50 else "Fail")

# Count Pass and Fail
print("\nResult Count:")
print(df["result"].value_counts())

# Students who Passed
print("\nPassed Students:")
print(df[df["result"] == "Pass"])

# Students who Failed
print("\nFailed Students:")
print(df[df["result"] == "Fail"])

# Final DataFrame
print("\n===== FINAL DATAFRAME =====")
print(df)