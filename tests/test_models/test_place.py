#!/usr/bin/python3
"""
Contains the unittests for 'Place' class.
"""
import unittest
from models.place import Place
from models import storage
from time import sleep
from datetime import datetime


class TestPlace(unittest.TestCase):
    """
    Unittest for 'Place' class.
    """
    def test_default_args(self):
        """
        Tests default args.
        """
        inst = Place()
        self.assertEqual(inst.city_id, '')
        self.assertEqual(inst.user_id, '')
        self.assertEqual(inst.name, '')
        self.assertEqual(inst.description, '')
        self.assertEqual(inst.number_rooms, 0)
        self.assertEqual(inst.number_bathrooms, 0)
        self.assertEqual(inst.max_guest, 0)
        self.assertEqual(inst.price_by_night, 0)
        self.assertEqual(inst.latitude, 0.0)
        self.assertEqual(inst.longitude, 0.0)
        self.assertEqual(inst.amenity_ids, [])

    def test_args_not_used(self):
        """
        Tests args not used.
        """
        inst = Place(1)
        self.assertNotIn(1, inst.__dict__.values())

    def test_instantiation(self):
        """
        Tests instantiation.
        """
        self.assertEqual(Place, type(Place()))

    def test_using_kwargs(self):
        """
        Tests using kwargs.
        """
        inst = Place(email="Ahmad@gmail", number=12)
        self.assertEqual(inst.email, "Ahmad@gmail")
        self.assertEqual(inst.number, 12)

    def test_id_type(self):
        """
        Tests id type.
        """
        self.assertEqual(type(Place().id), str)

    def test_create_at_different_times(self):
        """
        Tests create at different times.
        """
        inst1 = Place()
        inst2 = Place()
        self.assertNotEqual(inst1.created_at, inst2.created_at)

    def test_different_ids(self):
        """
        Tests different ids.
        """
        inst1 = Place()
        inst2 = Place()
        self.assertNotEqual(inst1.id, inst2.id)

    def test_update_at_different_times(self):
        """
        Tests update_at_different_times.
        """
        inst1 = Place()
        inst2 = Place()
        self.assertNotEqual(inst1.updated_at, inst2.updated_at)

    def test_save(self):
        """
        Tests save() method.
        """
        inst = Place()
        time1 = inst.updated_at
        sleep(0.1)
        inst.save()
        time2 = inst.updated_at
        self.assertGreater(time2, time1)

    def test_str_represnetation(self):
        """
        Tests string represnetation.
        """
        inst = Place()
        inst.id = "123"
        dt = datetime.today()
        dt_repr = repr(dt)
        inst.created_at = inst.updated_at = dt
        inst_str = inst.__str__()
        self.assertIn("[Place] " + "(123)", inst_str)
        self.assertIn("'created_at': " + dt_repr, inst_str)
        self.assertIn("'updated_at': " + dt_repr, inst_str)

    def test_to_dict(self):
        """
        Tests to_dict().
        """
        inst = Place()
        inst.name = "HereisMyName"
        inst.number = 111
        inst_dict = inst.to_dict()
        self.assertEqual(inst_dict["__class__"], inst.__class__.__name__)
        self.assertEqual(inst_dict["id"], inst.id)
        self.assertEqual(inst_dict["created_at"], inst.created_at.isoformat())
        self.assertEqual(inst_dict["updated_at"], inst.updated_at.isoformat())
        self.assertEqual(type(inst_dict['created_at']), str)
        self.assertEqual(type(inst_dict['updated_at']), str)
        self.assertEqual(inst_dict["name"], inst.name)
        self.assertEqual(inst_dict["number"], inst.number)


if __name__ == '__main__':
    unittest.main()
