#!/usr/bin/python3
import json
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """This contains the entry point of the command interpreter"""
    prompt = "(hbnb)"

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Handles the EOF to exit the program"""
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id."""
        args = line.split()
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            try:
                instance = BsseModel()
                print(instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance based
        on the class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            try:
                instance = BaseModel()
                print(str(instance))
            except NameError:
                print("** class doesn't exist **")
            except FileNotFoundError:
                print("** no instance found **")

    def save_to_file(self):
        """saves data to file"""
        with open("user_data.json", "w") as json_file:
            json.dump(self.users, json_file)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
