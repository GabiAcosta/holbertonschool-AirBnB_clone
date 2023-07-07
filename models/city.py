#!/usr/bin/python3
""" The destination of this module is create a
City class with stateid and name """
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that represents a city.
    Inherits from the BaseModel class.
    """
    def __init__(self, state_id='', name=''):
        """
         Initializes an instance of City.

        Args:
            state_id (str): ID of the state associated with the city.
            name (str): Name of the city (default is an empty string).
        """
        self.state_id = state_id
        self.name = name
