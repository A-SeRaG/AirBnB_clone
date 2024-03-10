#!/usr/bin/python3
"""program called console that contains  command"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):

    """Defines the HBNB Commands"""

    prompt = "(hbnb)"
    __classes = {
        "BaseModel", "User", "State", "City",
        "Place", "Amenity", "Review"
    }

    def emptyline(self):
        """handling empty line"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print("")
        return True

    def help_quit(self):
        """What quit command do"""
        print("Quit command to exit the program")

    def do_create(self, arg):
        """Create a new class instance and print its id"""
        Wrds = shlex.split(arg)
        if len(Wrds) == 0:
            print("** class name missing **")
        elif Wrds[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(Wrds[0])().id)
            storage.save()

    def do_show(self, arg):
        """Display the str repr. of a class instance of a given id"""
        Wrds = shlex.split(arg)
        objs = storage.all()
        if len(Wrds) == 0:
            print("** class name missing **")
        elif Wrds[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(Wrds) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(Wrds[0], Wrds[1]) not in objs:
            print("** no instance found **")
        else:
            print(objs["{}.{}".format(Wrds[0], Wrds[1])])

    def do_destroy(self, arg):
        """Delete a class instance of a given id"""
        Wrds = shlex.split(arg)
        objs = storage.all()
        if len(Wrds) == 0:
            print("** class name missing **")
        elif Wrds[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(Wrds) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(Wrds[0], Wrds[1]) not in objs.keys():
            print("** no instance found **")
        else:
            del objs["{}.{}".format(Wrds[0], Wrds[1])]
            storage.save()

    def do_all(self, arg):
        """Prints all str repr. of all instances based on\not class name"""
        Wrds = shlex.split(arg)
        if len(Wrds) > 0 and Wrds[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            objs = []
            for obj in storage.all().values():
                if len(Wrds) > 0 and Wrds[0] == obj.__class__.__name__:
                    objs.append(obj.__str__())
                elif len(Wrds) == 0:
                    objs.append(obj.__str__())
            print(objs)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        Wrds = shlex.split(arg)
        objs = storage.all()

        if len(Wrds) == 0:
            print("** class name missing **")
            return False
        if Wrds[0] not in self.__classes:
            print("** class doesn't exist **")
            return False
        if len(Wrds) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(Wrds[0], Wrds[1]) not in objs.keys():
            print("** no instance found **")
            return False
        if len(Wrds) == 2:
            print("** attribute name missing **")
            return False
        if len(Wrds) == 3:
            try:
                type(eval(Wrds[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(Wrds) == 4:
            obj = objs["{}.{}".format(Wrds[0], Wrds[1])]
            if Wrds[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[Wrds[2]])
                obj.__dict__[Wrds[2]] = valtype(Wrds[3])
            else:
                obj.__dict__[Wrds[2]] = Wrds[3]
        elif type(eval(Wrds[2])) == dict:
            obj = objs["{}.{}".format(Wrds[0], Wrds[1])]
            for i, j in eval(Wrds[2]).items():
                if (i in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[i]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[i])
                    obj.__dict__[i] = valtype(j)
                else:
                    obj.__dict__[i] = j
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
