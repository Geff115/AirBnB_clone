#!/usr/bin/python3
"""A Review class that inherits from BaseModel"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""

    @classmethod
    def all(cls):
        """Returns a dictionary of all Review instances"""
        from models import storage

        return ([obj for obj in storage.all().values()
                if isinstance(obj, cls)])

    @classmethod
    def show(cls, obj_id):
        """Returns an instance of Review by id"""
        from models import storage

        all_instances = storage.all()
        for instance in all_instances.values():
            if isinstance(instance, cls) and instance.id == obj_id:
                return (instance)
        return (None)
