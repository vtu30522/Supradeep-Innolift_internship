import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Get the folder where this Python file is located
folder = os.path.dirname(os.path.abspath(__file__))

# Path to CSV file
csv_file = os.path.join(folder, "student-mat.csv")

# Load dataset
df = pd.read_csv(csv_file, sep=";")

# 1. Average Grade by School
plt.figure(figsize=(6,4))
df.groupby("school")["G3"].mean().plot(kind="bar")
plt.title("Average Grade by School")
plt.ylabel("Average G3")
plt.savefig(os.path.join(folder, "01_grade_by_school.png"))
plt.close()

# 2. G1 vs G3
plt.figure(figsize=(6,4))
plt.scatter(df["G1"], df["G3"])
plt.title("G1 vs G3")
plt.xlabel("G1")
plt.ylabel("G3")
plt.savefig(os.path.join(folder, "02_G1_vs_G3.png"))
plt.close()

# 3. Age Distribution
plt.figure(figsize=(6,4))
plt.hist(df["age"], bins=10)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.savefig(os.path.join(folder, "03_age_distribution.png"))
plt.close()

# 4. Grade Trend
plt.figure(figsize=(6,4))
avg = [df["G1"].mean(), df["G2"].mean(), df["G3"].mean()]
plt.plot(["G1", "G2", "G3"], avg, marker="o")
plt.title("Average Grade Trend")
plt.ylabel("Average Grade")
plt.savefig(os.path.join(folder, "04_grade_trend.png"))
plt.close()

# 5. Grade by Study Time
plt.figure(figsize=(6,4))
df.groupby("studytime")["G3"].mean().plot(kind="bar")
plt.title("Average Grade by Study Time")
plt.ylabel("Average G3")
plt.savefig(os.path.join(folder, "05_grade_by_studytime.png"))
plt.close()

# 6. Grade by Gender
plt.figure(figsize=(6,4))
df.groupby("sex")["G3"].mean().plot(kind="bar")
plt.title("Average Grade by Gender")
plt.ylabel("Average G3")
plt.savefig(os.path.join(folder, "06_grade_by_gender.png"))
plt.close()

# 7. Gender Pie Chart
plt.figure(figsize=(6,6))
df["sex"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Gender Distribution")
plt.ylabel("")
plt.savefig(os.path.join(folder, "07_gender_pie.png"))
plt.close()

# 8. School Pie Chart
plt.figure(figsize=(6,6))
df["school"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("School Distribution")
plt.ylabel("")
plt.savefig(os.path.join(folder, "08_school_pie.png"))
plt.close()

# 9. Study Time vs G3
plt.figure(figsize=(6,4))
plt.scatter(df["studytime"], df["G3"])
plt.title("Study Time vs G3")
plt.xlabel("Study Time")
plt.ylabel("G3")
plt.savefig(os.path.join(folder, "09_studytime_vs_G3.png"))
plt.close()

# 10. Absences vs G3
plt.figure(figsize=(6,4))
plt.scatter(df["absences"], df["G3"])
plt.title("Absences vs G3")
plt.xlabel("Absences")
plt.ylabel("G3")
plt.savefig(os.path.join(folder, "10_absences_vs_G3.png"))
plt.close()

# 11. G3 Distribution
plt.figure(figsize=(6,4))
plt.hist(df["G3"], bins=10)
plt.title("G3 Grade Distribution")
plt.xlabel("G3")
plt.ylabel("Frequency")
plt.savefig(os.path.join(folder, "11_G3_distribution.png"))
plt.close()

# 12. Correlation Heatmap
plt.figure(figsize=(12,8))
sns.heatmap(
    df.select_dtypes(include="number").corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation Heatmap")
plt.savefig(os.path.join(folder, "12_correlation_heatmap.png"))
plt.close()
