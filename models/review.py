"""
Contains the definition of 'Review' class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Definition of 'Review' class.
    """
    place_id = ''
    user_id = ''
    text = ''
