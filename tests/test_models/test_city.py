#!/usr/bin/python3
"""
Contains the unittests for 'City' class.
"""
import unittest
from models.city import City
from models import storage
from time import sleep
from datetime import datetime


class TestCity(unittest.TestCase):
    """
    Unittest for 'City' class.
    """
    def test_default_values(self):
        """
        Tests default values.
        """
        inst = City()
        self.assertEqual(inst.state_id, '')
        self.assertEqual(inst.name, '')

    def test_args_not_used(self):
        """
        Tests args not used.
        """
        inst = City(1)
        self.assertNotIn(1, inst.__dict__.values())

    def test_instantiation(self):
        """
        Tests instantiation.
        """
        self.assertEqual(City, type(City()))

    def test_using_kwargs(self):
        """
        Tests using kwargs.
        """
        inst = City(email="Ahmad@gmail", number=12)
        self.assertEqual(inst.email, "Ahmad@gmail")
        self.assertEqual(inst.number, 12)

    def test_id_type(self):
        """
        Tests id type.
        """
        self.assertEqual(type(City().id), str)

    def test_create_at_different_times(self):
        """
        Tests create at different times.
        """
        inst1 = City()
        inst2 = City()
        self.assertNotEqual(inst1.created_at, inst2.created_at)

    def test_different_ids(self):
        """
        Tests different ids.
        """
        inst1 = City()
        inst2 = City()
        self.assertNotEqual(inst1.id, inst2.id)

    def test_update_at_different_times(self):
        """
        Tests update_at_different_times.
        """
        inst1 = City()
        inst2 = City()
        self.assertNotEqual(inst1.updated_at, inst2.updated_at)

    def test_save(self):
        """
        Tests save() method.
        """
        inst = City()
        time1 = inst.updated_at
        sleep(0.1)
        inst.save()
        time2 = inst.updated_at
        self.assertGreater(time2, time1)

    def test_str_represnetation(self):
        """
        Tests string represnetation.
        """
        inst = City()
        inst.id = "123"
        dt = datetime.today()
        dt_repr = repr(dt)
        inst.created_at = inst.updated_at = dt
        inst_str = inst.__str__()
        self.assertIn("[City] " + "(123)", inst_str)
        self.assertIn("'created_at': " + dt_repr, inst_str)
        self.assertIn("'updated_at': " + dt_repr, inst_str)

    def test_to_dict(self):
        """
        Tests to_dict().
        """
        inst = City()
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
