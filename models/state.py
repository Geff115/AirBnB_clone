#!/usr/bin/python3
"""A state class that inherits from BaseModel"""


from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherits from BaseModel"""

    name = ""

    @classmethod
    def all(cls):
        """Returns a dictionary of all State instances"""
        from models import storage

        return ([obj for obj in storage.all().values()
                if isinstance(obj, cls)])
