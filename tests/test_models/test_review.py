"""Runs a unittest on the Review class"""


import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Review class"""

    def setUp(self):
        """method test"""

        review = Review()

    def test_attributes(self):
        """Test the attributes of Review."""

        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_inheritance(self):
        """Test if Review is a subclass of BaseModel."""

        self.assertTrue(issubclass(type(self.review), BaseModel))


if __name__ == '__main__':
    unittest.main()
