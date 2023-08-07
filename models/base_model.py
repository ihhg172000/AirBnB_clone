"""
Contains the definition of 'BaseModel' class.
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    Definition of 'BaseModel' class,
    that defines all common attributes/methods for other classes.
    """
    def __init__(self):
        """
        Initializes an instance.
        """
        self.id = str(uuid.uuid4())
        now = datetime.now()
        self.created_at = now
        self.updated_at = now

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

    def to_dict(self):
        """
        Returns a dict containing all keys/values of __dict__ of the instance.
        """
        my_dict = {'__class__': self.__class__.__name__}
        for k, v in self.__dict__.items():
            my_dict[k] = v if type(v) != datetime else v.isoformat()
        return my_dict
