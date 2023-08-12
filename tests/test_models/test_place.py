#!/usr/bin/python3
"""
Contains the unittests for 'Place' class.
"""
import unittest
from models.place import Place
from models import storage
from time import sleep
from datetime import datetime


class TestPlace_init(unittest.TestCase):
    """
    Unittest for 'Place' class.
    """
    def test_default_args(self):
        inst1 = Place()
        self.assertEqual(inst1.city_id, '')
        self.assertEqual(inst1.user_id, '')
        self.assertEqual(inst1.name, '')
        self.assertEqual(inst1.description, '')
        self.assertEqual(inst1.number_rooms, 0)
        self.assertEqual(inst1.number_bathrooms, 0)
        self.assertEqual(inst1.max_guest, 0)
        self.assertEqual(inst1.price_by_night, 0)
        self.assertEqual(inst1.latitude, 0.0)
        self.assertEqual(inst1.longitude, 0.0)
        self.assertEqual(inst1.amenity_ids, [])
        
    def test_args_notused(self):
        inst1 = Place(1)
        self.assertNotIn(1, inst1.__dict__.values())

    def test_instantiation(self):
        self.assertEqual(Place, type(Place()))

    def test_using_kwargs(self):
        inst1 = Place(email="Ahmad@gmail", number=12, name="Aplace")
        self.assertEqual(inst1.email, "Ahmad@gmail")
        self.assertEqual(inst1.number, 12)
        self.assertEqual(inst1.name, "Aplace")

    def test_id(self):
        self.assertEqual(type(Place().id), str)

    def test_different_times(self):
        inst1 = Place()
        inst2 = Place()
        self.assertNotEqual(inst1.created_at, inst2.created_at)

    def test_different_ids(self):
        inst1 = Place()
        inst2 = Place()
        self.assertNotEqual(inst1.id, inst2.id)

    def test_different_update_times(self):
        inst1 = Place()
        inst2 = Place()
        self.assertNotEqual(inst1.updated_at, inst2.updated_at)

    def test_save(self):
        inst1 = Place()
        time1 = inst1.updated_at
        sleep(0.1)
        inst1.save()
        time2 = inst1.updated_at
        self.assertGreater(time2, time1)

    def test_str_represnetation(self):
        inst1 = Place()
        inst1.id = "123"
        dt = datetime.today()
        dt_repr = repr(dt)
        inst1.created_at = inst1.updated_at = dt
        inst1_str = inst1.__str__()
        self.assertIn("[Place] " + "(123)", inst1_str)
        self.assertIn("'created_at': " + dt_repr, inst1_str)
        self.assertIn("'updated_at': " + dt_repr, inst1_str)


class TestPlace_to_dict(unittest.TestCase):
    """Unit tests for testing to_dict() method in Place Class"""
    def test_to_dict_keys(self):
        inst1 = Place()
        inst1.name = "Place"
        inst1.city_id = 111
        self.assertIn("__class__", inst1.to_dict())
        self.assertIn("id", inst1.to_dict())
        self.assertIn("created_at", inst1.to_dict())
        self.assertIn("updated_at", inst1.to_dict())
        self.assertEqual(type(inst1.to_dict()['created_at']), str)
        self.assertEqual(type(inst1.to_dict()['updated_at']), str)
        self.assertIn("name", inst1.to_dict())
        self.assertIn("city_id", inst1.to_dict())

    def test_datetime_type(self):
        inst1 = Place()
        self.assertEqual(str, type(inst1.to_dict()["created_at"]))
        self.assertEqual(str, type(inst1.to_dict()["updated_at"]))

    def test_attributes_type(self):
        inst1 = Place(city_id='123', user_id='456', name='Placee',
                description='text', longitude=1.2, amenity_ids=[1, 2, 3])
        self.assertEqual(str, type(inst1.to_dict()['city_id']))
        self.assertEqual(str, type(inst1.to_dict()['user_id']))
        self.assertEqual(str, type(inst1.to_dict()['name']))
        self.assertEqual(str, type(inst1.to_dict()['description']))
        self.assertEqual(float, type(inst1.to_dict()['longitude']))
        self.assertEqual(list, type(inst1.to_dict()['amenity_ids']))


if __name__ == '__main__':
    unittest.main()
