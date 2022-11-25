#!/usr/bin/python3
'''
class FileStorage that serializes instances to a
JSON file and deserializes JSON file to instances
'''
import json

class FileStorage:
    '''seralizes and deserializes instances
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
        print("{}: {}".format("##############", self.__objects))

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)
        '''
        dummy = {}
        for key, value in self.__objects.items():
            dummy[key] = value.to_dict()

        with open(FileStorage.__file_path, mode="w") as write_file:
            write_file.write(json.dumps(dummy))

    def reload(self):
        '''deserializes the JSON file to __objects
        '''
        '''
        with open(self.__file_path, mode="r") as read_file:
            dummy = json.loads(read_file.read())
        for key, value in dummy.items():
            self.__objects[key] = BaseModel(dummy)

        print("Reloaded Objects: {}".format(self.__objects))
        '''
        pass
