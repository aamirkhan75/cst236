"""
Test for source.source1
"""
from source.source2 import get_rectangle
from unittest import TestCase

class TestGetRectangleType(TestCase):

    def test_get_square_all_int(self):
        result = get_rectangle(1, 1, 1, 1)
        self.assertEqual(result, 'square')

    def test_get_rectangle_all_int(self):
        result = get_rectangle(1, 2, 1, 2)
        self.assertEqual(result, 'rectangle')

    def test_get_invalid_all_int(self):
        result = get_rectangle("hello", 0, 0, 0)
        self.assertEqual(result, 'invalid')

    def test_get_neither_all_int(self):
        result = get_rectangle(1, 2, 3, 4)
        self.assertEqual(result, 'neither')

    def test_get_invalid_all_int(self):
        result = get_rectangle(-1, -1, -1, -1)
        self.assertEqual(result, 'invalid')

    def test_get_squaretuple_all_int(self):
        result = get_rectangle([1,1,1,1])
        self.assertEqual(result, 'squaretuple')

    def test_get_squaredictionary_all_int(self):
        result = get_rectangle({"sideone":1, "sidetwo":1, "sidethree":1, "sidefour":1})
        self.assertEqual(result, 'squaredictionary')

    

	