#!/usr/bin/python3
"""Unit tests for Review class"""

import unittest
from models.review import Review

class TestReview(unittest.TestCase):

    def test_instance_creation(self):
        obj = Review()
        self.assertIsInstance(obj, Review)

    def test_attributes(self):
        obj = Review()
        self.assertTrue(hasattr(obj, "place_id"))
        self.assertTrue(hasattr(obj, "user_id"))
        self.assertTrue(hasattr(obj, "text"))

if __name__ == "__main__":
    unittest.main()
