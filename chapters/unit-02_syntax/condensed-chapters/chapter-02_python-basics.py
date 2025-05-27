# Chapter 2: Python Basics
# Variables, Data Types, Operators, Strings, and Input

# 2.1 Variables and Data Types
age = 25  # Integer
height = 1.75  # Float
name = "Alice"  # String
is_student = True  # Boolean

# Type checking and conversion
print(type(age))  # <class 'int'>
print(type(height))  # <class 'float'>

# Type conversion examples
age_str = str(age)  # Convert to string
height_int = int(height)  # Convert to integer (truncates)
num_from_str = int("123")  # String to integer

# 2.2 Operators
# Arithmetic operators
a, b = 10, 3
print(f"Addition: {a + b}")  # 13
print(f"Subtraction: {a - b}")  # 7
print(f"Multiplication: {a * b}")  # 30
print(f"Division: {a / b}")  # 3.333...
print(f"Floor Division: {a // b}")  # 3
print(f"Modulus: {a % b}")  # 1
print(f"Exponentiation: {a ** b}")  # 1000

# Comparison operators
print(f"Equal: {a == b}")  # False
print(f"Not equal: {a != b}")  # True
print(f"Greater than: {a > b}")  # True
print(f"Less than or equal: {a <= b}")  # False

# Logical operators
print(f"And: {True and False}")  # False
print(f"Or: {True or False}")  # True
print(f"Not: {not True}")  # False

# Assignment operators
x = 5
x += 3  # Same as x = x + 3
x *= 2  # Same as x = x * 2
print(f"Final x: {x}")  # 16

# 2.3 Strings and Input
first_name = "John"
last_name = "Doe"

# String concatenation
full_name = first_name + " " + last_name
print(full_name)

# String methods
print(full_name.upper())  # JOHN DOE
print(full_name.lower())  # john doe
print(full_name.split())  # ['John', 'Doe']
print(len(full_name))  # 8

# String formatting (f-strings)
age = 30
print(f"My name is {full_name} and I am {age} years old.")

# String formatting (older methods)
print("My name is {} and I am {} years old.".format(full_name, age))
print("My name is %s and I am %d years old." % (full_name, age))

# Getting user input
# user_name = input("Enter your name: ")
# user_age = int(input("Enter your age: "))
# print(f"Hello {user_name}, you are {user_age} years old")

# String slicing and indexing
text = "Python"
print(text[0])  # P
print(text[-1])  # n
print(text[1:4])  # yth
print(text[:3])  # Pyt
print(text[2:])  # thon
