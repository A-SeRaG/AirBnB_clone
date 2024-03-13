#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:

    __file_path = "file.json"
    __obj = {}

    def all(self):
        return FileStorage.__obj

    def new(self, obj):
        obj_name = obj.__class__.__name__
        FileStorage.__obj["{}.{}".format(obj_name, obj.id)] = obj

    def save(self):
        odj_1 = FileStorage.__obj
        obj_2 = {obj: odj_1[obj].to_dict() for obj in odj_1.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_2, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path) as f:
                obj_2 = json.load(f)
                for o in obj_2.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
