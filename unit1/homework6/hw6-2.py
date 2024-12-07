class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        print(self.height*self.width)

rect1 = Rectangle(1920, 1080)
rect2 = Rectangle(1280, 720)
rect1.calculate_area()
rect2.calculate_area()
