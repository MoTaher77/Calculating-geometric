import math

class Shape:
    def calculate_perimeter(self):
        pass

    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return math.pi * self.radius**2


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3

    def calculate_area(self):
        # Using Heron's formula to calculate the area of a triangle
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def calculate_area(self):
        return self.length * self.width


# Function to get user input for Circle
def get_circle_input():
    radius = float(input("Enter the radius of the circle: "))
    circle = Circle(radius)
    return circle


# Function to get user input for Triangle
def get_triangle_input():
    side1 = float(input("Enter the length of side 1: "))
    side2 = float(input("Enter the length of side 2: "))
    side3 = float(input("Enter the length of side 3: "))
    triangle = Triangle(side1, side2, side3)
    return triangle


# Function to get user input for Rectangle
def get_rectangle_input():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    rectangle = Rectangle(length, width)
    return rectangle


# Test the code
print("Select a shape:")
print("1. Circle")
print("2. Triangle")
print("3. Rectangle")

choice = input("Enter your choice (1-3): ")

if choice == "1":
    circle = get_circle_input()
    print("Circle Perimeter:", circle.calculate_perimeter())
    print("Circle Area:", circle.calculate_area())

elif choice == "2":
    triangle = get_triangle_input()
    print("Triangle Perimeter:", triangle.calculate_perimeter())
    print("Triangle Area:", triangle.calculate_area())

elif choice == "3":
    rectangle = get_rectangle_input()
    print("Rectangle Perimeter:", rectangle.calculate_perimeter())
    print("Rectangle Area:", rectangle.calculate_area())

else:
    print("Invalid choice.")