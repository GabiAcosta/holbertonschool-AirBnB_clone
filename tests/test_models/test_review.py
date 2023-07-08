#!/usr/bin/python3
"""Unittest for Amenity class"""
import unittest
from models.base_model import BaseModel
from models.review import Review

review = Review()
review.place_id = "k6fhyu16a5sdg1"
review.user_id = "cv16jdyer6a4y1d"
review.text = "Lorem ipsum"


class TestReview(unittest.TestCase):

    def test_subclass(self):
        self.assertTrue(issubclass(review.__class__, BaseModel), True)

    def test_attr(self):
        self.assertTrue("id" in review.__dict__)
        self.assertTrue("created_at" in review.__dict__)
        self.assertTrue("updated_at" in review.__dict__)
        self.assertTrue("place_id" in review.__dict__)
        self.assertTrue("user_id" in review.__dict__)
        self.assertTrue("text" in review.__dict__)

    def test_attr_type(self):
        self.assertEqual(type(review.place_id), str)
        self.assertEqual(type(review.user_id), str)
        self.assertEqual(type(review.text), str)

    def test_save(self):
        review.save()
        self.assertNotEqual(review.created_at, review.updated_at)

    def test_to_dict(self):
        review_dict = review.to_dict()
        self.assertEqual(review_dict["__class__"], "Review")
        self.assertIsInstance(review_dict["created_at"], str)
        self.assertIsInstance(review_dict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
