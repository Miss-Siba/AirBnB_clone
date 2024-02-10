#!/usr/bin/python3
"""Serializes instance to a JSON file and deserializes JSON
file to instances"""
import json
from models.base_model import BaseModel


class FileStorage:
    """File Storage manager"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dicionary."""
        return self.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        with open("file.json", "w") as file:
            json.dump(self.__objects, file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open("file.json", "r") as file:
                self.__objects = json.load(file)
        except FileNotFoundError:
            pass
