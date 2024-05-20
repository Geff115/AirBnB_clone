"""Runs a unittest on the Amenity class"""


import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test Amenity class"""

    def test_attributes(self):
        """mathod test"""

        amenity = Amenity()
        self.assertEqual(amenity.name, "")


if __name__ == '__main__':
    unittest.main()
