"""Runs a unittest on the Amenity class"""


import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test Amenity class"""

    def setUp(self):
        """mathod test"""

        self.amenity = Amenity()

    def test_attributes(self):
        """Test the attributes of Amenity."""

        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, "")

    def test_inheritance(self):
        """Test if Amenity is a subclass of BaseModel."""
        self.assertTrue(issubclass(type(self.amenity), BaseModel))


if __name__ == '__main__':
    unittest.main()
