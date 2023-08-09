#!/usr/bin/python3
""" Enty Point To The Console Module """


import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
"""from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review"""


class HBNBCommand(cmd.Cmd):
    """Our console class"""
    prompt = '(hbnb) '

    classes = {'BaseModel': BaseModel, 'User': User}

    def do_quit(self, line):
        """quit implementation to exit the program"""
        exit()

    def do_EOF(self, line):
        """EOF implementation to exit the program"""
        exit()

    def help_quit(self):
        """quit help documentation"""
        print("This method Quits the program\n")

    def help_EOF(self):
        """EOF help documentation"""
        print("This method Exits the program (Ctrl-D or Ctrl-Z).\n")

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id"""
        if not args:
            print("** class name missing **")
            return
        elif args not in self.classes:
            print("** class doesn't exist **")
            return
        obj = BaseModel()
        obj.save()  # should we use the class save or the storage save? - using both now
        print(obj.id)
        storage.save()

    def help_create(self):
        """Help info about the create command"""
        print("Creates an instance of any Class, saves it and print id")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        """Prints the string representation of an instance
        based on the class name and id"""
        input_split = args.partition(" ")
        class_n = input_split[0]
        class_id = input_split[2]
        if not class_n:
            print("** class name missing **")
            return
        elif class_n not in self.classes:
            print("** class doesn't exist **")
            print(HBNBCommand.classes)
            return
        elif not class_id:
            print("** instance id missing **")
            return
        instance_key = class_n + '.' + class_id
        try:
            print(str(storage.all()[instance_key]))
        except KeyError:
            print("** no instance found **")
            return

    def help_show(self):
        """Help info about the show command"""
        print("Shows the string representation of an instance")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        input_split = args.partition(" ")
        class_n = input_split[0]
        class_id = input_split[2]
        if not class_n:
            print("** class name missing **")
            return
        elif class_n not in self.classes:
            print("** class doesn't exist **")
            return
        elif not class_id:
            print("** instance id missing **")
            return
        instance_key = class_n + '.' + class_id
        try:
            del(storage.all()[instance_key])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        """Help info about the destroy command"""
        print("Deletes an instance based on the class name and id")
        print("[Usage]: destroy <classname> <objectsId>\n")

    def do_all(self, args):
        """Prints all string representation of all instances
        based or not on the class name."""
        output_list = []
        if args:
            input_split = args.partition(" ")
            if input_split[0] not in self.classes:
                print("** class doesn't exist **")
                return
            for k, v in  storage.all().items():
                output_list.append(str(v))
        else:
            for k, v in storage.all().items():
                output_list.append(str(v))
        print(output_list)

    def help_all(self):
        """Help info about the all command"""
        print("Prints all str representation of instances")
        print("[Usage]: all or all <classname>\n")

    def do_update(self, args):
        """Updates an instance based on the class name 
        and id by adding or updating attribute"""
        # Seperating class name
        input_split = args.partition(" ")
        if input_split[0]:
            class_n = input_split[0]
        else:
            print("** class name missing **")
            return
        
        # Missing class name
        if class_n not in self.classes:
            print("** class doesn't exist **")
            return

        # Seperating instance Id
        input_split = input_split[2].partition(" ")
        if input_split[0]:
            class_id = input_split[0]
        else:
            print("** instance id missing **")
            return

        # Missing instance id
        instance_key = class_n + '.' + class_id
        if instance_key not in storage.all():
            print("** no instance found **")
            return

        # Seperating Attribute name
        input_split = input_split[2].partition(" ")
        if input_split[0]:
            attr_name = input_split[0]
        else:
            print("** attribute name missing **")
            return

        # Seperating attribute value
        input_split = input_split[2].partition(" ")
        if input_split[0]:
            attr_value = input_split[0]
        else:
            print("** value missing **")
            return

        # Getting the Attr type
        attr_type = type(storage.all()[attr_name])

        # Casting the value into the type
        attr_value_type = attr_type(attr_value)

        new_dict = storage.all()[instance_key]

        new_dict.__dict__.update({attr_name: attr_value_type})

        new_dict.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()

