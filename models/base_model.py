#!/usr/bin/python3
""""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of the HBnB project. """

    def __init__(self, *args, **kwargs):
        """Generate unique id in string format.
        Args:
            *args (any): Unused.
            **kwargs (dict): value pairs of attributes
        """
        tformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != 0:
            for c, u in kwargs.items():
                if c == "created_at" or c == "updated_at":
                    self.__dict__[c] = datetime.strptime(u, tformat)
                else:
                    self.__dict__[c] = u
        else:
            models.storage.new(self)

    def save(self):
        """Saves the updates"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary of the BaseModel."""
        copy_dict = self.__dict__.copy()
        copy_dict["created_at"] = self.updated_at.isoformat()
        copy_dict["updated_at"] = self.updated_at.isoformat()
        copy_dict["__class__"] = self.__class__.__name__
        return copy_dict

    def __str__(self):
        """Prints the BaseModel instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
