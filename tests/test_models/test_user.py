#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.password), str)

    def test_command_line_params(self):
        """Test if Command line parameters are actually added"""
        params = {'first_name': "Joseph",
                  'last_name': "Oluchukwu",
                  'password': "user_pwd",
                  'email': "user@gmail.com"
                  }
        obj = self.value(**params)

        self.assertEqual(obj.first_name, params['first_name'])
        self.assertEqual(obj.last_name, params['last_name'])
        self.assertEqual(obj.password, params['password'])
        self.assertEqual(obj.email, params['email'])
        new_dict = obj.to_dict()
        # Test default values
        self.assertEqual(obj.id, new_dict['id'])
        self.assertEqual(obj.created_at.isoformat(), new_dict['created_at'])
        self.assertEqual(obj.updated_at.isoformat(), new_dict['updated_at'])
