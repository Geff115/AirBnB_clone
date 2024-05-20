"""
This file runs a unittest on the User class created
using different methods.
"""


import unittest
from models.user import User
from models.base_model import BaseModel
from models import storage
import os


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def setUp(self):
        """Set up for User tests."""

        self.user = User()
        self.user.email = "test@example.com"
        self.user.password = "password"
        self.user.first_name = "Test"
        self.user.last_name = "User"

    def tearDown(self):
        """Test that User inherits from BaseModel."""

        self.assertIsInstance(self.user, BaseModel)

    def test_user_attributes(self):
        """Test that User has the correct attributes."""

        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "password")
        self.assertEqual(self.user.first_name, "Test")
        self.assertEqual(self.user.last_name, "User")

    def test_save_user(self):
        """Test that User can be saved to storage."""

        self.user.save()
        key = "User." + self.user.id
        self.assertIn(key, storage.all())

    def test_to_dict_user(self):
        """Test that to_dict method creates a dictionary with correct attributes."""

        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['email'], "test@example.com")
        self.assertEqual(user_dict['password'], "password")
        self.assertEqual(user_dict['first_name'], "Test")
        self.assertEqual(user_dict['last_name'], "User")
        self.assertEqual(user_dict['__class__'], "User")

    def test_reload_user(self):
        """Test that reload correctly deserializes a User instance."""

        self.user.save()
        storage.reload()
        key = "User." + self.user.id
        self.assertIn(key, storage.all())
        loaded_user = storage.all()[key]
        self.assertEqual(loaded_user.email, "test@example.com")
        self.assertEqual(loaded_user.password, "password")
        self.assertEqual(loaded_user.first_name, "Test")
        self.assertEqual(loaded_user.last_name, "User")


if __name__ == "__main__":
    unittest.main()
