# NumPy Fundamentals
# Arrays, Indexing, Mathematical Operations,
# and Array-Based Calculations

import numpy as np  #import

# Create NumPy Arrays

print("----- Creating Arrays -----")

arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])

print("1D Array:")
print(arr1)

print("\n2D Array:")
print(arr2)

# Array Properties

print("\n----- Array Properties -----")

print("Shape:", arr2.shape)
print("Dimensions:", arr2.ndim)
print("Size:", arr2.size)
print("Data Type:", arr2.dtype)


# Indexing

print("\n----- Indexing -----")

print("First Element:", arr1[0])
print("Last Element:", arr1[-1])
print("Element at Row 2 Column 3:", arr2[1, 2])

# Slicing

print("\n----- Slicing -----")

print("First Three Elements:", arr1[:3])
print("Last Two Elements:", arr1[-2:])
print("First Row:", arr2[0])
print("Second Column:", arr2[:, 1])


# Mathematical Operations

print("\n----- Mathematical Operations -----")

a = np.array([5, 10, 15])
b = np.array([2, 4, 6])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Square:", a ** 2)


# Aggregate Functions

print("\n----- Aggregate Functions -----")

print("Sum:", np.sum(a))
print("Mean:", np.mean(a))
print("Maximum:", np.max(a))
print("Minimum:", np.min(a))
print("Standard Deviation:", np.std(a))


# Reshape Array

print("\n----- Reshape -----")

numbers = np.arange(1, 13)

matrix = numbers.reshape(3, 4)

print(matrix)


# Array-Based Calculations

print("\n----- Array Calculations -----")

marks = np.array([75, 80, 90, 65, 88])

print("Marks:", marks)
print("Total Marks:", np.sum(marks))
print("Average Marks:", np.mean(marks))
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))


# Element-wise Operations

print("\n----- Element-wise Operations -----")

print("Marks + 5:", marks + 5)
print("Marks * 2:", marks * 2)


# Filtering Arrays

print("\n----- Filtering -----")

print("Marks Greater Than 80:")
print(marks[marks > 80])


# Random Numbers

print("\n----- Random Array -----")

random_array = np.random.randint(1, 101, size=(3, 3))

print(random_array)


# Matrix Operations

print("\n----- Matrix Operations -----")

matrix1 = np.array([[1, 2],
                    [3, 4]])

matrix2 = np.array([[5, 6],
                    [7, 8]])

print("Matrix Addition:")
print(matrix1 + matrix2)

print("\nMatrix Multiplication:")
print(np.dot(matrix1, matrix2))


# End

print("\nNumPy Fundamentals Completed Successfully!")