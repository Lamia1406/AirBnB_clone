#!/usr/bin/python3
"""defines unittests for review.py.
Unittest classes:
    TestReviewClass
    """
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReviewClass(unittest.TestCase):
    """Unittests for the Review class"""
    def test_instance(self):
        """tests if the class is a child of BaseModel"""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review, BaseModel)

    def test_type_str(self):
        """tests if all attributes are of str type"""
        review = Review()
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)
