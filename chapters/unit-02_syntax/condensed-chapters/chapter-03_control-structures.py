# Chapter 3: Control Structures
# Conditionals, Loops, and Exception Handling

# 3.1 Conditionals
# Basic if statement
temperature = 25
if temperature > 20:
    print("It's a warm day!")

# if-else statement
age = 17
if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote yet.")

# if-elif-else statement
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Grade: {grade}")

# Nested conditionals
x = 10
y = 5
if x > 5:
    print("x is greater than 5")
    if y > 5:
        print("y is also greater than 5")
    else:
        print("y is not greater than 5")

# Conditional expressions (ternary operator)
age = 20
status = "adult" if age >= 18 else "minor"
print(f"Status: {status}")

# 3.2 Loops
# For loop with range
for i in range(5):
    print(f"Count: {i}")

# For loop with list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# For loop with string
for char in "Python":
    print(char)

# Range variations
for i in range(2, 8):  # 2 to 7
    print(i, end=" ")
print()

for i in range(1, 10, 2):  # 1 to 9, step 2
    print(i, end=" ")
print()

# While loop
count = 0
while count < 3:
    print(f"While count: {count}")
    count += 1

# Loop control statements
# Break and continue
for i in range(10):
    if i == 3:
        continue  # Skip 3
    if i == 7:
        break  # Stop at 7
    print(i, end=" ")
print()

# Loop with else clause
for i in range(3):
    print(i)
else:
    print("Loop completed normally")

# Nested loops
for i in range(3):
    for j in range(2):
        print(f"({i}, {j})")

# 3.3 Exception Handling
# Basic try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple exception types
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("Please enter a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Try-except-else-finally
try:
    x = int("123")
except ValueError:
    print("Conversion failed")
else:
    print("Conversion successful")
finally:
    print("This always executes")


# Raising exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age


try:
    validate_age(-5)
except ValueError as e:
    print(f"Error: {e}")
