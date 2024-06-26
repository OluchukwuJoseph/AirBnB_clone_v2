#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

    def test_command_line_params(self):
        """Test if Command line parameters are actually added"""
        params = {'user_id': "16c216cf-9d55-4763-b730-974ac2642a1d",
                  'city_id': "16c246cf-9d55-4763-b730-974ac2642a1d",
                  'name': "Little house",
                  'number_rooms': 4,
                  'number_bathrooms': 2,
                  'max_guest': 8,
                  'price_by_night': 150000.00,
                  'latitude': 37.773972,
                  'longitude': -122.431297
                  }
        obj = self.value(**params)

        self.assertEqual(obj.user_id, params['user_id'])
        self.assertEqual(obj.city_id, params['city_id'])
        self.assertEqual(obj.number_rooms, params['number_rooms'])
        self.assertEqual(obj.number_bathrooms, params['number_bathrooms'])
        self.assertEqual(obj.max_guest, params['max_guest'])
        self.assertEqual(obj.price_by_night, params['price_by_night'])
        self.assertEqual(obj.latitude, params['latitude'])
        self.assertEqual(obj.longitude, params['longitude'])

        # Test default values
        new_dict = obj.to_dict()
        self.assertEqual(obj.id, new_dict['id'])
        self.assertEqual(obj.created_at.isoformat(), new_dict['created_at'])
        self.assertEqual(obj.updated_at.isoformat(), new_dict['updated_at'])
