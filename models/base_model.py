#!/usr/bin/python3
"""This module contains one class Basemodel"""
import uuid
from datetime import datetime


class BaseModel:
    """defines all common attributes/methods for other classes"""
    def __init__(self):
        """constuctor
        initializes an object when an instance of a class is created
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """returns string representation of the object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime
        """
        self.update_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing
        all keys/values of __dict__ of the instance
        """
        dict_ = self.__dict__.copy()
        dict_["__class__"] = self.__class__.__name__
        dict_["created_at"] = self.created_at.isoformat()
        dict_["updated_at"] = self.updated_at.isoformat()
        return dict_
