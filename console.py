#!/usr/bin/python3
"""
Contains the definition of 'HBNBCommand' class.
"""
import cmd
import re
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
    """
    Definition of 'HBNBCommand' class.
    """
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
        Creates a new instance based on the class name,
        saves it (to the JSON file) and prints the id.
        """
        kwargs = HBNBCommand.__parse(line)

        if not kwargs:
            return

        if not kwargs['cls_name']:
            print("** class name missing **")
            return

        if kwargs['cls_name'] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        obj = eval(f"{kwargs['cls_name']}()")
        obj.save()
        print(obj.id)

    def help_create(self):
        """
        Prints help documentation of 'create'
        """
        print(
            'Creates a new instance based on the class name, '
            'saves it (to the JSON file) and prints the id.'
        )
        print(
            '[Usage]:\n'
            '\tcreate <class_name> Or\n'
            '\t<class_name>.create()'
        )

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id.
        """
        kwargs = HBNBCommand.__parse(line)

        if not kwargs:
            return

        if not kwargs['cls_name']:
            print("** class name missing **")
            return

        if kwargs['cls_name'] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not kwargs['id']:
            print("** instance id missing **")
            return

        try:
            print(
                str(
                    storage.all()[f"{kwargs['cls_name']}.{kwargs['id']}"]
                )
            )
        except KeyError:
            print("** no instance found **")
            return

    def help_show(self):
        """
        Prints help documentation of 'show'
        """
        print(
            'Prints the string representation of an instance '
            'based on the class name and id.'
        )
        print(
            '[Usage]:\n'
            '\tshow <class_name> <id> Or\n'
            '\t<class_name>.show(<id>)'
        )

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        kwargs = HBNBCommand.__parse(line)

        if not kwargs:
            return

        if not kwargs['cls_name']:
            print("** class name missing **")
            return

        if kwargs['cls_name'] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not kwargs['id']:
            print("** instance id missing **")
            return

        try:
            del storage.all()[f"{kwargs['cls_name']}.{kwargs['id']}"]
            storage.save()
        except KeyError:
            print("** no instance found **")
            return

    def help_destroy(self):
        """
        Prints help documentation of 'destroy'
        """
        print(
            'Deletes an instance based on the class name and id '
            '(save the change into the JSON file).'
        )
        print(
            '[Usage]:\n'
            '\tdestroy <class_name> <id> Or\n'
            '\t<class_name>.destroy(<id>)'
        )

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name.
        """
        kwargs = HBNBCommand.__parse(line)

        if not kwargs:
            return

        if not kwargs['cls_name']:
            print([str(v) for v in storage.all().values()])
            return

        if kwargs['cls_name'] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        print(
            [
                str(v) for v in list(
                    filter(
                        lambda v: v.__class__.__name__ == kwargs['cls_name'],
                        storage.all().values()
                    )
                )
            ]
        )

    def help_all(self):
        """
        Prints help documentation of 'all'
        """
        print(
            'Prints all string representation of all instances '
            'based or not on the class name.'
        )
        print(
            '[Usage]:\n'
            '\tall Or\n'
            '\tall <class_name> Or\n'
            '\t<class_name>.all()'
        )

    def do_count(self, line):
        """
        Prints the number of instances based or not on the class name.
        """
        kwargs = HBNBCommand.__parse(line)

        if not kwargs:
            return

        if not kwargs['cls_name']:
            print(len(storage.all().values()))
            return

        if kwargs['cls_name'] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        print(
            len(
                list(
                    filter(
                        lambda v: v.__class__.__name__ == kwargs['cls_name'],
                        storage.all().values()
                    )
                )
            )
        )

    def help_count(self):
        """
        Prints help documentation of 'count'
        """
        print('Prints the number of instances based or not on the class name.')
        print(
            '[Usage]:\n'
            '\tcount Or\n'
            '\tcount <class_name> Or\n'
            '\t<class_name>.count()'
        )

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        """
        kwargs = HBNBCommand.__parse(line)

        if not kwargs:
            return

        if not kwargs['cls_name']:
            print("** class name missing **")
            return

        if kwargs['cls_name'] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not kwargs['id']:
            print("** instance id missing **")
            return

        if not kwargs['attr_name']:
            print("** attribute name missing **")
            return

        if not kwargs['attr_value']:
            print("** value missing **")
            return

        try:
            obj = storage.all()[f"{kwargs['cls_name']}.{kwargs['id']}"]

            setattr(obj, kwargs['attr_name'], kwargs['attr_value'])
            obj.save()
        except KeyError:
            print("** no instance found **")
            return

    def help_update(self):
        """
        Prints help documentation of 'update'
        """
        print(
            'Updates an instance based on the class name and id by adding '
            'or updating attribute (save the change into the JSON file).'
        )
        print(
            '[Usage]:\n'
            '\tupdate <class_name> <id> <attr_name> "<attr_value> Or\n'
            '\t<class_name>.update(<id>, <attr_name>, <attr_value>)'
        )

    def do_quit(self, line):
        """
        Quits the console.
        """
        quit()

    def help_quit(self):
        """
        Prints help documentation of 'quit'
        """
        print("quits the console.")
        print(
            '[Usage]:\n\tquit'
        )

    def do_EOF(self, line):
        """
        Quits the console.
        """
        quit()

    def help_EOF(self):
        """
        Prints help documentation of 'EOF'.
        """
        print("quits the console.")
        print(
            '[Usage]:\n\tEOF , Ctrl-D or Ctrl-Z'
        )

    def default(self, line):
        """
        Called when the command prefix is not recognized.
        """
        commands = {
            'show': self.do_show,
            'destroy': self.do_destroy,
            'all': self.do_all,
            'count': self.do_count,
            'update': self.do_update
        }

        try:
            command = re.findall(
                r"^.+\.(.+)\(.*\)",
                line
            )[0]
        except IndexError:
            print(f'** invalid syntax: {line} **')
            return

        if command not in commands:
            print(f'** command not exist: {command} **')
            return

        cls_name = re.findall(
            r"^(.+)\..+\(.*\)",
            line
        )[0]

        args = re.findall(r"^.+\..+\((.*)\)", line)[0]

        if len(re.findall(r'"', args)) % 2 != 0:
            print('** missing closing quotation **')
            return

        args = re.sub(
            r',(?=(?:[^"]*"[^"]*")*[^"]*$)',
            '',
            args
        )

        commands[command](f'{cls_name} {args}')

    def emptyline(self):
        """
        Called when an empty line is entered.
        """
        pass

    @staticmethod
    def __parse(line):
        """
        Parses the line
        """
        try:
            args = split(line)
        except ValueError:
            print('** missing closing quotation **')
            return

        kwargs = {}

        try:
            kwargs['cls_name'] = args[0]
        except IndexError:
            kwargs['cls_name'] = None

        try:
            kwargs['id'] = args[1]
        except IndexError:
            kwargs['id'] = None

        try:
            kwargs['attr_name'] = args[2]
        except IndexError:
            kwargs['attr_name'] = None

        try:
            kwargs['attr_value'] = HBNBCommand.__cast_to_type(args[3])
        except IndexError:
            kwargs['attr_value'] = None

        return kwargs

    @staticmethod
    def __cast_to_type(arg):
        """
        Casts arg type
        """
        if arg.isdigit():
            return int(arg)
        elif arg.replace('.', '').isdigit():
            return float(arg)

        return arg


if __name__ == "__main__":
    HBNBCommand().cmdloop()
