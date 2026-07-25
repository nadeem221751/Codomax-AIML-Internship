# Python Basics Task
# Variables, Data Types, Operators,
# Loops, Functions, and Simple Programs

# Variables and Data Types

name = "Mahek"          # String
age = 22                # Integer
height = 5.4            # Float
is_student = True       # Boolean

print("----- Variables and Data Types -----")
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)

# Operators

a = 20
b = 5

print("\n----- Operators -----")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponent:", a ** b)
print("Floor Division:", a // b)

# Conditional Statement

print("\n----- If-Else Example -----")
number = 10

if number % 2 == 0:
    print(number, "is Even")
else:
    print(number, "is Odd")


# For Loop

print("\n----- For Loop -----")
for i in range(1, 6):
    print("Number:", i)

# While Loop

print("\n----- While Loop -----")
count = 1

while count <= 5:
    print("Count:", count)
    count += 1


# Functions

print("\n----- Functions -----")

def greet(name):
    print("Hello,", name)

greet("Mahek")

def add(x, y):
    return x + y

result = add(15, 25)
print("Addition Result:", result)

# Simple Program 1
# Sum of First 10 Numbers

print("\n----- Sum of First 10 Numbers -----")

total = 0
for i in range(1, 11):
    total += i

print("Sum =", total)


# Simple Program 2
# Multiplication Table

print("\n----- Multiplication Table of 5 -----")

for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")


# Simple Program 3
# Factorial

print("\n----- Factorial -----")

num = 5
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial of", num, "=", factorial)


# Simple Program 4
# Find Largest Number

print("\n----- Largest Number -----")

x = 15
y = 8

if x > y:
    print(x, "is larger")
else:
    print(y, "is larger")

# End of Program
print("\nPython Basics Task Completed Successfully!")