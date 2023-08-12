#!/usr/bin/python3
"""
Contains the unittests for 'Review' class.
"""
import unittest
from models.review import Review
from models import storage
from time import sleep
from datetime import datetime


class TestReview_init(unittest.TestCase):
    """
    Unittest for 'Review' class.
    """
    def test_args_notused(self):
        inst1 = Review(1)
        self.assertNotIn(1, inst1.__dict__.values())

    def test_instantiation(self):
        self.assertEqual(Review, type(Review()))

    def test_using_kwargs(self):
        inst1 = Review(text="Great", number=12, place_id="50")
        self.assertEqual(inst1.text, "Great")
        self.assertEqual(inst1.number, 12)
        self.assertEqual(inst1.place_id, "50")

    def test_id(self):
        self.assertEqual(type(Review().id), str)
        self.assertEqual(type(Review().place_id), str)

    def test_different_creation_times(self):
        inst1 = Review()
        sleep(0.1)
        inst2 = Review()
        self.assertLess(inst1.created_at, inst2.created_at)

    def test_unique_ids(self):
        inst1 = Review()
        inst2 = Review()
        self.assertNotEqual(inst1.id, inst2.id)

    def test_different_update_times(self):
        inst1 = Review()
        sleep(0.1)
        inst2 = Review()
        self.assertLess(inst1.updated_at, inst2.updated_at)

    def test_save(self):
        inst1 = Review()
        time1 = inst1.updated_at
        sleep(0.1)
        inst1.save()
        time2 = inst1.updated_at
        self.assertGreater(time2, time1)

    def test_str_represnetation(self):
        inst1 = Review()
        inst1.id = "123"
        dt = datetime.today()
        dt_repr = repr(dt)
        inst1.created_at = inst1.updated_at = dt
        inst1_str = inst1.__str__()
        self.assertIn("[Review] " + "(123)", inst1_str)
        self.assertIn("'created_at': " + dt_repr, inst1_str)
        self.assertIn("'updated_at': " + dt_repr, inst1_str)


class TestReview_to_dict(unittest.TestCase):
    """Unit tests for testing to_dict() method in Review Class"""
    def test_to_dict_keys(self):
        inst1 = Review()
        inst1.name = "HereisMyName"
        inst1.my_number = 111
        self.assertIn("__class__", inst1.to_dict())
        self.assertIn("id", inst1.to_dict())
        self.assertIn("created_at", inst1.to_dict())
        self.assertIn("updated_at", inst1.to_dict())
        self.assertEqual(type(inst1.to_dict()['created_at']), str)
        self.assertEqual(type(inst1.to_dict()['updated_at']), str)
        self.assertIn("name", inst1.to_dict())
        self.assertIn("my_number", inst1.to_dict())

    def test_datetime_type(self):
        inst1 = Review()
        self.assertEqual(str, type(inst1.to_dict()["created_at"]))
        self.assertEqual(str, type(inst1.to_dict()["updated_at"]))


if __name__ == '__main__':
    unittest.main()
