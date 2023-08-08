import cmd
"""console.py file that contains the entry point of the command interpreter"""


class HBNBCommand(cmd.Cmd):
    """Our console class"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """quit implementation to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF implementation to exit the program"""
        return True

    def help_quit(self):
        """quit help documentation"""
        print("This method Quits the program\n")

    def help_EOF(self):
        """EOF help documentation"""
        print("This method Exits the program (Ctrl-D or Ctrl-Z).\n")

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
