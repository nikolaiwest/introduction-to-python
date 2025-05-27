# Chapter 5: Functions and Parameters
# Function Fundamentals, Arguments, Advanced Concepts, and Best Practices


# 5.1 Function Fundamentals
# Basic function definition and calling
def say_hello():
    print("Hello, World!")


def greet_user(name):
    """Display a personalized greeting."""
    return f"Hello, {name}!"


# Function with multiple parameters and return value
def add_numbers(a, b):
    """Add two numbers and return the result."""
    result = a + b
    return result


# Calling functions
say_hello()
message = greet_user("Alice")
print(message)
sum_result = add_numbers(5, 3)
print(f"Sum: {sum_result}")

# Variable scope demonstration
x = 10  # Global variable


def print_x():
    x = 20  # Local variable
    print(f"Local x: {x}")


print_x()  # Local x: 20
print(f"Global x: {x}")  # Global x: 10


# 5.2 Function Arguments
# Positional arguments
def make_coffee(coffee_type, size):
    return f"Making a {size} {coffee_type}"


print(make_coffee("latte", "large"))


# Keyword arguments
def create_user(username, email, age, is_active=True):
    return {"username": username, "email": email, "age": age, "is_active": is_active}


# Different ways to call with keyword arguments
user1 = create_user("john_doe", "john@example.com", 25)
user2 = create_user(username="jane_doe", email="jane@example.com", age=28)
user3 = create_user("bob_doe", email="bob@example.com", age=22, is_active=False)


# Default parameters
def greet(name, greeting="Hello", punctuation="!"):
    return f"{greeting}, {name}{punctuation}"


print(greet("Alice"))  # Hello, Alice!
print(greet("Bob", "Hi"))  # Hi, Bob!
print(greet("Charlie", "Hey", "..."))  # Hey, Charlie...
print(greet("David", punctuation="?"))  # Hello, David?


# Variable-length arguments (*args)
def calculate_average(*numbers):
    """Calculate average of any number of values."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


print(calculate_average(2, 4, 6))  # 4.0
print(calculate_average(1, 2, 3, 4, 5))  # 3.0


# Variable keyword arguments (**kwargs)
def create_profile(**info):
    """Create profile from arbitrary keyword arguments."""
    return info


profile = create_profile(name="Alice", age=30, occupation="Engineer", city="NYC")
print(profile)


# Combining all argument types
def process_order(order_id, *items, discount=0, **details):
    print(f"Order ID: {order_id}")
    print(f"Items: {items}")
    print(f"Discount: {discount}%")
    print(f"Details: {details}")


process_order(
    "12345", "Coffee", "Muffin", discount=10, payment="Credit", delivery="Express"
)

# 5.3 Advanced Function Concepts
# Lambda functions (anonymous functions)
square = lambda x: x**2
print(f"Square of 5: {square(5)}")

# Lambda with multiple arguments
rectangle_area = lambda length, width: length * width
print(f"Rectangle area: {rectangle_area(5, 3)}")

# Lambda with higher-order functions
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Squared: {squared_numbers}")
print(f"Evens: {even_numbers}")


# Recursive functions
def factorial(n):
    """Calculate factorial using recursion."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """Calculate nth Fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(f"Factorial of 5: {factorial(5)}")  # 120
print(f"Fibonacci of 7: {fibonacci(7)}")  # 13


# Higher-order functions
def apply_to_list(numbers, operation):
    """Apply an operation to each number in a list."""
    return [operation(num) for num in numbers]


def double(x):
    return x * 2


def cube(x):
    return x**3


numbers = [1, 2, 3, 4, 5]
doubled = apply_to_list(numbers, double)
cubed = apply_to_list(numbers, cube)
print(f"Doubled: {doubled}")
print(f"Cubed: {cubed}")


# Closures (functions that remember their environment)
def create_multiplier(factor):
    """Create a function that multiplies by a specific factor."""

    def multiplier(x):
        return x * factor

    return multiplier


double_func = create_multiplier(2)
triple_func = create_multiplier(3)
print(f"Double 10: {double_func(10)}")  # 20
print(f"Triple 10: {triple_func(10)}")  # 30


# 5.4 Function Best Practices
# Single Responsibility Principle - each function does one thing
def validate_email(email):
    """Validate email format (simplified)."""
    return "@" in email and "." in email


def format_name(first_name, last_name):
    """Format a person's name."""
    return f"{first_name.title()} {last_name.title()}"


def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index.

    Args:
        weight (float): Weight in kilograms
        height (float): Height in meters

    Returns:
        float: BMI value

    Raises:
        ValueError: If weight or height is negative
    """
    if weight <= 0 or height <= 0:
        raise ValueError("Weight and height must be positive")
    return weight / (height**2)


# Error handling in functions
def safe_divide(a, b):
    """Safely divide two numbers."""
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except TypeError:
        print("Error: Both arguments must be numbers")
        return None


print(safe_divide(10, 2))  # 5.0
print(safe_divide(10, 0))  # None (with error message)
