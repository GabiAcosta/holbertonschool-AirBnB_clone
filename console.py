#!/usr/bin/python3
""" Console for AirBnB"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Simple command processor

    Args:
        Cmd: Used to read the input
        and execute a command
    """
    prompt = '(hbnb) '

    def do_help(self, arg: str) -> bool:
        """
        Displays undocumented commands
        """
        return super().do_help(arg)

    def do_EOF(self, line):
        """
        Reaches end of file(quits the program)
        """
        return True

    def do_quit(self, line):
        """
        Exits the program soft, clean and smoothly
        """
        return self.do_EOF

    def emptyline(self):
        """
        Do nothing when an empty line is entered
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()