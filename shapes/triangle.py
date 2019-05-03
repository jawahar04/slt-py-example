"""
Author: Jawahar Siva
File: triangle.py
Purpose: Defines a Triangle object, inherited from the abstract class Shape.
"""
import math
from shapes.shape import Shape


class Triangle(Shape):
    """
    Represents a Triangle shape, and contains 3 sides.
    """
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        """
        Compute the area using the formula sqrt(p*(p-side1))*(p-side2)*(p-side3))
        where p = perimeter
        see: https://www.mathopenref.com/heronsformula.html
        """
        p = self.perimeter() / 2
        a = math.sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3))

        return a

    def perimeter(self):
        """
        Compute the perimeter using the formula side1 + side2 + side3
        see: https://www.mathopenref.com/triangleperimeter.html
        """
        return self.side1 + self.side2 + self.side3

    def is_equilateral(self):
        """
        Determine if the Triangle is an equilateral triangle, which is true if all 3 sides are equal.
        """
        return self.side1 == self.side2 and self.side1 == self.side3
