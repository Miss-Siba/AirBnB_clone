#!/usr/bin/python3
"""Defines a place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents a place.
    Attributes:
        city_id: city id
        user_id: user id
        name: name of the place
        description: description of the place
        number_rooms: number of rooms available
        number_bathrooms: number of bathrooms available
        max_guest: maximum guests
        price_by_night: rate per night
        latitude: float - 0.0
        longitude: float - 0.0
        amenity_ids: list of string - list of Amenity.id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
