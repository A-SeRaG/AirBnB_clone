#!/usr/bin/python3
"""class Place that inherits from BaseModel"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place class"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_roomes = ""
    number_bathrooms = ""
    price_by_night = ""
    latitude = ""
    longitude = ""
    amenity_ids = ""
