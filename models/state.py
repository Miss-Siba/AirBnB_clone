#!/usr/bin/python3
"""Defines the State class."""
from models.base_model import BaseModel

class State(BaseModel):
    """inherits from BaseModel to represent state.
    Attributes:
        name = name of the state.
    """
    name = ""
