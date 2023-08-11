"""
Contains the unittests for 'BaseModel' class.
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel_init(unittest.TestCase):
    """
    Unittest for 'BaseModel' class.
    """
    def test_args_notused(self):
        inst1 = BaseModel(1)
        assertNotIn(1, inst1.__dict__.values())

    def test_instantiation(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_stored_in_objects(self):
        self.assertIn(BaseModel(), storage.all())

    def test_id(self):
        self.assertEqual(type(BaseModel().id), str)

    def test_different_times(self):
        inst1 = BaseModel()
        inst2 = BaseModel()
        self.assertNotEqual(inst1.created_at, inst2.created_at)

    def test_different_ids(self):
        inst1 = BaseModel()
        inst2 = BaseModel()
        self.assertNotEqual(inst1.id, inst2.id)

    def test_different_update_times(self):
        inst1 = BaseModel()
        inst2 = BaseModel()
        self.assertNotEqual(inst1.updated_at, inst2.updated_at)

    def test_save(self):
        inst1 = BaseModel()
        time1 = inst1.updated_at
        inst1.save()
        time2 = inst1.updated_at
        self.assertGreater(time2, time1)

    def test_str_represnetation(self):
        inst1 = BaseModel()
        inst1_str = inst1.__str__()
        self.assertIn("[BaseModel] " + "(" + inst1.id + ")", inst1_str)
        self.assertIn("'created_at': ", inst1_str)
        self.assertIn("'updated_at': ", inst1_str)

class TestBaseModel_to_dict(unittest.TestCase):
    """Unit tests for testing to_dict() method in BaseModel Class"""
    
    def test_to_dict_keys(self):
        inst1 = BaseModel()
        inst1.name = "HereisMyName"
        inst1.my_number = 0111
        self.assertIn("__class__", inst1.to_dict())
        self.assertIn("id", inst1.to_dict())
        self.assertIn("created_at", inst1.to_dict())
        self.assertIn("updated_at", inst1.to_dict())
        self.assertIn("name", inst1.to_dict())
        self.assertIn("my_number", inst1.to_dict())

    def test_datetime_type(self):
        inst1 = BaseModel()
        self.assertEqual(str, type(inst1.to_dict()["created_at"]))
        self.assertEqual


if __name__ == '__main__':
    unittest.main()
