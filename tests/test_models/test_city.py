"""Runs a unittest on the City class."""


import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Tests the City class"""

    def setUp(self):
        """test method"""

        self.city = City()

    def test_attributes(self):
        """Test the attributes of City."""

        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_inheritance(self):
        """Test if City is a subclass of BaseModel."""

        self.assertTrue(issubclass(type(self.city), BaseModel))


if __name__ == '__main__':
    unittest.main()
