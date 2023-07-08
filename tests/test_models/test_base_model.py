#!/usr/bin/python3
"""Unittest for BaseModel class"""
import unittest
from models.base_model import BaseModel

base = BaseModel()


class TestBaseModel(unittest.TestCase):

    def test_init(self):
        self.assertTrue(isinstance(base, BaseModel))

    def test_save(self):
        base.save()
        self.assertNotEqual(base.created_at, base.updated_at)

    def test_to_dict(self):
        base_dict = base.to_dict()
        self.assertEqual(base_dict["__class__"], "BaseModel")
        self.assertIsInstance(base_dict["created_at"], str)
        self.assertIsInstance(base_dict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
