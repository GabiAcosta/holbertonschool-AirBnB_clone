#!/usr/bin/python3
""" Place Class """
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class that represents a place or accommodation.
    Inherits from the BaseModel class.
    """
    def __init__(self, city_id='', user_id='', name='', description='',
                 number_rooms=0, number_bathrooms=0, max_guest=0,
                 price_by_night=0, latitude=0.0, longitude=0.0,
                 amenity_ids=[]):
        """
        Initializes an instance of Place.

        Args:
            city_id (str): ID of the city where the place is located.
            user_id (str): ID of the user who owns the place.
            name (str): Name of the place.
            description (str): Description of the place.
            number_rooms (int): Number of rooms in the place.
            number_bathrooms (int): Number of bathrooms in the place.
            max_guest (int): Maximum number of guests allowed in the place.
            price_by_night (int): Price per night for the place.
            latitude (float): Latitude coordinate of the place.
            longitude (float): Longitude coordinate of the place.
            amenity_ids (list): List of amenity IDs associated with the place.
        """
        self.city_id = city_id
        self.user_id = user_id
        self.name = name
        self.description = description
        self.number_rooms = number_rooms
        self.number_bathrooms = number_bathrooms
        self.max_guest = max_guest
        self.price_by_night = price_by_night
        self.latitude = latitude
        self.longitude = longitude
        self.amenity_ids = amenity_ids
