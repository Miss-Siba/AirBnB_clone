#!/usr/bin/python3
"""Defines the review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review.
    Attributes:
        place_id
        user_id
        text
    """
    place_id = ""
    user_id = ""
    text = ""
