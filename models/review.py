#!/usr/bin/python3
"""This module contains one class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """child class of the class BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
