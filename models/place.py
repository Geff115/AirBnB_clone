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

    def __init__(self, *args, **kwargs):
        """Initialization method of an instance of Place"""

        super().__init__(*args, **kwargs)
        self.city_id = kwargs.get("city_id", "")
        self.user_id = kwargs.get("user_id", "")
        self.name = kwargs.get("name", "")
        self.description = kwargs.get("description", "")
        self.number_rooms = kwargs.get("number_rooms", 0)
        self.number_bathrooms = kwargs.get("number_bathrooms", 0)
        self.max_guest = kwargs.get("max_guest", 0)
        self.price_by_night = kwargs.get("price_by_night", 0)
        self.latitude = kwargs.get("latitude", 0.0)
        self.longitude = kwargs.get("longitude", 0.0)
        self.amenity_ids = kwargs.get("amenity_ids", [])

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
    def update(cls, obj_id, obj_dict):
        """Updates an instance of Place by ID"""
        from models import storage

        instance = storage.all()[f'{cls.__name__}.{obj_id}']
        if instance:
            for key, value in obj_dict.items():
                if hasattr(instance, key):
                    attr_type = type(getattr(instance, key))
                    setattr(instance, key, attr_type(value))
                else:
                    setattr(instance, key, value)
            instance.save()
            return (True)
        return (False)
