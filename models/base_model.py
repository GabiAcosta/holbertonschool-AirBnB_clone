#!/usr/bin/python3
"""Base class model"""
import uuid
from datetime import datetime


class BaseModel:
    """Class for BaseModel"""
    def __init__(self):
        """
        Initialize a new instance of the class.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.update_at = self.created_at

    def __str__(self):
        """
        Return a string representation of the object.
        """
        return "[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the 'updated_at' attribute with the current datetime.
        """
        self.update_at = datetime.now()

    def to_dict(self):
        """
        Convert the object's attributes to a dictionary representation.
        """
        my_dict = self.__dict__
        my_dict["__class__"] = __class__.__name__
        my_dict["update_at"] = self.update_at.isoformat()
        my_dict["created_at"] = self.created_at.isoformat()
        return my_dict
