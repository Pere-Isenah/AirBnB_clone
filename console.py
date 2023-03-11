#!/usr/bin/python3
""" This module defines a class `HBNBCommand` """
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    A command line interface for interacting with a HBNB database.

    The HBNBCommand class defines a command line interface
    using Python's cmd module.
    It provides two commands - "quit" and "EOF"
    - that can be used to exit the program.
    """

    prompt = "(hbnb)"
    __classes = {"BaseModel",
                 "User",
                 "Place",
                 "State",
                 "City",
                 "Amenity",
                 "Review"}

    def do_quit(self, arg):
        """
        Quit command to exit the program.

        Args:
        - arg (str): Optional argument to the command

        Returns:
        - True to signal the command loop to exit.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.

        Args:
        - arg (str): Optional argument to the command

        Returns:
        - True to signal the command loop to exit.
        """
        return True

    def emptyline(self):
        """Handles empty lines"""
        return

    def do_create(self, arg):
        """
        Create a new instance of a given class and print its ID.

        Args:
             (str): The name of the class to create an instance of.

        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            new_object = eval(f"{args[0]}")()
            print(new_object.id)
            storage.save()

    def do_show(self, arg):
        """
        Print the string representation of a given instance.

        Args:
            arg (str): The class name and ID of the instance to show,
            separated by a space.

        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[f"{args[0]}.{args[1]}"])

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id.

        Args:
            arg (str): A space-separated string containing
            the class name and id.

        Returns:
            None

        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}"not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[f"{args[0]}.{args[1]}"]
            storage.save()

    def do_all(self, arg):
        """Print all instances or all instances of a specific class.

        Args:
            arg (str): An optional space-separated string
            containing the class name.

        Returns:
            None

        """
        args = arg.split()

        if len(args) == 0:
            print([str(value)for value in storage.all().values()])

        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            print([str(v) for k, v in storage.all().items()
                   if k.startswith(args[0])])

    def do_update(self, arg):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            obj_class = args[0]
            obj_id = args[1]
            obj_key = args[0] + "." + args[1]
            obj = storage.all()[obj_key]
            attr_name = args[2]
            attr_value = args[3]

            if attr_value[1].startswith("'"):
                attr_value[1] = attr_value[1][1:-1]

            if hasattr(obj, attr_name):
                type_ = type(getattr(obj, attr_name))
                if type_ in [str, float, int]:
                    attr_value = type_(attr_value)
                    setattr(obj, attr_name, attr_value)
            else:
                setattr(obj, attr_name, attr_value)
                storage.save()

    def default(self, arg):
        """Handle default command for all instances of a class.

        Args:
            arg (str): The command argument.

        """
        args = arg.split(".")
        if args[0] in self.__classes and args[1] == "all()":
            self.do_all(args[0])
        elif args[1] == "count()":
            count = [v for k, v in storage.all().items()
                     if k.startswith(args[0])]
            print(len(count))
        elif args[1].startswith("show"):
            id_ = args[1].split('"')[1]
            self.do_show(f"{args[0]} {id_}")
        elif args[1].startswith("destroy"):
            id_ = args[1].split('"')[1]
            self.do_destroy(f"{args[0]} {id_}")
        elif args[1].startswith("update"):
            argv = [arg.strip() for arg in args[1].split('"')
                    if arg.strip() != ',']
            id_ = argv[1]
            attr_name_ = argv[2]
            attr_value_ = argv[3]
            self.do_update(f"{args[0]} {id_} {attr_name_} {attr_value_}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
