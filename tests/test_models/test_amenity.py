#!/usr/bin/python3
"""defines unittests for amenity.py
Unittest classes:
    TestAmenityClass
    """
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenityClass(unittest.TestCase):
    """Unittests for the Amenity class"""
    def test_instance(self):
        """tests if the class is a child of BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)

    def test_type_str(self):
        """tests if all attributes are of str type"""
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)
