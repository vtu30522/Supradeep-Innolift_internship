import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Load dataset
folder = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(folder, "student-mat.csv")
df = pd.read_csv(csv_file, sep=";")

# Average grade by study time
avg_grade = df.groupby("studytime")["G3"].mean()

# Data
study_time = avg_grade.index
grades = avg_grade.values

# Mean grade
mean_grade = grades.mean()

# Custom colors
colors = ["red", "blue", "green", "orange"]

# Create figure
plt.figure(figsize=(10, 6))

# Bar chart
bars = plt.bar(
    study_time,
    grades,
    color=colors,
    edgecolor="black",
    linewidth=2
)

# Title
plt.title(
    "Average Grade by Study Time",
    fontsize=16,
    fontweight="bold"
)

# Axis Labels
plt.xlabel("Study Time Category", fontsize=12)
plt.ylabel("Average Final Grade (G3)", fontsize=12)

# Mean Line
plt.axhline(
    y=mean_grade,
    color="purple",
    linestyle="--",
    linewidth=2,
    label=f"Mean Grade = {mean_grade:.2f}"
)

# Grid
plt.grid(
    axis="y",
    linestyle=":",
    alpha=0.7
)

# X Ticks
plt.xticks(study_time)

# Y Limits
plt.ylim(0, max(grades) + 5)

# Add Values on Bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height + 0.2,
        f"{height:.2f}",
        ha="center",
        fontsize=10
    )

# Legend
plt.legend()

# Tight Layout
plt.tight_layout()

# Save Figure
plt.savefig(
    os.path.join(folder, "custom_styled_chart.png"),
    dpi=300
)

# Show Plot
plt.show()

print("Custom Styled Chart saved successfully!")