#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_command_line_params(self):
        """Test if Command line parameters are actually added"""
        params = {'state_id': "16c216cf-9f55-4763-b730-974ac2642a1d",
                  'name': "Lagos Island"
                  }
        obj = self.value(**params)

        self.assertEqual(obj.state_id, params['state_id'])
        self.assertEqual(obj.name, params['name'])

        # Test default values
        new_dict = obj.to_dict()
        self.assertEqual(obj.id, new_dict['id'])
        self.assertEqual(obj.created_at.isoformat(), new_dict['created_at'])
        self.assertEqual(obj.updated_at.isoformat(), new_dict['updated_at'])
