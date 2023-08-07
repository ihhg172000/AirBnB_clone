"""
Contains the unittests of 'BaseModel' class.
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Unittest of 'BaseModel' class.
    """
    def test_id(self):
        """
        Tests 'id' attribute.
        """
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertTrue(type(obj1.id) == str and type(obj2.id) == str)
        self.assertNotEqual(obj1.id, obj2.id)

    def test_created_at_and_updated_at(self):
        """
        Tests 'created_at & updated_at' attributes.
        """
        obj = BaseModel()
        self.assertTrue(
            type(obj.created_at) == datetime and
            type(obj.updated_at) == datetime
        )
        self.assertEqual(obj.created_at, obj.updated_at)

    def test_save(self):
        """
        Tests 'save' method.
        """
        obj = BaseModel()
        obj.save()
        self.assertGreater(obj.updated_at, obj.created_at)

    def test_to_dict(self):
        """
        Tests 'to_dict' method.
        """
        obj = BaseModel()
        obj.number = 89
        my_dict = obj.to_dict()
        self.assertEqual(my_dict['__class__'], obj.__class__.__name__)
        self.assertEqual(my_dict['id'], obj.id)
        self.assertEqual(my_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(my_dict['updated_at'], obj.updated_at.isoformat())
        self.assertEqual(my_dict['number'], 89)

    def test_create_instance_from_dictionary(self):
        """
        Tests create instance from dictionary aka kwargs
        """
        obj1 = BaseModel()
        my_dict = obj1.to_dict()
        obj2 = BaseModel(**my_dict)
        self.assertEqual(obj1.__dict__, obj2.__dict__)
        self.assertFalse(obj1 is obj2)

    def test_string_representation(self):
        """
        Tests string representation.
        """
        obj = BaseModel()
        self.assertEqual(
            obj.__str__(),
            f'[{obj.__class__.__name__}] ({obj.id}) {obj.__dict__}'
        )
