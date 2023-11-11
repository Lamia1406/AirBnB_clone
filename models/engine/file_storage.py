#!/usr/bin/python3
"""defines the file storage  class."""
from models.base_model import BaseModel
import json
from datetime import datetime
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """represents an abstract storage engine.

    Attributes:
    __file_path (str): Name of the file to save objects to
    __objects (dict): Dictionary of instantiated objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        "returns the dictionary"
        return FileStorage.__objects

    def new(self, obj):
        """set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        for obj_key, obj_value in objdict.items():
            for key, value in obj_value.items():
                if isinstance(value, datetime):
                    obj_value[key] = value.isoformat()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for key, obj in objdict.items():
                    cls_name = obj.get('__class__')
                    mod_name = obj.get('__module__')
                    if cls_name and mod_name:
                        import_mod = __import__(mod_name, fromlist=[cls_name])
                        class_ = getattr(import_mod, cls_name)
                        self.new(class_(**obj))
        except FileNotFoundError:
            return
