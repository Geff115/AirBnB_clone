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


class BaseModel:
    """The BaseModel class"""

    def __init__(self):
        """Initialization method"""

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

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


