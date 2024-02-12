#!/usr/bin/python3
"""Serializes instance to a JSON file and deserializes JSON
file to instances"""
import json
import os
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.user import User
from models.review import Review


class FileStorage:
    """File Storage manager"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dicionary."""
        return self.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        objdict = {obj: FileStorage.__objects[obj].to_dict()
                   for obj in FileStorage.__objects}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(objdict, file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for key, value in objdict.items():
                    class_name = value["__class__"]
                    del value["__class__"]
                    self.new(evial(class_name)(**value))
        except FileNotFoundError:
            pass
