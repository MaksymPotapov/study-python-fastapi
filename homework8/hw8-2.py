from abc import ABC, abstractclassmethod


class Shape(ABC):

    @abstractclassmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return self.base * self.height / 2


circle = Circle(3)
rectangle = Rectangle(3, 5)
triangle = Triangle(5, 3)
print(f'Circle: {circle.calculate_area()}m2, Rectangle: {rectangle.calculate_area()}m2, Triangle: {triangle.calculate_area()}m2')