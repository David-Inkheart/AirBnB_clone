#!/usr/bin/python3
'''
class FileStorage that serializes instances to a
JSON file and deserializes JSON file to instances
'''
import json
from datetime import datetime
'''from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import path'''


class FileStorage:
    '''serializes and deserializes instances
    '''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''returns the dictionary __objects
        '''
        return self.__objects

    def new(self, obj):
        ''' sets in __objects the obj with key <obj class name>.id
        '''
        self.__objects["{}.{}".format(obj.__class__.__name__,
                                      obj.id)] = obj

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)
        '''
        '''
        dummy = {}
        for key, value in self.__objects.items():
            dummy[key] = value.to_dict()
        '''
        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.base_model import BaseModel
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        dummy = self.__objects.copy()
        for key, value in dummy.items():
            dummy[key] = value.to_dict()

        with open(self.__file_path, mode="w") as write_file:
            write_file.write(json.dumps(dummy))

        for key, value in self.__objects.items():
            if type(value.created_at) is str:
                value.created_at = datetime.strptime(
                    value.created_at, '%Y-%m-%dT%H:%M:%S.%f')
            if type(value.updated_at) is str:
                value.updated_at = datetime.strptime(
                    value.updated_at, '%Y-%m-%dT%H:%M:%S.%f')

    def reload(self):
        '''deserializes the JSON file to __objects
        '''
        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.base_model import BaseModel
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        try:
            with open(self.__file_path, mode="r") as read_file:
                dummy = json.loads(read_file.read())
            for key, value in dummy.items():
                self.__objects[key] = eval(value['__class__'])(**value)
        except FileNotFoundError:
            pass
