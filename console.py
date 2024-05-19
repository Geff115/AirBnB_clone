#!/usr/bin/python3
"""program that contains entry point
    of command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """class defintion that inherits from cmd"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program when EOF (Ctrl+D) is encountered"""
        print()  # Print a newline for better formatting
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
