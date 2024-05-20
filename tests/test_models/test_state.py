"""Runs a unittest on the State class"""


import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Runs a test on the State class"""

    def setUp(self):
        state = State()

    def test_attributes(self):
        """Test the attributes of State."""

        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "")

    def test_inheritance(self):
        """Test if State is a subclass of BaseModel."""

        self.assertTrue(issubclass(type(self.state), BaseModel))


if __name__ == '__main__':
    unittest.main()
