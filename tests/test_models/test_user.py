#!/usr/bin/python3
"""Defines unittests for models/user.py.

Unittest classes:
    TestUser_instantiation
    TestUser_save
    TestUser_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


def test_no_args_instantiates(self):
    self.assertEqual(User, type(User()))


def test_new_instance_stored_in_objects(self):
    self.assertIn(User(), models.storage.all().values())


def test_id_is_public_str(self):
    self.assertEqual(str, type(User().id))


def test_created_at_is_public_datetime(self):
    self.assertEqual(datetime, type(User().created_at))


def test_updated_at_is_public_datetime(self):
    self.assertEqual(datetime, type(User().updated_at))


def test_email_is_public_str(self):
    self.assertEqual(str, type(User.email))


def test_password_is_public_str(self):
    self.assertEqual(str, type(User.password))


def test_first_name_is_public_str(self):
    self.assertEqual(str, type(User.first_name))


def test_last_name_is_public_str(self):
    self.assertEqual(str, type(User.last_name))


def test_to_dict_contains_added_attributes(self):
    us = User()
    us.middle_name = "Holberton"
    us.my_number = 98
    self.assertEqual("Holberton", us.middle_name)
    self.assertIn("my_number", us.to_dict())


def test_to_dict_datetime_attributes_are_strs(self):
    us = User()
    us_dict = us.to_dict()
    self.assertEqual(str, type(us_dict["id"]))
    self.assertEqual(str, type(us_dict["created_at"]))
    self.assertEqual(str, type(us_dict["updated_at"]))


def test_to_dict_output(self):
    dt = datetime.today()
    us = User()
    us.id = "123456"
    us.created_at = us.updated_at = dt
    testdict = {
        'id': '123456',
        '__class__': 'User',
        'created_at': dt.isoformat(),
        'updated_at': dt.isoformat(),
    }
    self.assertDictEqual(us.to_dict(), testdict)


def test_contrast_to_dict_dunder_dict(self):
    us = User()
    self.assertNotEqual(us.to_dict(), us.__dict__)


def test_to_dict_with_arg(self):
    us = User()
    with self.assertRaises(TypeError):
        us.to_dict(None)


if __name__ == "__main__":
    unittest.main()
