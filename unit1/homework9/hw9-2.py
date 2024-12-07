class Shape:
    pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

class CalculateArea:
    @staticmethod
    def calculate_area(shape):
        if shape.__class__ == Circle:
            return 3.14 * shape.radius ** 2
        elif shape.__class__ == Rectangle:
            return shape.width * shape.height
        else:
            return 'Formula not found'

circle = Circle(6)

rectangle = Rectangle(3, 7)

print(f'Circle area: {CalculateArea.calculate_area(circle)}')
print(f'Rectangle area: {CalculateArea.calculate_area(rectangle)}')
