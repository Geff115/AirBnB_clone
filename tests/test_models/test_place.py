"""Runs a unittest on the Place class"""


import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Place class"""

    def setUp(self):
        """Sets up test environment"""

        self.place = Place()

    def test_attributes(self):
        """Test if Place is a subclass of BaseModel."""

        attributes = {
                "city_id": str,
                "user_id": str,
                "name": str,
                "description": str,
                "number_rooms": int,
                "number_bathrooms": int,
                "max_guest": int,
                "price_by_night": int,
                "latitude": float,
                "longitude": float,
                "amenity_ids": list
        }
        for attr, attr_type in attributes.items():
            self.assertTrue(hasattr(self.place, attr))
            self.assertIsInstance(getattr(self.place, attr), attr_type)
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_inheritance(self):
        """Test if Place is a subclass of BaseModel."""

        self.assertTrue(issubclass(type(self.place), BaseModel))


if __name__ == '__main__':
    unittest.main()
