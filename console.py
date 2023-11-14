#!/usr/bin/python3
"""defines the HBnB console."""
import cmd
import re
from shlex import split
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    """Parses a command-line input, handling curly braces and square brackets.
    Args:
        arg (str): The input string to be parsed.
    """
    curly_braces = re.search(r"\{.*?\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """defines the Holberton entry point command interpreter.

    Attributes:
    prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
            "BaseModel": BaseModel,
            "User": User,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "State": State,
            "Review": Review
            }

    def emptyline(self):
        """do nothing upon receiving an empty line"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_create(self, arg):
        """usage: Create <class>, create a new class instances
        and prints it id.
        """
        argl = parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(HBNBCommand.__classes[argl[0]]().id)
            storage.save()

    def do_show(self, arg):
        """usage: show <class> <id>. Prints the string representation
        of an instance base on the class name and id.
        """
        objdict = storage.all()
        if type(arg) != str:
            argl = parse(arg[0])
            if len(arg) > 1:
                arg = arg[1].split('"')[1]
        else:
            argl = parse(arg)
            if len(argl) > 1:
                arg = argl[1].split('"')[0]

        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif f"{argl[0]}.{arg}" not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """usage: destroy <class> <id>. Deletes an instance based on
        the class name and id.
        """
        objdict = storage.all()
        if type(arg) != str:
            argl = parse(arg[0])
            if len(arg) > 1:
                arg = arg[1].split('"')[1]
        else:
            argl = parse(arg)
            if len(argl) > 1:
                arg = argl[1].split('"')[0]

        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif f"{argl[0]}.{arg}" not in objdict:
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, arg):
        """usage: all <class>. Prints all string representation of
        all instances based or not on the class name.
        """
        if type(arg) != str:
            argl = parse(arg[0])

        else:
            argl = parse(arg)
        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name>
        <attribute_value>.
        to update an instance based on his ID.
        """
        argl = parse(arg)
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            print("** value missing **")
            return False
        if len(argl) >= 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and type
                        (obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        return True

    def do_count(self, arg):
        """usage: <class>.count(). retrieve the number of instances
        of a class.
        """
        count = 0
        for obj in storage.all().values():
            if arg[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def default(self, arg):
        """default behaviour for cmd module when input is invalid."""
        argdict = {
                "all": self.do_all,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "count": self.do_count,
                "update": self.do_update
                }

        parts = arg.split('.')
        cls = parts[0]
        command = parts[1].split("()")[0]
        command_args = parts[1].split("(")[1].split(")")[0].split(",")
        if command_args[0] == "":
            del command_args[0]
        for arg in command_args:
            arg = parse(arg)
        if cls in HBNBCommand.__classes:
            method_func = argdict[command]
            if method_func:
                args = []
                args.append(cls)
                args += command_args
                return method_func(args)
        print(f"*** Unknown syntax: {arg}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
