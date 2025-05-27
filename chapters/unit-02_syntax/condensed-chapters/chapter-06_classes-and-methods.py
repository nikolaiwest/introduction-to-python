# Chapter 6: Classes and Methods
# Object-Oriented Programming in Python


# 6.1 Classes and Objects Fundamentals
# Basic class definition
class Person:
    """A class representing a person."""

    # Class attribute (shared by all instances)
    species = "Human"

    def __init__(self, name, age):
        """Initialize a new Person object."""
        self.name = name  # Instance attributes
        self.age = age

    def greet(self):
        """Return a greeting message."""
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    def have_birthday(self):
        """Increment age by 1."""
        self.age += 1
        return f"{self.name} is now {self.age} years old."


# Creating objects (instances)
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print(person1.greet())
print(person2.greet())
print(person1.have_birthday())

# Accessing class and instance attributes
print(f"Species: {Person.species}")  # From class
print(f"Species: {person1.species}")  # From instance


# Bank account example demonstrating encapsulation
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self._balance = balance  # "Protected" attribute

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return self._balance
        raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False


account = BankAccount("12345", 1000)
account.deposit(500)
account.withdraw(200)
print(f"Balance: ${account.get_balance()}")


# 6.2 Special Methods and Operators
class Vector:
    """A 2D vector class demonstrating special methods."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """String representation for users."""
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        """String representation for developers."""
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        """Add two vectors."""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Subtract two vectors."""
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """Multiply vector by scalar."""
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        """Check if two vectors are equal."""
        return self.x == other.x and self.y == other.y

    def __len__(self):
        """Return magnitude of vector."""
        return int((self.x**2 + self.y**2) ** 0.5)


# Using special methods
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1)  # Calls __str__
print(v1 + v2)  # Calls __add__
print(v1 - v2)  # Calls __sub__
print(v1 * 2)  # Calls __mul__
print(v1 == v2)  # Calls __eq__
print(len(v1))  # Calls __len__


# Container behavior example
class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def __len__(self):
        return len(self.songs)

    def __getitem__(self, index):
        return self.songs[index]

    def __contains__(self, song):
        return song in self.songs


playlist = Playlist()
playlist.add_song("Song 1")
playlist.add_song("Song 2")
print(len(playlist))  # 2
print(playlist[0])  # Song 1
print("Song 1" in playlist)  # True


# 6.3 Properties and Access Control
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Get the radius."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Set the radius with validation."""
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @property
    def area(self):
        """Calculate area (read-only property)."""
        return 3.14159 * self._radius**2

    @property
    def diameter(self):
        """Calculate diameter (read-only property)."""
        return self._radius * 2


circle = Circle(5)
print(f"Area: {circle.area}")
print(f"Diameter: {circle.diameter}")
circle.radius = 10  # Uses setter
print(f"New area: {circle.area}")


# Class methods and static methods
class Employee:
    company_name = "TechCorp"
    all_employees = []

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.all_employees.append(self)

    @classmethod
    def set_company_name(cls, name):
        """Change company name for all employees."""
        cls.company_name = name

    @classmethod
    def from_string(cls, employee_string):
        """Alternative constructor from string."""
        name, salary_str = employee_string.split(",")
        return cls(name, float(salary_str))

    @staticmethod
    def is_workday(day):
        """Check if a day is a workday."""
        return day not in ["Saturday", "Sunday"]


emp1 = Employee("Alice", 60000)
emp2 = Employee.from_string("Bob,70000")  # Class method
Employee.set_company_name("GlobalTech")  # Class method
print(Employee.is_workday("Monday"))  # Static method


# 6.4 Inheritance and Polymorphism
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return "Some generic animal sound"

    def info(self):
        return f"{self.name} is {self.age} years old"


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # Call parent constructor
        self.breed = breed

    def speak(self):
        """Override parent method."""
        return "Woof!"

    def info(self):
        """Extend parent method."""
        basic_info = super().info()
        return f"{basic_info} and is a {self.breed}"

    def fetch(self):
        """New method specific to dogs."""
        return f"{self.name} is fetching!"


class Cat(Animal):
    def speak(self):
        return "Meow!"

    def climb(self):
        return f"{self.name} is climbing!"


# Using inheritance
dog = Dog("Buddy", 5, "Golden Retriever")
cat = Cat("Whiskers", 3)

print(dog.speak())  # Woof! (overridden)
print(dog.info())  # Extended info
print(dog.fetch())  # Dog-specific method

# Polymorphism - same interface, different behavior
animals = [dog, cat]
for animal in animals:
    print(f"{animal.name} says: {animal.speak()}")


# Multiple inheritance example
class FlyingMixin:
    def fly(self):
        return f"{self.name} is flying!"


class SwimmingMixin:
    def swim(self):
        return f"{self.name} is swimming!"


class Duck(Animal, FlyingMixin, SwimmingMixin):
    def speak(self):
        return "Quack!"


duck = Duck("Donald", 2)
print(duck.speak())  # Quack!
print(duck.fly())  # Donald is flying!
print(duck.swim())  # Donald is swimming!

# 6.5 Modern Class Patterns
# Dataclasses - simplified class creation
from dataclasses import dataclass, field
from typing import List


@dataclass
class Point:
    x: float
    y: float

    def distance(self):
        return (self.x**2 + self.y**2) ** 0.5


@dataclass
class Rectangle:
    width: float
    height: float
    color: str = "red"
    tags: List[str] = field(default_factory=list)

    def area(self):
        return self.width * self.height


# Using dataclasses
point = Point(3, 4)
rect = Rectangle(5, 10, "blue", ["shape", "geometry"])

print(point)  # Point(x=3, y=4)
print(f"Distance: {point.distance()}")
print(f"Rectangle area: {rect.area()}")

# Named tuples
from typing import NamedTuple


class Coordinate(NamedTuple):
    x: float
    y: float
    z: float

    def magnitude(self):
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5


coord = Coordinate(1, 2, 3)
print(f"Coordinate: {coord}")
print(f"Magnitude: {coord.magnitude()}")


# Composition vs Inheritance example
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return "Engine started"


class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine  # Composition: Car HAS an Engine

    def start(self):
        return f"{self.make} {self.model}: {self.engine.start()}"


# Using composition
engine = Engine(200)
car = Car("Toyota", "Camry", engine)
print(car.start())
