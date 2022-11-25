#!/usr/bin/python3
'''
program called console.py that contains
the entry point of the command interpreter
'''


from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import cmd
import json
import models
import re
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
        arg_list.append('#')
        storage = FileStorage().all()
        if arg_list[0] == '':
           print('** class name missing **')
        elif arg_list[0] and arg_list[1] == '#':
            for key in storage:
                if arg_list[0] in key.split('.'):
                    print("** instance id missing **")
                    return
            print("** class doesn't exist **")
        elif arg_list[1]:
            for key in storage:
                if key == 'BaseModel.' + arg_list[1]:
                    print(storage[key])
                    return
            print('** no instance found **')

    def do_destroy(self, arg):
        '''Deletes an instance based on the class name and id'''
        arg_list = arg.split(' ')
        arg_list.append('#')
        storage = FileStorage().all()
        if arg_list[0] == '':
            print("** class name missing **")
        elif arg_list[0] and arg_list[1] == '#':
            for key in storage:
                if arg_list[0] in key.split('.'):
                    print("** instance id missing **")
                    return
            print("** class doesn't exist **")
        elif arg_list[1]:
            for key in storage:
                if key == 'BaseModel.' + arg_list[1]:
                    storage.pop(key)
                    return
            print('** no instance found **')

    def do_all(self, arg):
        '''Prints all string representation of all
        instances based or not on the class name'''
        storage = FileStorage().all()
        if not arg:
            print([j for i, j in storage.items()])
        else:
            class_list = []
            for key in storage:
                if arg in key.split('.'):
                    class_list.append(storage[key])
            if len(class_list) != 0:
                print(class_list)
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        ''' Updates an instance based on the class
        name and id by adding or updating attribute'''
        arg_list = arg.split(' ')
        arg_list.append('#')
        storage = FileStorage().all()
        if arg_list[0] == '':
            print("** class name missing **")
        elif arg_list[0] and arg_list[1] == '#':
            for key in storage:
                if arg_list[0] in key.split('.'):
                    print("** instance id missing **")
                    return
            print("** class doesn't exist **")
        elif arg_list[1]:
            for key in storage:
                if key == 'BaseModel.' + arg_list[1]:
                    if arg_list[2] == '#':
                        print("** attribute name missing **")
                    elif arg_list[3] == '#':
                        print("** value missing **")
                    else:
                        setattr(storage[key], arg_list[2], arg_list[3])
                        storage[key].save()
                    return
            print('** no instance found **')

if __name__ == '__main__':
    HBNBCommand().cmdloop()
