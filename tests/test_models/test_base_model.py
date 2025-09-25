#!/usr/bin/python3
"""Unit tests for BaseModel"""

import unittest
import uuid
from datetime import datetime
from unittest.mock import patch
from models.base_model import BaseModel
import time
import time


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def setUp(self):
        """Set up test fixtures before each test method"""
        self.model = BaseModel()

    def test_instance_creation(self):
        """Test BaseModel instance creation"""
        self.assertIsInstance(self.model, BaseModel)
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))

    def test_id_is_string(self):
        """Test that id is a string"""
        self.assertIsInstance(self.model.id, str)

    def test_id_is_unique(self):
        """Test that each instance has a unique id"""
        model2 = BaseModel()
        self.assertNotEqual(self.model.id, model2.id)

    def test_created_at_is_datetime(self):
        """Test that created_at is a datetime object"""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test that updated_at is a datetime object"""
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str_representation(self):
        """Test string representation of BaseModel"""
        string = str(self.model)
        self.assertIn("[BaseModel]", string)
        self.assertIn(self.model.id, string)

    def test_save_updates_updated_at(self):
        """Test that save() updates updated_at"""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict_returns_dict(self):
        """Test that to_dict returns a dictionary"""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)

    def test_to_dict_contains_class(self):
        """Test that to_dict contains __class__ key"""
        model_dict = self.model.to_dict()
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')

    def test_to_dict_datetime_format(self):
        """Test that datetime objects are converted to ISO format strings"""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_to_dict_with_custom_attributes(self):
        """Test to_dict with custom attributes"""
        self.model.name = "My First Model"
        self.model.my_number = 89
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['name'], "My First Model")
        self.assertEqual(model_dict['my_number'], 89)

    def test_kwargs_initialization(self):
        """Test initialization with kwargs"""
        kwargs = {
            'id': 'test-id-123',
            'created_at': '2023-01-01T00:00:00.000000',
            'updated_at': '2023-01-01T00:00:01.000000',
            'name': 'Test Model'
        }
        model = BaseModel(**kwargs)
        self.assertEqual(model.id, 'test-id-123')
        self.assertEqual(model.name, 'Test Model')
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_kwargs_ignores_class(self):
        """Test that __class__ key is ignored in kwargs"""
        kwargs = {'__class__': 'ShouldBeIgnored', 'id': 'test-123'}
        model = BaseModel(**kwargs)
        self.assertEqual(model.__class__.__name__, 'BaseModel')

        @patch('models.storage')
        def test_save_calls_storage_save(self, mock_storage):
            """Test that save() calls storage.save()"""
            self.model.save()
            mock_storage.save.assert_called_once()

        def test_save_updates_timestamp(self):
            """Test that save() updates the updated_at timestamp"""
            original_time = self.model.updated_at
            time.sleep(0.01)  # Small delay to ensure timestamp difference
            self.model.save()
            self.assertGreater(self.model.updated_at, original_time)

        def test_save_does_not_change_created_at(self):
            """Test that save() does not modify created_at"""
            original_created_at = self.model.created_at
            self.model.save()
            self.assertEqual(self.model.created_at, original_created_at)

        def test_save_does_not_change_id(self):
            """Test that save() does not modify the id"""
            original_id = self.model.id
            self.model.save()
            self.assertEqual(self.model.id, original_id)

        def test_multiple_saves_update_timestamp(self):
            """Test that multiple saves continue to update timestamp"""
            first_save_time = self.model.updated_at
            time.sleep(0.01)
            self.model.save()
            second_save_time = self.model.updated_at
            time.sleep(0.01)
            self.model.save()
            third_save_time = self.model.updated_at
            
            self.assertGreater(second_save_time, first_save_time)
            self.assertGreater(third_save_time, second_save_time)

        @patch('models.storage')
        def test_save_with_custom_attributes(self, mock_storage):
            """Test that save() works with custom attributes"""
            self.model.name = "Test Model"
            self.model.number = 42
            old_updated_at = self.model.updated_at
            self.model.save()
            
            self.assertNotEqual(old_updated_at, self.model.updated_at)
            self.assertEqual(self.model.name, "Test Model")
            self.assertEqual(self.model.number, 42)
            mock_storage.save.assert_called_once()

    if __name__ == '__main__':
        unittest.main()
