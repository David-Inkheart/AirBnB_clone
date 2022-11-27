#!/usr/bin/python3
'''
class BaseModel that defines all common attributes/methods
for other classes
'''
from datetime import datetime
import uuid
from models import storage


class BaseModel:
    '''super class
    '''
    def __init__(self, *args, **kwargs):
        '''initializes an instance
        '''
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at':
                        self.created_at = datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f')
                    elif key == 'updated_at':
                        self.updated_at = datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f')
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        '''return a user friendly string
        '''
        return '[{}] ({}) {}'.format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        '''updates the public instance attribute 'updated_at'
        with the current datetime
        '''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''returns a dictionary containing all keys/values
        of __dict__ of the instance
        '''
        if type(self.created_at) is str:
            self.created_at = datetime.strptime(
                self.created_at, '%Y-%m-%dT%H:%M:%S.%f')
        if type(self.updated_at) is str:
            self.updated_at = datetime.strptime(
                self.updated_at, '%Y-%m-%dT%H:%M:%S.%f')
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        res = self.__dict__.copy()
        res['__class__'] = self.__class__.__name__
        return res
