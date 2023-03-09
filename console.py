#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
import json
import sys


class HBNBCommand(cmd.Cmd):
    """
    A command line interface for interacting with a HBNB database.

    The HBNBCommand class defines a command line interface
    using Python's cmd module.
    It provides two commands - "quit" and "EOF"
    - that can be used to exit the program.
    """

    prompt = "(hbnb)"
    __classes = {"BaseModel"}

    def do_quit(self, arg):
        """
        Quit command to exit the program.

        Args:
        - arg (str): Optional argument to the command

        Returns:
        - True to signal the command loop to exit.
        """
        return True

    def help_quit(self):
        """
        Display help text for the quit command.
        """
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """
        EOF command to exit the program.

        Args:
        - arg (str): Optional argument to the command

        Returns:
        - True to signal the command loop to exit.
        """
        return True

    def help_EOF(self):
        """
        Display help text for the EOF command.
        """
        print("EOF command to exit the program")

    def emptyline(self):
        """Handles empty lines"""
        pass
 
    def do_create(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")


if __name__ == '__main__':
    """
    Create an instance of the HBNBCommand class and start the command loop.
    """
    HBNBCommand().cmdloop()
