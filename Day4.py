# Pandas Fundamentals
# Import Pandas, Load Student Score Dataset,
# Explore Rows, Columns, and Dataset Information


import pandas as pd

# Load Dataset

# Make sure 'student_scores.csv' is in the same folder as this Python file.

df = pd.read_csv("student_scores.csv")

print("===== Dataset Loaded Successfully =====")


# Display First 5 Rows

print("\n----- First 5 Rows -----")
print(df.head())


# Display Last 5 Rows

print("\n----- Last 5 Rows -----")
print(df.tail())


# Display Number of Rows and Columns

print("\n----- Dataset Shape -----")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])


# Display Column Names

print("\n----- Column Names -----")
print(df.columns)


# Display Dataset Information

print("\n----- Dataset Information -----")
print(df.info())


# Display Data Types

print("\n----- Data Types -----")
print(df.dtypes)


# Display Summary Statistics

print("\n----- Summary Statistics -----")
print(df.describe())


# Check Missing Values

print("\n----- Missing Values -----")
print(df.isnull().sum())


# Display a Specific Column

# Replace 'Score' with your actual column name if different.

print("\n----- Score Column -----")
print(df["Score"])


# Display Multiple Columns

# Replace column names according to your dataset.

print("\n----- Student Name and Score -----")
print(df[["Name", "Score"]])



print("\nDataset Loaded Successfully!")