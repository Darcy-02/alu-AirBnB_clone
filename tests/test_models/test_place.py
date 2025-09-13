#!/usr/bin/python3
"""Unit tests for Place class"""

import unittest
from models.place import Place

class TestPlace(unittest.TestCase):

    def test_instance_creation(self):
        obj = Place()
        self.assertIsInstance(obj, Place)

    def test_attributes(self):
        obj = Place()
        self.assertTrue(hasattr(obj, "name"))
        self.assertTrue(hasattr(obj, "description"))
        self.assertTrue(hasattr(obj, "number_rooms"))
        self.assertTrue(hasattr(obj, "number_bathrooms"))
        self.assertTrue(hasattr(obj, "max_guest"))
        self.assertTrue(hasattr(obj, "price_by_night"))
        self.assertTrue(hasattr(obj, "latitude"))
        self.assertTrue(hasattr(obj, "longitude"))

if __name__ == "__main__":
    unittest.main()
