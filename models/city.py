#!/usr/bin/python3
""" The destination of this module is create a
City class with stateid and name """
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that represents a city.
    Inherits from the BaseModel class.
    """
    state_id = ''
    name = ''
