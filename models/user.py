#!/usr/bin/python3
"""Defines a class User."""
from models.base_model import BaseModel


class User(BaseModel):
    """ Represents a User.
    Attributes:
        email: email of the user
        password: user's password
        first_name: user's first name
        last_name: user's last name.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
