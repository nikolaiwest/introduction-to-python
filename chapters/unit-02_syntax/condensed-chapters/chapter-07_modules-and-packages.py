# Chapter 7: Modules and Packages
# Importing, Using Standard Library, and Module Management

# 7.1 Using Modules
# Basic import
import math

print(f"Pi: {math.pi}")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Ceiling of 4.3: {math.ceil(4.3)}")

# Import with alias
import random as rnd

print(f"Random number: {rnd.randint(1, 10)}")
print(f"Random choice: {rnd.choice(['red', 'green', 'blue'])}")

# Import specific items
from datetime import date, datetime, timedelta

current_time = datetime.now()
today = date.today()
tomorrow = today + timedelta(days=1)

print(f"Current time: {current_time}")
print(f"Today: {today}")
print(f"Tomorrow: {tomorrow}")

# Multiple imports from same module
from os import getcwd, listdir, path

print(f"Current directory: {getcwd()}")
print(f"Directory contents: {listdir('.')[:3]}")  # First 3 items
print(f"Path exists: {path.exists('.')}")

# Standard library modules demonstration
# JSON module
import json

data = {"name": "Alice", "age": 30, "skills": ["Python", "JavaScript"]}
json_string = json.dumps(data, indent=2)
print("JSON string:")
print(json_string)
parsed_data = json.loads(json_string)
print(f"Parsed name: {parsed_data['name']}")

# Collections module
from collections import Counter, defaultdict, namedtuple

# Counter for counting items
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_count = Counter(words)
print(f"Word count: {word_count}")
print(f"Most common: {word_count.most_common(2)}")

# defaultdict for dictionaries with default values
dd = defaultdict(list)
dd["fruits"].append("apple")
dd["vegetables"].append("carrot")
print(f"Default dict: {dict(dd)}")

# CSV module example
import csv
import io

# Create sample CSV data
csv_data = """name,age,city
Alice,30,New York
Bob,25,San Francisco
Charlie,35,Chicago"""

# Reading CSV
csv_reader = csv.DictReader(io.StringIO(csv_data))
for row in csv_reader:
    print(f"{row['name']} is {row['age']} years old")

# Regular expressions
import re

text = "Contact us at support@example.com or sales@company.org"
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
emails = re.findall(email_pattern, text)
print(f"Found emails: {emails}")

# pathlib for modern path handling
from pathlib import Path
from urllib.parse import urlencode

# 7.2 Working with Packages
# urllib package for web requests
from urllib.request import urlopen

# Note: This makes an actual web request
# try:
#     response = urlopen('http://httpbin.org/json')
#     data = json.loads(response.read().decode())
#     print(f"Response: {data}")
# except Exception as e:
#     print(f"Request failed: {e}")


current_path = Path(".")
print(f"Current path: {current_path.absolute()}")
print(f"Is directory: {current_path.is_dir()}")

# Create path objects
home = Path.home()
documents = home / "Documents"
print(f"Documents path: {documents}")

# 7.3 Module Search Path and Error Handling
import sys

print("Python path (first 3 entries):")
for i, path in enumerate(sys.path[:3]):
    print(f"  {i}: {path}")

# Checking if module exists
import importlib.util


def module_exists(module_name):
    """Check if a module can be imported."""
    return importlib.util.find_spec(module_name) is not None


# Test with existing and non-existing modules
modules_to_check = ["os", "sys", "nonexistent_module", "json"]
for module in modules_to_check:
    exists = module_exists(module)
    print(f"Module '{module}' exists: {exists}")

# Graceful import handling
try:
    import numpy as np

    print("NumPy is available")
    # Could use NumPy-specific functionality here
except ImportError:
    print("NumPy not available, using built-in alternatives")
    # Use built-in alternatives


# Optional imports with fallbacks
def safe_import(module_name, fallback_name=None):
    """Safely import a module with optional fallback."""
    try:
        return __import__(module_name)
    except ImportError:
        if fallback_name:
            try:
                return __import__(fallback_name)
            except ImportError:
                return None
        return None


# Try to import advanced modules with fallbacks
advanced_math = safe_import("numpy", "math")
if advanced_math:
    if hasattr(advanced_math, "array"):
        print("Using NumPy for advanced math")
    else:
        print("Using built-in math module")
else:
    print("No math module available")

# Environment and platform information
import platform
import sys

print(f"\nSystem Information:")
print(f"Python version: {sys.version}")
print(f"Platform: {platform.platform()}")
print(f"Architecture: {platform.architecture()}")
print(f"Processor: {platform.processor()}")

# Working with environment variables
import os

python_path = os.environ.get("PYTHONPATH", "Not set")
home_dir = os.environ.get("HOME", os.environ.get("USERPROFILE", "Unknown"))
print(f"PYTHONPATH: {python_path}")
print(f"Home directory: {home_dir}")

# Package management information
import subprocess
import sys


def get_installed_packages():
    """Get list of installed packages."""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "list"], capture_output=True, text=True
        )
        if result.returncode == 0:
            lines = result.stdout.split("\n")[2:]  # Skip header
            packages = []
            for line in lines:
                if line.strip():
                    parts = line.split()
                    if len(parts) >= 2:
                        packages.append((parts[0], parts[1]))
            return packages[:5]  # Return first 5 packages
        return []
    except Exception:
        return []


packages = get_installed_packages()
if packages:
    print("\nSome installed packages:")
    for name, version in packages:
        print(f"  {name}: {version}")
else:
    print("\nCould not retrieve package information")


# Demonstrate __name__ == "__main__" pattern
def main():
    """Main function demonstrating entry point pattern."""
    print("This runs when the script is executed directly")
    print("Not when it's imported as a module")


if __name__ == "__main__":
    main()
