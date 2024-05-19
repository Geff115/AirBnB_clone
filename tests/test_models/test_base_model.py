"""This imports the modules: unttest, BaseModel, and
the datetime module.
"""


import unittest
from unittest.mock import patch
from datetime import datetime
from models.base_model import BaseModel
from uuid import uuid4


class TestBaseModel(unittest.TestCase):
    """Runs a series of unittest on the BaseModel class"""

    @patch('models.base_model.storage')
    def test_initialization(self, mock_storage):
        """Runs a test on the init method"""

        mock_storage.new = MagicMock()
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))
        mock_storage.new.assert_called_once_with(obj)

    def test_str_method(self):
        """Runs a test on the string representation method"""

        obj = BaseModel()
        expect_output = f"[{obj.__class__.__name__}] ({obj.id}) {obj.__dict__}"
        self.assertEqual(str(obj), expect_output)

    @patch('models.base_model.storage')
    def test_save_method(self, mock_storage):
        """Runs a test on the save method which checks for the
        current time which an instance was created and updated.
        """

        mock_storage.save = MagicMock()
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(obj.updated_at, old_updated_at)
        mock_storage.save.assert_called_once()

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

    @patch('models.base_model.storage')
    def test_kwargs_initialization(self, mock_storage):
        "Runs a test on the keyworded arguments initialization"""

        data = {
            'id': str(uuid4()),
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat(),
            '__class__': 'BaseModel'
        }
        obj = BaseModel(**data)
        self.assertIsInstance(obj, BaseModel)
        self.assertEqual(obj.id, data['id'])
        self.assertEqual(obj.created_at.isoformat(), data['created_at'])
        self.assertEqual(obj.updated_at.isoformat(), data['updated_at'])
        mock_storage.new.assert_not_called()

    def test_args_initialization(self):
        """Runs a test to ensure *args are not used"""

        obj = BaseModel('arg1', 'arg2')
        self.assertIsInstance(obj, BaseModel)
        self.assertNotIn('arg1', obj.__dict__)
        self.assertNotIn('arg2', obj.__dict__)

    @patch('models.base_model.storage')
    def test_invalid_datetime_format(self, mock_storage):
        """Runs a test to check invalid daytime format"""

        invalid_data = {
                'created_at': 'invalid_data',
                'updated_at': 'invalid_data'
        }
        with self.assertLogs(level='INFO') as log:
            obj = BaseModel(**invalid_data)
            self.assertTrue(any("Invalid date format"
                                in message for message in log.output))
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertNotEqual(obj.created_at.isoformat(), 'invalid_date')
        self.assertNotEqual(obj.updated_at.isoformat(), 'invalid_date')
        mock_storage.new.assert_not_called()


if __name__ == '__main__':
    """Ensures that this script runs when it is executed directly
    and not when it is imported as a module.
    """

    unittest.main()
