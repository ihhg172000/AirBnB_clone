#!/usr/bin/python3
""" Enty Point To The Console Module """
import cmd
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Our console class"""
    prompt = '(hbnb) '
    classes = (
        'BaseModel',
        'User',
        'Place',
        'State',
        'City',
        'Amenity',
        'Review'
    )

    def do_create(self, line):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        """
        try:
            args = split(line)
        except ValueError:
            print('** no closing quotation **')
            return

        try:
            class_name = args[0]
        except IndexError:
            print("** class name missing **")
            return

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        obj = eval(f'{class_name}()')
        obj.save()
        print(obj.id)

    def help_create(self):
        """Help info about the create command"""
        print("Creates an instance of any Class, saves it and print id")
        print("[Usage]: create <className>\n")

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id.
        """
        try:
            args = split(line)
        except ValueError:
            print('** no closing quotation **')
            return

        try:
            class_name = args[0]
        except IndexError:
            print("** class name missing **")
            return

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        try:
            id = args[1]
        except IndexError:
            print("** instance id missing **")
            return

        try:
            print(str(storage.all()[f'{class_name}.{id}']))
        except KeyError:
            print("** no instance found **")
            return

    def help_show(self):
        """Help info about the show command"""
        print("Shows the string representation of an instance")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id.
        """
        try:
            args = split(line)
        except ValueError:
            print('** no closing quotation **')
            return

        try:
            class_name = args[0]
        except IndexError:
            print("** class name missing **")
            return

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        try:
            id = args[1]
        except IndexError:
            print("** instance id missing **")
            return

        try:
            del storage.all()[f'{class_name}.{id}']
            storage.save()
        except KeyError:
            print("** no instance found **")
            return

    def help_destroy(self):
        """Help info about the destroy command"""
        print("Deletes an instance based on the class name and id")
        print("[Usage]: destroy <classname> <objectsId>\n")

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name.
        """
        try:
            args = split(line)
        except ValueError:
            print('** no closing quotation **')
            return

        try:
            class_name = args[0]
        except IndexError:
            print([str(v) for v in storage.all().values()])
            return

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        print(
            [
                str(v) for v in list(
                    filter(
                        lambda v: v.__class__.__name__ == class_name,
                        storage.all().values()
                    )
                )
            ]
        )

    def help_all(self):
        """Help info about the all command"""
        print("Prints all str representation of instances")
        print("[Usage]: all or all <classname>\n")

    def do_update(self, line):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute.
        """
        try:
            args = split(line)
        except ValueError:
            print('** no closing quotation **')
            return

        try:
            class_name = args[0]
        except IndexError:
            print("** class name missing **")
            return

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        try:
            id = args[1]
        except IndexError:
            print("** instance id missing **")
            return

        try:
            attr_name = args[2]
        except IndexError:
            print("** attribute name missing **")
            return

        try:
            attr_value = args[3]
        except IndexError:
            print("** value missing **")
            return

        if attr_value.isdigit():
            attr_value = int(attr_value)
        elif attr_value.replace('.', '').isdigit():
            attr_value = float(attr_value)

        obj = storage.all()[f'{class_name}.{id}']

        setattr(obj, attr_name, attr_value)
        obj.save()

    def help_update(self):
        """Help info about the update command"""
        print(
            'Updates an instance based on the class name and id ' +
            'by adding or updating attribute'
        )
        print(
            '[Usage]: update <class name> <id> ' +
            '<attribute name> "<attribute value>"\n'
        )

    def do_quit(self, line):
        """quit implementation to exit the program"""
        quit()

    def help_quit(self):
        """quit help documentation"""
        print("This method Quits the program\n")

    def do_EOF(self, line):
        """EOF implementation to exit the program"""
        quit()

    def help_EOF(self):
        """EOF help documentation"""
        print("This method Exits the program (Ctrl-D or Ctrl-Z).\n")

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
