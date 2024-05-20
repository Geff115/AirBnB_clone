#!/usr/bin/python3


"""This class User inherits from the
BaseModel class.
"""


from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    @classmethod
    def all(cls):
        """Returns a dictionary of all User instances"""
        from models import storage

        return ([obj for obj in storage.all().values()
                if isinstance(obj, cls)])
