#!/usr/bin/python3
"""Unit tests for User class"""

import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """Tests for User class"""

    def test_instance_creation(self):
        """Test that a User instance is created properly"""
        obj = User()
        self.assertIsInstance(obj, User)

    def test_attributes(self):
        """Test that the instance has correct attributes"""
        obj = User()
        self.assertTrue(hasattr(obj, "email"))
        self.assertTrue(hasattr(obj, "password"))
        self.assertTrue(hasattr(obj, "first_name"))
        self.assertTrue(hasattr(obj, "last_name"))

if __name__ == "__main__":
    unittest.main()
