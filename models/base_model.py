#!/usr/bin/python3


"""
This is a Python script with a BaseModel class.
ARGS:

    id: Public instance attribute of the class that uses the uuid module
    to create an id.
    created_at: This is a public instance attribute of the class that uses
    the datetime module.
    updated_at: This is a public instance attribute of the class that uses
    the datetime module.
    str: returns a string representation of the object.
    to_dict: returns a dictionary containing all keys/values of the instances.
"""


from uuid import uuid4
from datetime import datetime
import json
from os import path

class BaseModel:
    """The BaseModel class"""

     def __init__(self, *args, **kwargs):
        """a recreation of an instance with dictionary representation"""

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """str method that returns a string representation of the object"""

        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """Updates the public instance attribute updated_at
        with the current datetime.
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__
        of the instance: self.__dict__, __class__ as a key
        with the value of the class name, created_at and updated_at converted
        to isoformat.
        """

        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return (new_dict)

class FileStorage:
    """link of BaseModel to Filestorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary of all objects"""
        return FileStorage.__objects

    def new(self, obj):
        """new method that adds a new object to the __objects dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """this method serializes all objects to a JSON file"""
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """the reload method deserializes the JSON file to objects if the file exists"""
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                loaded_objects = json.load(file)
                for key, value in loaded_objects.items():
                    class_name, obj_id = key.split('.')
                    class_obj = eval(class_name)
                    obj = class_obj(**value)
                    FileStorage.__objects[key] = obj
