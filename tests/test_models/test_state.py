#!/usr/bin/python3
"""Unit tests for State class"""

import unittest
from models.state import State  # Make sure the class exists

class TestState(unittest.TestCase):
    """Tests for State class"""

    def test_instance_creation(self):
        """Test creating a State instance"""
        obj = State()
        self.assertIsInstance(obj, State)

    def test_attributes(self):
        """Test State has name attribute"""
        obj = State()
        self.assertTrue(hasattr(obj, "name"))

if __name__ == "__main__":
    unittest.main()
