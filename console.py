#!/usr/bin/python3
'''
program called console.py that contains
the entry point of the command interpreter
'''

<<<<<<< HEAD

=======
>>>>>>> 463cd63afa0e5006f803f8ca2285eb266ec8b8bd
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
<<<<<<< HEAD

=======
import re
import models
'''import sys'''
>>>>>>> 463cd63afa0e5006f803f8ca2285eb266ec8b8bd


class HBNBCommand(cmd.Cmd):
    '''
    commandline interface to manage data
    '''
    intro = None
    prompt = '(hbnb) '
    file = 'file.json'
    check_class = {"Amenity": Amenity, "BaseModel": BaseModel,
                   "City": City, "Place": Place, "Review": Review,
                   "State": State, "User": User}

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
<<<<<<< HEAD
=======
            return
>>>>>>> 463cd63afa0e5006f803f8ca2285eb266ec8b8bd
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
<<<<<<< HEAD
=======
        '''
        if not arg:
            print('** class name missing **')
            return
        if arg in check_class:
            arg_list = arg.split()
            inst = check_class[arg_list[0]]()
            inst.save()
            storage.reload()
            print(inst.id)
        else:
            print("** class doesn't exist **")
        inst.save()
        print(inst.id)
        '''
>>>>>>> 463cd63afa0e5006f803f8ca2285eb266ec8b8bd

    def do_show(self, arg):
        '''Prints the string representation of an instance
        based on the class name and id
        '''
        arg_list = arg.split(' ')
        arg_list.append('#')
        storage = FileStorage().all()
<<<<<<< HEAD
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
=======
        if arg_list[0] == '':
            print('** class name missing **')
        elif arg_list[0]:
            for key in storage:
                if arg_list[0] in key.split('.'):
                    if arg_list[1] and arg_list[1] != '#':
                        for key in storage:
                            if key == arg_list[0] + "." + arg_list[1]:
                                print(storage[key])
                                return
                        print('** no instance found **')
                        return
                    elif arg_list[1] == '#':
                        print("** instance id missing **")
                        return
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        '''Deletes an instance based on the class name and id'''
        arg_list = arg.split(' ')
        arg_list.append('#')
        storage = FileStorage().all()
        if arg_list[0] == '':
            print("** class name missing **")
        elif arg_list[0]:
            for key in storage:
                if arg_list[0] in key.split('.'):
                    if arg_list[1] and arg_list[1] != '#':
                        for key in storage:
                            if key == arg_list[0] + "." + arg_list[1]:
                                storage.pop(key)
                                return
                        print('** no instance found **')
                        return
                    elif arg_list[1] == '#':
                        print("** instance id missing **")
                        return
            print("** class doesn't exist **")

        '''
>>>>>>> 463cd63afa0e5006f803f8ca2285eb266ec8b8bd
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
<<<<<<< HEAD
            print('** no instance found **')
=======
            print('** no instance found **')'''
>>>>>>> 463cd63afa0e5006f803f8ca2285eb266ec8b8bd

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
<<<<<<< HEAD
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
=======
        elif arg_list[0]:
            for key in storage:
                if arg_list[0] in key.split('.'):
                    if arg_list[1] and arg_list[1] != '#':
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
                        return
                    elif arg_list[1] == '#':
                        print("** instance id missing **")
                        return
            print("** class doesn't exist **")
>>>>>>> 463cd63afa0e5006f803f8ca2285eb266ec8b8bd

    def emptyline(self):
        """
        When an empty line is entered in response to the prompt,
        it won't repeat the last nonempty command entered.
        """
        pass

<<<<<<< HEAD
=======
    def get_objects(self, instance=''):
        """
        Args:
            instance (:obj:`str`, optional): The instance to finds into
                the objects.
        Returns:
            list: If the `instance` argument is not empty, it will search
            only for objects that match the instance. Otherwise, it will show
            all instances in the file where all objects are stored.
        """
        objects = models.storage.all()

        if instance:
            keys = objects.keys()
            return [str(val) for key, val in objects.items()
                    if key.startswith(instance)]

        return [str(val) for key, val in objects.items()]

    def default(self, line):
        """
        When the command prefix is not recognized, this method
        looks for whether the command entered has the syntax:
            "<class name>.<method name>" or not,
        and links it to the corresponding method in case the
        class exists and the method belongs to the class.
        """

        if '.' in line:
            splitted = re.split(r'\.|\(|\)', line)
            class_name = splitted[0]
            method_name = splitted[1]

            if class_name in self.check_class:
                if method_name == 'all':
                    print(self.get_objects(class_name))
                elif method_name == 'count':
                    print(len(self.get_objects(class_name)))
                elif method_name == 'show':
                    class_id = splitted[2][1:-1]
                    self.do_show(class_name + ' ' + class_id)
                elif method_name == 'destroy':
                    class_id = splitted[2][1:-1]
                    self.do_destroy(class_name + ' ' + class_id)

>>>>>>> 463cd63afa0e5006f803f8ca2285eb266ec8b8bd

if __name__ == '__main__':
    HBNBCommand().cmdloop()
