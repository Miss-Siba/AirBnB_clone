#!/usr/bin/python3
"""Defines the city class."""
from models.base_model import BaseModel


class City(BaseModel):
    """ Represents a city class.
    Attributes:
        name = name of the city
        state_id = state id.
    """
    state_id = ""
    name = ""
