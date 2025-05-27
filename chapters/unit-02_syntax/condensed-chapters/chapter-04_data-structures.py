# Chapter 4: Data Structures
# Lists, Dictionaries, Tuples, and Sets

# 4.1 Lists
# Creating and accessing lists
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]

# Accessing elements
print(numbers[0])  # First element: 1
print(numbers[-1])  # Last element: 5
print(fruits[1:3])  # Slicing: ['banana', 'cherry']

# Modifying lists
fruits.append("orange")  # Add to end
fruits.insert(1, "kiwi")  # Insert at position
fruits.remove("banana")  # Remove by value
popped = fruits.pop()  # Remove and return last
fruits[0] = "grape"  # Change by index

print(f"Modified fruits: {fruits}")

# List methods
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()  # Sort in place
print(f"Sorted: {numbers}")
print(f"Count of 1: {numbers.count(1)}")
print(f"Index of 4: {numbers.index(4)}")

# List comprehensions
squares = [x**2 for x in range(5)]
evens = [x for x in range(10) if x % 2 == 0]
print(f"Squares: {squares}")
print(f"Evens: {evens}")

# 4.2 Dictionaries
# Creating dictionaries
person = {"name": "Alice", "age": 30, "city": "New York"}
student = {}  # Empty dictionary
student["name"] = "Bob"
student["grade"] = "A"

# Accessing and modifying
print(person["name"])  # Alice
person["age"] = 31  # Update
person["job"] = "Engineer"  # Add new key
del person["city"]  # Remove key-value pair

# Dictionary methods
print(person.keys())  # dict_keys(['name', 'age', 'job'])
print(person.values())  # dict_values(['Alice', 31, 'Engineer'])
print(person.items())  # dict_items([('name', 'Alice'), ...])

# Safe access with get()
phone = person.get("phone", "Not available")
print(f"Phone: {phone}")

# Iterating through dictionaries
for key in person:
    print(f"{key}: {person[key]}")

for key, value in person.items():
    print(f"{key} = {value}")

# Dictionary comprehensions
squared_dict = {x: x**2 for x in range(5)}
print(f"Squared dict: {squared_dict}")

# 4.3 Tuples
# Creating tuples
coordinates = (10, 20)
rgb_color = (255, 128, 0)
single_item = (42,)  # Note the comma
empty_tuple = ()

# Accessing elements
print(coordinates[0])  # 10
print(rgb_color[-1])  # 0

# Tuple packing and unpacking
point = 3, 4, 5  # Packing
x, y, z = point  # Unpacking
print(f"x={x}, y={y}, z={z}")

# Tuple methods
numbers = (1, 2, 3, 2, 1)
print(f"Count of 2: {numbers.count(2)}")
print(f"Index of 3: {numbers.index(3)}")

# Multiple assignment using tuples
a, b = 1, 2
a, b = b, a  # Swap values
print(f"After swap: a={a}, b={b}")

# 4.4 Sets
# Creating sets
unique_numbers = {1, 2, 3, 2, 1}  # Duplicates removed
print(f"Unique numbers: {unique_numbers}")

fruits = set(["apple", "banana", "apple"])
print(f"Unique fruits: {fruits}")

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
