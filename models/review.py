#!/usr/bin/python3
"""Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that represents a review.
    Inherits from the BaseModel class.
    """
    def __init__(self, place_id='', user_id='', text=''):
        """
        Initializes an instance of Review.

        Args:
            place_id (str): ID of the place associated with the review.
            user_id (str): ID of the user who wrote the review.
            text (str): Text content of the review.
        """
        self.place_id = place_id
        self.user_id = user_id
        self.text = text
