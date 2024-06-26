#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.text), str)

    def test_command_line_params(self):
        """Test if Command line parameters are actually added"""
        params = {'place_id': "61c216cf-9d55-4765-b730-974ac2642a1d",
                  'user_id': "16c216cf-9d55-4763-b730-974ac2642a1d",
                  'text': "Nice place!"
                  }
        obj = self.value(**params)

        self.assertEqual(obj.place_id, params['place_id'])
        self.assertEqual(obj.user_id, params['user_id'])
        self.assertEqual(obj.text, params['text'])

        # Test default values
        new_dict = obj.to_dict()
        self.assertEqual(obj.id, new_dict['id'])
        self.assertEqual(obj.created_at.isoformat(), new_dict['created_at'])
        self.assertEqual(obj.updated_at.isoformat(), new_dict['updated_at'])
