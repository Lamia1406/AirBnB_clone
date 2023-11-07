#!/usr/bin/python3
"""defines the file storage  class."""
from models.base_model import BaseModel
import json


class FileStorage:
    """represents an abstract storage engine.

    Attributes:
    __file_path (str): Name of the file to save objects to
    __objects (dict): Dictionary of instantiated objects
    """

    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """
        deserialize the JSON file __file_path to __objects, if it exists.
        """
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.value():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
