# Data Cleaning Tasks using Pandas
# Handle Missing Values, Remove Duplicates,
# and Understand Dataset Statistics

import pandas as pd


# Load Dataset

df = pd.read_csv("student_scores.csv")

print("===== Original Dataset =====")
print(df)

# Dataset Information

print("\n----- Dataset Information -----")
df.info()


# Check Missing Values

print("\n----- Missing Values -----")
print(df.isnull().sum())


# Fill Missing Values

# Fill numeric columns with their mean

numeric_columns = df.select_dtypes(include=["number"]).columns

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].mean())

print("\nMissing values handled successfully.")


# Check Duplicate Rows

print("\n----- Duplicate Rows -----")
print("Duplicate Rows:", df.duplicated().sum())


# Remove Duplicate Rows

df = df.drop_duplicates()

print("Duplicates removed successfully.")


# Dataset Statistics

print("\n----- Dataset Statistics -----")
print(df.describe())


# Check Data Types

print("\n----- Data Types -----")
print(df.dtypes)


# Check Dataset Shape

print("\n----- Dataset Shape -----")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])


# Verify Missing Values Again

print("\n----- Missing Values After Cleaning -----")
print(df.isnull().sum())


# Save Clean Dataset

df.to_csv("student_scores_clean.csv", index=False)

print("\nClean dataset saved as 'student_scores_clean.csv'.")


# Display Clean Dataset

print("\n===== Clean Dataset =====")
print(df)

print("\nExpected Outcome: Clean Dataset Prepared Successfully!")