"""Runs a unittest on the City class."""


import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Tests the City class"""

    def test_attributes(self):
        """test method"""

        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == '__main__':
    unittest.main()
