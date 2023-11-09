#!/usr/bin/python3
"""defines unittests for state.py.
Unittest classes:
    TestStateClass
    """
import unittest
from models.base_model import BaseModel
from models.state import State


class TestStateClass(unittest.TestCase):
    """Unittests for the State class"""
    def test_instance(self):
        """tests if the class is a child of BaseModel"""
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state, BaseModel)

    def test_type_str(self):
        """tests if all attributes are of str type"""
        state = State()
        self.assertIsInstance(state.name, str)
