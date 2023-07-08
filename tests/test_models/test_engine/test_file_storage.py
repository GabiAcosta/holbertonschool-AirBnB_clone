#!/usr/bin/python3
"""Unittest for FileStorage class"""
import unittest
import os
from models.user import User
from models.engine.file_storage import FileStorage

storage = FileStorage()
user = User()
user.email = "HIM@Heat.com"
user.first_name = "Jimmy"
user.last_name = "Buckets"
user.password = "im_HIM"
storage.save()


class TestFileStorage(unittest.TestCase):
    """
    TestFileStorage class to perform unit tests on the FileStorage class.
    """
    def test_all(self):
        """
        Test the all() method of FileStorage.
        """
        obj_dict = storage.all()
        self.assertIsNotNone(obj_dict)
        self.assertIsInstance(obj_dict, dict)

    def test_new(self):
        """
        Test the new() method of FileStorage.
        """
        obj_dict = storage.all()
        storage.new(user)
        key = f"{user.__class__.__name__}.{user.id}"
        self.assertIsNotNone(obj_dict[key])

    def test_save(self):
        """
        Test the save() method of FileStorage.
        """
        self.assertTrue(os.path.exists("objects.json"))


if __name__ == "__main__":
    unittest.main()
