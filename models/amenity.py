#!/usr/bin/python3
""" Amenity class """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity class that represents a convenience or service.
    Inherits from the BaseModel class."""
    name = ''
