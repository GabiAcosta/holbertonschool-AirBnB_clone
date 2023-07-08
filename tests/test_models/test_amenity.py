#!/usr/bin/python3
"""Unittest for Amenity class"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity

amenity = Amenity()
amenity.name = "Pool"


class TestAmenity(unittest.TestCase):

    def test_subclass(self):
        self.assertTrue(issubclass(amenity.__class__, BaseModel), True)

    def test_attr(self):
        self.assertTrue("name" in amenity.__dict__)
        self.assertTrue("id" in amenity.__dict__)
        self.assertTrue("created_at" in amenity.__dict__)
        self.assertTrue("updated_at" in amenity.__dict__)

    def test_attr_type(self):
        self.assertEqual(type(amenity.name), str)

    def test_save(self):
        amenity.save()
        self.assertNotEqual(amenity.created_at, amenity.updated_at)

    def test_to_dict(self):
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertIsInstance(amenity_dict["created_at"], str)
        self.assertIsInstance(amenity_dict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
