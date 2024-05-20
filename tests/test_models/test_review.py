"""Runs a unittest on the Review class"""


import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Review class"""

    def test_attributes(self):
        """method test"""

        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == '__main__':
    unittest.main()
