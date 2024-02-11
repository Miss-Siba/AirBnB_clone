#!/usr/bin/python3
""" Module for the console."""
import cmd
import re
from shlex import split
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


def parse_string(line):
    """Parses string. """
    curly_braces = re.search(r"\{(.*?)\}", line)
    brackets = re.search(r"\[(.*?)\]", line)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(line)]
        else:
            parter = split(line[:brackets.span()[0]])
            parsed_str = [i.strip(",") for i in parter]
            parsed_str.append(brackets.group())
            return parsed_str
    else:
        parter = split(line[:curly_braces.span()[0]])
        parsed_str = [i.strip(",") for i in parter]
        parsed_str.append(curly_braces.group())
        return parsed_str


class HBNBCommand(cmd.Cmd):
    """This contains the entry point of the command interpreter"""
    prompt = "(hbnb)"
    HBNBC_classes = ["BaseModel", "User", "Amenity",
                     "Place", "Review", "State", "City"]

    def emptyline(self):
        """Do nothing when an empty line is encountered."""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Handles the EOF to exit the program"""
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id."""
        args = parse_string(line)
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            try:
                instance = BaseModel()
                instance.save()
                print(instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance based
        on the class name and id"""
        args = parse_string(line)

        if not args:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            try:
                key = f"{class_name}.{instance_id}"
                instance = storage.all().get(key)
                if instance:
                    print(instance)
                else:
                    print("** no instance found **")
            except NameError:
                print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = parse_string(line)

        if not args:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            del objdict["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, line):
        """"Prints all string representation of all instances
        based or not on the class name
        """
        args = parse_string(line)
        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(args) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_count(self, line):
        """Retrieve the number of instances of a given class."""
        args = parse_string(line)
        count = 0
        for obj in storage.all().values():
            if args[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, line):
        """ Updates an instance based on the class name and id by adding
        or updating attribute(save the change into the JSON file).
        """
        args = parse_string(line)
        objdict = storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(args[0], args[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(args) == 4:
            obj = objdict["{}.{}".format(args[0], args[1])]
            if args[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = valtype(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            obj = objdict["{}.{}".format(args[0], args[1])]
            for c, u in eval(args[2]).items():
                if (c in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[c]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[c])
                    obj.__dict__[c] = valtype(u)
                else:
                    obj.__dict__[c] = u
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
