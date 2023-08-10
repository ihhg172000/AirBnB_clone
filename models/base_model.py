"""
Contains the definition of 'BaseModel' class.
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Definition of 'BaseModel' class.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes an instance.
        """
        if kwargs:
            for k, v in kwargs.items():
                if k != '__class__':
                    if k in ['created_at', 'updated_at']:
                        setattr(self, k, datetime.fromisoformat(v))
                    else:
                        setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the instance.
        """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """
        Updates the instance attribute updated_at with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dict containing all keys/values of __dict__ of the instance.
        """
        my_dict = {'__class__': self.__class__.__name__}
        for k, v in self.__dict__.items():
            my_dict[k] = v if type(v) != datetime else v.isoformat()
        return my_dict
