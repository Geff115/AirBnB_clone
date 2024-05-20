#!/usr/bin/python3
"""An Amenity class that inherits from BaseModel"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel"""

    name = ""

    @classmethod
    def all(cls):
        """Returns a dictionary of all Amenity instances"""
        from models import storage

        return ([obj for obj in storage.all().values()
                if isinstance(obj, cls)])
