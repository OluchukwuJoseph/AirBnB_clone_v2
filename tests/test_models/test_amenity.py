#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_command_line_params(self):
        """Test if Command line parameters are actually added"""
        params = {'name': "Internet"}
        obj = self.value(**params)

        self.assertEqual(obj.name, params['name'])

        # Test default values
        new_dict = obj.to_dict()
        self.assertEqual(obj.id, new_dict['id'])
        self.assertEqual(obj.created_at.isoformat(), new_dict['created_at'])
        self.assertEqual(obj.updated_at.isoformat(), new_dict['updated_at'])
