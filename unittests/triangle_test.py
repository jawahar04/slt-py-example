"""
Author: Jawahar Siva
File: triangle_test.py
Purpose: Unit tests for the Triangle class.
"""

from unittest import TestCase
from shapes.triangle import Triangle

class TriangleTest(TestCase):
    """
    Defines a test case for the Triangle class.
    """

    def setUp(self):
        """
        Create a few test objects.
        """
        self.side8side10side15 = Triangle(8, 10, 15)
        self.side10side12side15 = Triangle(10, 12, 15)
        self.side5side5side5 = Triangle(5, 5, 5)

    def test_area(self):
        """
        Compare the test triangle area computations to the actual values.
        """
        self.assertEqual(round(self.side8side10side15.area()), 37) #36.9789)
        self.assertEqual(round(self.side10side12side15.area()), 60) #59.8117)
        self.assertEqual(round(self.side5side5side5.area()), 11) #10.8253)

    def test_perimeter(self):
        """
        Compare the test triangle perimeter computations to the actual values.
        """
        self.assertEqual(self.side8side10side15.perimeter(), 33)
        self.assertEqual(self.side10side12side15.perimeter(), 37)
        self.assertEqual(self.side5side5side5.perimeter(), 15)

    def test_is_equilateral(self):
        """
        Confirm or deny if the triangle is an equilateral.
        """
        self.assertFalse(self.side8side10side15.is_equilateral())
        self.assertFalse(self.side10side12side15.is_equilateral())
        self.assertTrue(self.side5side5side5.is_equilateral())
