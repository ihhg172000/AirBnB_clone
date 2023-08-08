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
    def test_id_type(self):
        """
        Tests 'id' type.
        """
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)

    def test_each_instance_has_unique_id(self):
        """
        Tests each instance has unique 'id'.
        """
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_created_at_and_updated_at_types(self):
        """
        Tests 'created_at & updated_at' types.
        """
        obj = BaseModel()
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_created_at_and_updated_at_is_same_in_new_instance(self):
        """
        Tests 'created_at' and 'updated_at' is same in new instance.
        """
        obj = BaseModel()
        self.assertEqual(obj.created_at, obj.updated_at)
        self.assertTrue(obj.created_at is obj.updated_at)

    def test_updated_at_is_updated_when_save_is_called(self):
        """
        Tests 'updated_at' is updated when save is called.
        """
        obj = BaseModel()
        obj.save()
        self.assertNotEqual(obj.created_at, obj.updated_at)
        self.assertFalse(obj.created_at is obj.updated_at)

    def test_convert_an_instance_into_serializable_dict(self):
        """
        Tests convert an instance into serializable dict.
        """
        obj = BaseModel()
        obj.number = 89
        obj.name = 'alx'
        my_dict = obj.to_dict()
        self.assertEqual(my_dict['__class__'], obj.__class__.__name__)
        self.assertEqual(my_dict['id'], obj.id)
        self.assertEqual(my_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(my_dict['updated_at'], obj.updated_at.isoformat())
        self.assertEqual(my_dict['number'], 89)
        self.assertEqual(my_dict['name'], 'alx')

    def test_create_an_instance_from_dict(self):
        """
        Tests create instance from dict aka kwargs.
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
