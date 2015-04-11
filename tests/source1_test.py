"""
Test for source.source1
"""
from source.source1 import get_triangle_type
from unittest import TestCase

class TestGetTriangleType(TestCase):

    def test_get_triangle_equilateral_all_int(self):
        result = get_triangle_type(1, 1, 1)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_all_int(self):
        result = get_triangle_type(1, 2, 3)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_isosceles_all_int(self):
        result = get_triangle_type(2, 2, 3)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_invalid_all_int(self):
        result = get_triangle_type(-1, 2, 3)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_list(self):
        result = get_triangle_type([1,1,1])
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_equilateral_dict(self):
        result = get_triangle_type({"sideone":1,"sidetwo": 1,"sidethree": 1})
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_equilateral_all_float(self):
        result = get_triangle_type(1.0, 1.0, 1.0)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_invalidstring(self):
        result = get_triangle_type("hello", 1, 1)
        self.assertEqual(result, 'invalid')

    

	