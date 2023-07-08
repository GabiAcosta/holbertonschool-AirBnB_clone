#!/usr/bin/python3
"""Unittest for Amenity class"""
import unittest
from models.base_model import BaseModel
from models.state import State

state = State()
state.name = "Florida"


class TestState(unittest.TestCase):

    def test_subclass(self):
        self.assertTrue(issubclass(state.__class__, BaseModel), True)

    def test_attr(self):
        self.assertTrue("id" in state.__dict__)
        self.assertTrue("created_at" in state.__dict__)
        self.assertTrue("updated_at" in state.__dict__)
        self.assertTrue("name" in state.__dict__)

    def test_attr_type(self):
        self.assertEqual(type(state.name), str)

    def test_save(self):
        state.save()
        self.assertNotEqual(state.created_at, state.updated_at)

    def test_to_dict(self):
        state_dict = state.to_dict()
        self.assertEqual(state_dict["__class__"], "State")
        self.assertIsInstance(state_dict["created_at"], str)
        self.assertIsInstance(state_dict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
