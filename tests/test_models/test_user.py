#!/usr/bin/python3
"""
Contains the unittests for 'User' class.
"""
import unittest
from models.user import User
from models import storage
from time import sleep
from datetime import datetime


class TestUser_init(unittest.TestCase):
    """
    Unittest for 'User' class.
    """
    def test_default_values(self):
        inst1 = User()
        self.assertEqual(inst1.last_name, '')
        self.assertEqual(inst1.first_name, '')
        self.assertEqual(inst1.email, '')
        self.assertEqual(inst1.password, '')

    def test_args_notused(self):
        inst1 = User(1)
        self.assertNotIn(1, inst1.__dict__.values())

    def test_instantiation(self):
        self.assertEqual(User, type(User()))

    def test_setting_attributes(self):
        inst1 = User(email="Ahmad@gmail", password=12)
        self.assertEqual(inst1.email, "Ahmad@gmail")
        self.assertEqual(inst1.password, 12)

    def test_id(self):
        self.assertEqual(type(User().id), str)

    def test_different_times(self):
        inst1 = User()
        inst2 = User()
        self.assertNotEqual(inst1.created_at, inst2.created_at)

    def test_different_ids(self):
        inst1 = User()
        inst2 = User()
        self.assertNotEqual(inst1.id, inst2.id)

    def test_different_update_times(self):
        inst1 = User()
        inst2 = User()
        self.assertNotEqual(inst1.updated_at, inst2.updated_at)

    def test_save(self):
        inst1 = User()
        time1 = inst1.updated_at
        sleep(0.1)
        inst1.save()
        time2 = inst1.updated_at
        self.assertGreater(time2, time1)

    def test_str_represnetation(self):
        inst1 = User()
        inst1.id = "123"
        dt = datetime.today()
        dt_repr = repr(dt)
        inst1.created_at = inst1.updated_at = dt
        inst1_str = inst1.__str__()
        self.assertIn("[User] " + "(123)", inst1_str)
        self.assertIn("'created_at': " + dt_repr, inst1_str)
        self.assertIn("'updated_at': " + dt_repr, inst1_str)


class TestUser_to_dict(unittest.TestCase):
    """Unit tests for testing to_dict() method in User Class"""
    def test_to_dict_keys(self):
        inst1 = User()
        inst1.last_name = "HereisMyName"
        inst1.password = 111
        self.assertIn("__class__", inst1.to_dict())
        self.assertIn("id", inst1.to_dict())
        self.assertIn("created_at", inst1.to_dict())
        self.assertIn("updated_at", inst1.to_dict())
        self.assertEqual(type(inst1.to_dict()['created_at']), str)
        self.assertEqual(type(inst1.to_dict()['updated_at']), str)
        self.assertIn("last_name", inst1.to_dict())
        self.assertIn("password", inst1.to_dict())

    def test_datetime_type(self):
        inst1 = User()
        self.assertEqual(str, type(inst1.to_dict()["created_at"]))
        self.assertEqual(str, type(inst1.to_dict()["updated_at"]))


if __name__ == '__main__':
    unittest.main()
