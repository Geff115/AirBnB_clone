"""Running a unittest on the console to ensure
that everything works as it should.
"""


import sys
import os
import unittest
from unittest.mock import patch
from io import StringIO


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from console import HBNBCommand
from models.user import User
from models import storage


class TestConsole(unittest.TestCase):
    """Runs a unittest on all the methods in the
    console class.
    """

    def setUp(self):
        """Set up test environment"""

        storage._FileStorage__objects = {}

    def tearDown(self):
        """Tear down test environment"""

        storage._FileStorage__objects = {}

    def test_help_show(self):
        """Test the help_show command"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertIn("Prints string representation of an instance", f.getvalue())

    def test_create(self):
        """Test the create command."""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            output = f.getvalue().strip()
            self.assertTrue(len(output) == 36)

    def test_show(self):
        """Test the show command"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show User {user_id}")
            output = f.getvalue().strip()
            self.assertIn(user_id, output)

    def test_update(self):
        """Test the update command"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'User.update("{user_id}", {{"first_name": "John", "age": 22}})')
            HBNBCommand().onecmd(f"show User {user_id}")
            output = f.getvalue().strip()
            self.assertIn("'first_name': 'John'", output)
            self.assertIn("'age': 22", output)

    def test_destroy(self):
        """Test the destroy command"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy User {user_id}")
            self.assertEqual(f.getvalue().strip(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show User {user_id}")
            self.assertIn("** no instance found **", f.getvalue().strip())

    def test_all(self):
        """Test the all command"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
            output = f.getvalue().strip()
            self.assertIn(user_id, output)

    def test_count(self):
        """Test the count command"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("create User")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
            output_count = f.getvalue().strip()
            self.assertEqual(output_count, "2")


if __name__ == "__main__":
    unittest.main()
