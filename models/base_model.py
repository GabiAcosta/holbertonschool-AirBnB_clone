#!/usr/bin/python3
"""
This module defines the `BaseModel` class, which serves as the base model
for other classes.
It provides basic attributes and methods that can be inherited and extended
by other classes.

Classes:
- BaseModel: The base model class with attributes and methods common
    to all models.

Methods:
- __init__: Initialize a new instance of the class.
- __str__: Return a string representation of the object.
- save: Update the 'updated_at' attribute with the current datetime.
- to_dict: Convert the object's attributes to a dictionary representation.
"""
import uuid
from datetime import datetime


class BaseModel:
    """Base class for creating models"""
    def __init__(self):
        """
        Initialize a new instance of the class.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        Return a string representation of the object.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the 'updated_at' attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Convert the object's attributes to a dictionary representation.
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["created_at"] = self.created_at.isoformat()
        return my_dict
