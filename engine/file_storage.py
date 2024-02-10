#!/usr/bin/python3
"""Serializes instance to a JSON file and deserializes JSON file to instances"""

import json

class FileStorage:
    """File Storage manager"""
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """Returns the dicionary."""
        return {}

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj
    
    def save(self):
        with open {"file.json", "w") as file
        json.dump(self.__objects, file)
    
    def reload(self):
        try:
            with open {"file.json", "r") as file
             self.__objects = json.load(file)
        except FileNotFoundError:
            pass
