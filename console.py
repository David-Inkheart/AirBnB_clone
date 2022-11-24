#!/usr/bin/python3
'''
program called console.py that contains
the entry point of the command interpreter
'''


from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import cmd
import models
import sys


class HBNBCommand(cmd.Cmd):
    '''
    commandline interface to manage data
    '''
    intro = None
    prompt = '(hbnb) '
    file = 'file.json'

    ''' ------basic console commands----- '''

    def do_EOF(self, line):
        '''Clear the screen and return to prompt:  EOF'''
        print()
        return True

    def do_quit(self, arg):
        '''close the console, and exit:  QUIT'''
        return True

    def do_create(self, arg):
        '''Creates a new instance of BaseModel
        saves it (to the JSON file) and prints the id
        '''
        if not arg:
            print ('** class name missing **')
        elif arg == 'BaseModel':
            x = BaseModel()
            x.save()
            print(x.id)
        elif arg[0] != 'BaseModel':
            print ("** class doesn't exist **")

    def do_show(self, arg):
        '''Prints the string representation of an instance
        based on the class name and id
        '''
        arg_list = arg.split(' ')
        arg_list.append('x')
        if arg_list[0] == '':
           print('** class name missing **')
        elif arg_list[0] != 'BaseModel':
           print("** class doesn't exist **")
        elif arg_list[1] == 'x':
           print('** instance id missing **')
        elif arg_list[1]:
            storage = FileStorage().all()
            for key in storage:
                if key == 'BaseModel.' + arg_list[1]:
                    print(BaseModel(storage[key]))
                    return 
            print('** no instance found **')
                

if __name__ == '__main__':
    HBNBCommand().cmdloop()
