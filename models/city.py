#!/usr/bin/python3
"""This module contains one class City"""
from models.base_model import BaseModel


class City(BaseModel):
    """child class of the class Basemodel"""
    state_id = ""
    name = ""
