#!/usr/bin/python3
"""This module contains one class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """child class of the class Basemodel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
