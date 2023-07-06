#!/usr/bin/python3
""" Console for AirBnB"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage 


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

    def do_create(self, line):
        """ 
        
        """
        if line is None:
            print("** class name missing **")
        elif line not in FileStorage.class_dict:
            print("** class doesn't exist **")
        else:
            mew = FileStorage.class_dict[line]()
            FileStorage.new(mew, mew)
            FileStorage.save(self)
            print(mew.id)
    
    def do_show(self, line):
        """ 
        
        """
        if line is None:
            print("** class name missing **")
        if line is not None:
            args = line.split(" ")
        else:
            print("** class name doesn't exist **")
        # if args[1] not in FileStorage.class_dict:
        #     print("** class doesn't exist **")
          
        # if args[2] != "id":
        #     print("** instance id missing **")
        # else:
        #     for k in FileStorage.__objects.keys():
        #         id = k.split(".")
        #         if id[1] != args[2]:
        #             print("** no instance found **")
        #         else:
        #             self.__str__
        
        
            

    def emptyline(self):
        """
        Do nothing when an empty line is entered
        """
        pass



if __name__ == '__main__':
    HBNBCommand().cmdloop()
