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

    def __init__(self, *args, **kwargs):
        """Initialize a new User instance"""

        super().__init__(*args, **kwargs)
        self.email = kwargs.get("email", "")
        self.password = kwargs.get("password", "")
        self.first_name = kwargs.get("first_name", "")
        self.last_name = kwargs.get("last_name", "")

    @classmethod
    def all(cls):
        """Returns a dictionary of all User instances"""
        from models import storage

        return ([obj for obj in storage.all().values()
                if isinstance(obj, cls)])

    @classmethod
    def show(cls, obj_id):
        """Returns an instance of User by ID"""
        from models import storage

        all_instances = storage.all()
        for instance in all_instances.values():
            if isinstance(instance, cls) and instance.id == obj_id:
                return (instance)
        return (None)

    @classmethod
    def destroy(cls, obj_id):
        """Destroys an instance of User by ID"""
        from models import storage

        key = f"{cls.__name__}.{obj_id}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()
            return (True)
        return (False)

    @classmethod
    def update(cls, obj_id, obj_dict):
        """Updates an instance of User by ID"""
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
