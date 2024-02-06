#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):
    """This contains the entry point of the command interpreter"""
    prompt = "(hbnb)"

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Handles the EOF to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
