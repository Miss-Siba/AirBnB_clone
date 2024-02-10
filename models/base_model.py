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
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for c, u in kwargs.items():
                if c == "created_cat" or c == "updated_at":
                    self.__dict__[c] = datetime.strptime(u, tform)
                else:
                    self.__dict__[c] = u
        else:
            models.storage.new(self)

    def to_dict(self):
        """Returns a dictionary of the BaseModel."""
        return {
                "id": self.id,
                "created_at": self.created_at.isoformat(),
                "updated_at": self.updated_at.isoformat(),
                "__class__": self.__class__.__name__
                }

    def save(self):
        """Saves the updates"""
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """Prints the BaseModel instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
