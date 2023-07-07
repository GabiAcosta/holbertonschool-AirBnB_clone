#!/usr/bin/python3
""" Amenity class """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity class that represents a convenience or service.
    Inherits from the BaseModel class."""
    def __init__(self, name=''):
        """
        Initializes an instance of Amenity.

        Args:
            name (str): Name of the Amenity (default is an empty string).
        """
        self.name = name
