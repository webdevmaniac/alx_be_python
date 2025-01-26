import math

class Shape:
    def area(self):
        """
        Method to calculate the area of the shape. Should be overridden by subclasses.
        """
        raise NotImplementedError("The area method must be overridden in a subclass.")

class Rectangle(Shape):
    def __init__(self, length, width):
        """
        Initialize a Rectangle instance.
        :param length: The length of the rectangle.
        :param width: The width of the rectangle.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Calculate the area of the rectangle.
        :return: The area as length × width.
        """
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        """
        Initialize a Circle instance.
        :param radius: The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle.
        :return: The area as π × radius².
        """
        return math.pi * self.radius ** 2
