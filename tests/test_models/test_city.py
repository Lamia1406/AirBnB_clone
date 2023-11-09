#!/usr/bin/python3
"""defines unittests for city.py.
Unittest classes:
    TestCityClass
    """
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCityClass(unittest.TestCase):
    """Unittests for the City class"""
    def test_instance(self):
        """tests if the class is a child of BaseModel"""
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city, BaseModel)

    def test_type_str(self):
        """tests if all attributes are of str type"""
        city = City()
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)
