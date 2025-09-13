#!/usr/bin/python3
"""Unit tests for City class"""

import unittest
from models.city import City

class TestCity(unittest.TestCase):

    def test_instance_creation(self):
        obj = City()
        self.assertIsInstance(obj, City)

    def test_attributes(self):
        obj = City()
        self.assertTrue(hasattr(obj, "name"))
        self.assertTrue(hasattr(obj, "state_id"))

if __name__ == "__main__":
    unittest.main()
