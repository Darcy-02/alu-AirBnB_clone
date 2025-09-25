#!/usr/bin/python3
"""Unit tests for FileStorage class"""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Setup for tests"""
        self.storage = FileStorage()
        # Clean file before tests
        if os.path.exists("file.json"):
            os.remove("file.json")
        # Reset the class attribute properly
        FileStorage._FileStorage__objects = {}
        # Also reset the instance
        self.storage._FileStorage__objects = {}

    def test_all_empty(self):
        """all() returns empty dict initially"""
        self.assertEqual(self.storage.all(), {})

    def test_new_and_all(self):
        """Test adding a new object"""
        obj = BaseModel()
        self.storage.new(obj)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], obj)

    def test_save_and_reload(self):
        """Test saving to file and reloading"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        # Clear objects and reload
        FileStorage._FileStorage__objects = {}
        self.storage.reload()
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key].id, obj.id)

    def tearDown(self):
        """Clean up after tests"""
        if os.path.exists("file.json"):
            os.remove("file.json")

if __name__ == "__main__":
    unittest.main()
