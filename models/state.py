#!/usr/bin/python3
"""State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class that represents a state.
    Inherits from the BaseModel class.
    """

    def __init__(self, name=''):
        """
        Initializes an instance of State.

        Args:
            name (str): Name of the state (default is an empty string).
        """
        self.name = name
