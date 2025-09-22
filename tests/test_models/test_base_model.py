#!/usr/bin/python3
print ("OK")
"""Unit tests for BaseModel class"""

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Tests for BaseModel class"""

    def test_instance_creation(self):
        """Test that a BaseModel instance is created properly"""
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

    def test_attributes(self):
        """Test that the instance has correct attributes"""
        obj = BaseModel()
        self.assertTrue(hasattr(obj, "id"))
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertTrue(hasattr(obj, "updated_at"))

if __name__ == "__main__":
    unittest.main()
