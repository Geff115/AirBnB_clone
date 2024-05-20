"""Runs a unittest on the State class"""


import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Runs a test on the State class"""

    def test_attributes(self):
        state = State()
        self.assertEqual(state.name, "")


if __name__ == '__main__':
    unittest.main()
