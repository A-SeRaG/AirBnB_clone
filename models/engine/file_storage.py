#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:

    """Represent an abstracted storage engine"""

    __file_path = "file.json"
    __obj = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__obj

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        obj_name = obj.__class__.__name__
        FileStorage.__obj["{}.{}".format(obj_name, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odj_1 = FileStorage.__obj
        obj_2 = {obj: odj_1[obj].to_dict() for obj in odj_1.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_2, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                obj_2 = json.load(f)
                for o in obj_2.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
