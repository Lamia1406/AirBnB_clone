#!/usr/bin/python3
"""defines unittests for user.py.
Unittest classes:
    TestUserClass
    """
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUserClass(unittest.TestCase):
    """Unittests for the User class"""
    def test_instance(self):
        """tests if the class is a child of BaseModel"""
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user, BaseModel)

    def test_type_str(self):
        """tests if all attributes are of str type"""
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)
