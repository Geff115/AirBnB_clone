"""This imports the modules: unttest, BaseModel, and
the datetime module.
"""


import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Runs a series of unittest on the BaseModel class"""

    def test_initialization(self):
        """Runs a test on the init method"""

        obj = BaseModel()
        self.assertIsNotNone(obj.id)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertEqual(obj.created_at, obj.updated_at)

    def test_str_method(self):
        """Runs a test on the string representation method"""

        obj = BaseModel()
        expect_output = f"[{obj.__class__.__name__}] ({obj.id}) {obj.__dict__}"
        self.assertEqual(str(obj), expect_output)

    def test_save_method(self):
        """Runs a test on the save method which checks for the
        current time which an instance was created and updated.
        """

        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(obj.updated_at, old_updated_at)

    def test_to_dict_method(self):
        """Runs a test on the to_dict method which returns a
        dictionary representation of keys/values pair.
        """

        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], obj.__class__.__name__)
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())


if __name__ == '__main__':
    """Ensures that this script runs when it is executed directly
    and not when it is imported as a module.
    """

    unittest.main()
