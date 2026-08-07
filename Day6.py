# Data Visualization using Matplotlib
# Save Charts to Folder
# Expected Outcome: Basic Charts Created


import pandas as pd
import matplotlib.pyplot as plt
import os

# Load Dataset

df = pd.read_csv("student_scores.csv")


# Create Folder for Charts

folder_name = "charts"

if not os.path.exists(folder_name):
    os.makedirs(folder_name)

print("Charts folder created successfully.")

# Scatter Plot

plt.figure(figsize=(8, 5))
plt.scatter(df["Math"], df["Score"], color="blue", s=80)

plt.title("Scatter Plot: Math vs Score")
plt.xlabel("Math Marks")
plt.ylabel("Score")
plt.grid(True)

plt.savefig(os.path.join(folder_name, "scatter_plot.png"))
plt.show()
plt.close()

# Bar Chart

plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df["Score"], color="green")

plt.title("Bar Chart: Student Scores")
plt.xlabel("Student Name")
plt.ylabel("Score")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(os.path.join(folder_name, "bar_chart.png"))
plt.show()
plt.close()

# Line Chart

plt.figure(figsize=(8, 5))
plt.plot(df["ID"], df["Score"], marker="o", linewidth=2, color="red")

plt.title("Line Chart: Student Scores")
plt.xlabel("Student ID")
plt.ylabel("Score")
plt.grid(True)

plt.savefig(os.path.join(folder_name, "line_chart.png"))
plt.show()
plt.close()

# Completed

print("\nAll charts created successfully!")
print("Charts saved inside the 'charts' folder.")