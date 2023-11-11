#!/usr/bin/python3
"""defines unittests for BaseModel.py.
Unittest classes:
    TestInitMethod
    TestPublicInstanceMethods
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestInitMethod(unittest.TestCase):
    """Unittests for testing the constructor"""
    def test_obj_new(self):
        """ tests when an completely new object is created"""
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertIsNotNone(instance.id)
        self.assertIsNotNone(instance.created_at)
        self.assertIsNotNone(instance.updated_at)
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_obj_from_dict(self):
        """test when an object is created from a dictionary"""
        dict_ = {
            "id": "234",
            "created_at": "2023-11-09T12:00:00.000000",
            "updated_at": "2023-11-20T12:00:00.000000",
        }
        instance = BaseModel(**dict_)
        self.assertIsInstance(instance, BaseModel)


class TestPublicInstanceMethods(unittest.TestCase):
    """Unittests for testing the public instance methods"""
    def test_str(self):
        """ test string representation of the object """
        instance = BaseModel()
        name = instance.__class__.__name__
        id = instance.id
        dict_ = instance.__dict__
        expected_rep = f"[{name}] ({id}) {dict_}"
        self.assertEqual(str(instance), expected_rep)

    def test_save(self):
        """ tests save method """
        instance = BaseModel()
        updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(updated_at, datetime.now())

    def test_dict(self):
        """ tests the method that returns a dictionary containing
        all keys/values of __dict__ of the instance
        """
        instance = BaseModel()

        dict_ = instance.to_dict()
        self.assertIsInstance(dict_, dict)
        self.assertEqual(dict_["__class__"], instance.__class__.__name__)
        self.assertEqual(dict_["id"], instance.id)
        self.assertEqual(dict_["created_at"], instance.created_at.isoformat())
        self.assertEqual(dict_["updated_at"], instance.updated_at.isoformat())
