"""
Contains the definition of 'User' class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Definition of 'User' class.
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
