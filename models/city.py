#!/usr/bin/python3
"""A City class that inherits from BaseModel"""


from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherits from BaseModel"""

    state_id = ""
    name = ""

    @classmethod
    def all(cls):
        """Returns a dictionary of all City instances"""
        from models import storage

        return ([obj for obj in storage.all().values()
                if isinstance(obj, cls)])
