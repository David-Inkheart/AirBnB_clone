#!/usr/bin/python3
'''
program called console.py that contains
the entry point of the command interpreter
'''


import cmd
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity



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
            print('** class name missing **')
        elif arg == 'BaseModel':
            inst = BaseModel()
        elif arg == "User":
            inst = User()
        elif arg == "Place":
            inst = Place()
        elif arg == "State":
            inst = State()
        elif arg == "City":
            inst = City()
        elif arg == "Amenity":
            inst = Amenity()
        elif arg == "Review":
            inst = Review()
        else:
            print("** class doesn't exist **")
            return
        inst.save()
        print(inst.id)

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
                if key == arg_list[0] + "." + arg_list[1]:
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
                if key == arg_list[0] + '.' + arg_list[1]:
                    storage.pop(key)
                    return
            print('** no instance found **')

    def do_all(self, arg):
        '''Prints all string representation of all
        instances based or not on the class name'''
        storage = FileStorage().all()
        if not arg:
            print([j.__str__() for i, j in storage.items()])
        else:
            class_list = []
            for key in storage:
                if arg in key.split('.'):
                    class_list.append(storage[key].__str__())
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
                if key == arg_list[0] + '.' + arg_list[1]:
                    if arg_list[2] == '#':
                        print("** attribute name missing **")
                    elif arg_list[3] == '#':
                        print("** value missing **")
                    else:
                        setattr(storage[key], arg_list[2],
                                json.loads(arg_list[3]))
                        storage[key].save()
                    return
            print('** no instance found **')

    def emptyline(self):
        """
        When an empty line is entered in response to the prompt,
        it won't repeat the last nonempty command entered.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
