#!/usr/bin/python3
"""Unit tests for Amenity class"""

import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):

    def test_instance_creation(self):
        obj = Amenity()
        self.assertIsInstance(obj, Amenity)

    def test_attributes(self):
        obj = Amenity()
        self.assertTrue(hasattr(obj, "name"))

if __name__ == "__main__":
    unittest.main()
