#!/usr/bin/python3
"""A Review class that inherits from BaseModel"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialization method of an instance of Review"""

        super().__init__(*args, **kwargs)
        self.place_id = kwargs.get("place_id", "")
        self.user_id = kwargs.get("user_id", "")
        self.text = kwargs.get("text", "")

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

    @classmethod
    def destroy(cls, obj_id):
        """Destroys an instance of Review by ID"""
        from models import storage

        key = f"{cls.__name__}.{obj_id}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()
            return (True)
        return (False)

    @classmethod
    def update(cls, obj_id, obj_dict):
        """Updates an instance of Review by ID"""
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
