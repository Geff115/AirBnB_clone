#!/usr/bin/python3
"""A Place class that inherits from BaseModel"""


from models.base_model import BaseModel


class Place(BaseModel):
    """Place class that inherits from BaseModel."""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    @classmethod
    def all(cls):
        """Returns a dictionary of all Place instances"""
        from models import storage

        return ([obj for obj in storage.all().values()
                if isinstance(obj, cls)])

    @classmethod
    def show(cls, obj_id):
        """Returns an instance of Place by id"""
        from models import storage

        all_instances = storage.all()
        for instance in all_instances.values():
            if isinstance(instance, cls) and instance.id == obj_id:
                return (instance)
        return (None)

    @classmethod
    def destroy(cls, obj_id):
        """Destroys an instance of Place by ID"""
        from models import storage

        key = f"{cls.__name__}.{obj_id}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()
            return (True)
        return (False)

    @classmethod
    def update(cls, obj_id, attr_name, attr_value):
        """Updates an instance of Place by ID"""
        from models import storage

        instance = cls.show(obj_id)
        if instance:
            setattr(instance, attr_name, attr_value)
            instance.save()
            return (True)
        return (False)
