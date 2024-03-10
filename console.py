#!/usr/bin/python3

"""program called console.py that contains the command"""

import cmd


class HBNBCommand(cmd.Cmd):

    """Defines the HBNB Commands"""

    prompt = "(hbnb)"

    def emptyline(self):

        """handling empty line"""

        pass

    def do_quit(self, arg):

        """Quit command to exit the program"""

        return True

    def do_EOF(self, arg):

        """Exit the program"""

        print()
        return True

    def help_quit(self):
        """Quit command to exit the program"""
        print("Quit command to exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
