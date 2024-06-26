#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_command_line_params(self):
        """Test if Command line parameters are actually added"""
        params = {'name': "Lagos"}
        obj = self.value(**params)

        self.assertEqual(obj.name, params['name'])

        # Test default values
        new_dict = obj.to_dict()
        self.assertEqual(obj.id, new_dict['id'])
        self.assertEqual(obj.created_at.isoformat(), new_dict['created_at'])
        self.assertEqual(obj.updated_at.isoformat(), new_dict['updated_at'])
