#!/usr/bin/python3
'''
class FileStorage that serializes instances to a
JSON file and deserializes JSON file to instances
'''
import json


class FileStorage:
    '''serializes and deserializes instances
    '''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''returns the dictionary __objects
        '''
        return FileStorage.__objects

    def new(self, obj):
        ''' sets in __objects the obj with key <obj class name>.id
        '''
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__,
                                             obj.id)] = obj.to_dict()

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)
        '''

        with open(FileStorage.__file_path, mode="w") as write_file:
            write_file.write(json.dumps(FileStorage.__objects))

    def reload(self):
        '''deserializes the JSON file to __objects
        '''
        try:
            with open(FileStorage.__file_path, mode="r") as read_file:
                FileStorage.__objects = json.loads(read_file.read())
        except Exception:
            pass
