import pandas as pd

# Load Dataset
df = pd.read_csv(
    r"C:\Users\supradeep\OneDrive\Desktop\python_internship\day3\student-mat.csv",
    sep=";"
)

print("=" * 50)
print("STUDENT PERFORMANCE ANALYSIS REPORT")
print("=" * 50)

# Dataset Overview
print("\nDataset Shape:", df.shape)
print("Column Names:")
print(df.columns.tolist())

# Average G3 by Study Time
print("\n1. AVERAGE G3 BY STUDY TIME")
study_avg = df.groupby("studytime")["G3"].mean()
print(study_avg)

# Additional Statistics by Study Time
print("\nStudy Time Statistics")
study_stats = df.groupby("studytime")["G3"].agg(
    ["count", "mean", "min", "max", "std"]
)
print(study_stats)

# Average G3 by Gender
print("\n2. AVERAGE G3 BY GENDER")
gender_avg = df.groupby("sex")["G3"].mean()
print(gender_avg)

# Gender Statistics
print("\nGender Statistics")
gender_stats = df.groupby("sex")["G3"].agg(
    ["count", "mean", "min", "max", "std"]
)
print(gender_stats)

# Top 5 Students
print("\n3. TOP 5 STUDENTS BY G3")
top5 = df.sort_values(by="G3", ascending=False).head(5)
print(top5[["school", "sex", "age", "studytime", "G3"]])

# Bottom 5 Students
print("\n4. BOTTOM 5 STUDENTS BY G3")
bottom5 = df.sort_values(by="G3").head(5)
print(bottom5[["school", "sex", "age", "studytime", "G3"]])

# Overall Statistics
print("\n5. OVERALL G3 STATISTICS")
print("Average Grade :", round(df["G3"].mean(), 2))
print("Median Grade  :", df["G3"].median())
print("Highest Grade :", df["G3"].max())
print("Lowest Grade  :", df["G3"].min())
print("Std Deviation :", round(df["G3"].std(), 2))

# Grade Categories
df["Result"] = df["G3"].apply(
    lambda x: "Pass" if x >= 10 else "Fail"
)

print("\n6. PASS / FAIL COUNT")
print(df["Result"].value_counts())

# Crosstab
print("\n7. PASS / FAIL BY GENDER")
print(pd.crosstab(df["sex"], df["Result"]))

# Students with Highest Grade
print("\n8. STUDENTS WITH HIGHEST GRADE")
highest = df[df["G3"] == df["G3"].max()]
print(highest[["school", "sex", "age", "studytime", "G3"]])

# Summary
print("\n" + "=" * 50)
print("SUMMARY REPORT")
print("=" * 50)

best_study = study_avg.idxmax()
best_avg = study_avg.max()

print(f"Best Study Time Group : {best_study}")
print(f"Average Grade         : {best_avg:.2f}")

print(f"Overall Average Grade : {df['G3'].mean():.2f}")
print(f"Total Students        : {len(df)}")
print(f"Pass Percentage       : {(df['Result']=='Pass').mean()*100:.2f}%")
print(f"Fail Percentage       : {(df['Result']=='Fail').mean()*100:.2f}%")