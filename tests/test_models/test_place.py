#!/usr/bin/python3
"""defines unittests for place.py.
Unittest classes:
    TestPlaceClass
    """
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlaceClass(unittest.TestCase):
    """Unittests for the Place class"""
    def test_instance(self):
        """tests if the class is a child of BaseModel"""
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place, BaseModel)

    def test_type(self):
        """tests the types of the attributes"""
        place = Place()
        self.assertIsInstance(place.name, str)
        self.assertIsInstance(place.user_id, str)
        self.assertIsInstance(place.city_id, str)
        self.assertIsInstance(place.description, str)
        self.assertIsInstance(place.number_rooms, int)
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertIsInstance(place.max_guest, int)
        self.assertIsInstance(place.price_by_night, int)
        self.assertIsInstance(place.latitude, float)
        self.assertIsInstance(place.longitude, float)
        self.assertIsInstance(place.amenity_ids, list)
