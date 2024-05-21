#!/usr/bin/python3
"""program that contains entry point
    of command interpreter"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """class defintion that inherits from cmd"""

    prompt = "(hbnb) "

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it to JSON file, & prints the id."""

        if not arg:
            print("** class name missing **")
            return
        try:
            if arg in storage.get_class_map():
                new_instance = storage.get_class_map()[arg]()
                new_instance.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints string representation of an instance
        based on class name and id."""

        args = arg.split()
        class_map = storage.get_class_map()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in class_map:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""

        args = arg.split()
        class_map = storage.get_class_map()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in class_map:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of all
        instances based or not on class name."""

        args = arg.split()
        if args and args[0] not in storage.get_class_map():
            print("** class doesn't exist **")
            return
        class_name = args[0] if args else None
        instances = storage.all()
        instance_list = []
        for key, value in instances.items():
            if class_name:
                if key.startswith(class_name):
                    instance_list.append(value.to_dict())
            else:
                instance_list.append(value.to_dict())
        print(instance_list)

    def do_update(self, arg):
        """Updates an instance based on class name & id
        by adding or updating attribute."""

        args = arg.split()
        class_map = storage.get_class_map()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in class_map:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_name = args[2]
        attribute_value = args[3]
        obj = storage.all()[key]
        try:
            attribute_value = eval(attribute_value)
        except (NameError, SyntaxError):
            pass
        setattr(obj, attribute_name, attribute_value)
        obj.save()

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

    def default(self, line):
        """Handle class-specific commands like <class name>.all()."""

        args = line.split(".")
        if len(args) == 2:
            class_name = args[0]
            command = args[1].strip()

            class_map = storage.get_class_map()
            if class_name in class_map:
                cls = class_map[class_name]
                if command == "all()":
                    instances = cls.all()
                    print([str(obj) for obj in instances])
                    return
                elif command == "count()":
                    count = len(cls.all())
                    print(count)
                    return
                elif command.startswith("show(") and command.endswith(")"):
                    obj_id = command[5:-1].strip("\"'")
                    instance = cls.show(obj_id)
                    if instance:
                        print(instance)
                    else:
                        print("** no instance found **")
                    return
        print("*** Unknown syntax: {}".format(line))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
