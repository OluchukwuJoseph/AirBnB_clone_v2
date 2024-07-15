#!/usr/bin/python3
""" Place Module for HBNB project """
import os
import sys
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel):
    """ A place to stay """
    if os.getenv('HBNB_TYPE_STORAGE') == 'file':
        # File storage will be used
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
    elif os.getenv('HBNB_TYPE_STORAGE') == 'db':
        # DB storage will be used
        __tabalename__ = 'places'

        city_id = Column(String(60), ForeignKey('cities.id'))
        user_id = Column(String(60), ForeignKey('users.id'))
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)

        user = relationship('User', back_populates='places')
        cities = relationship('City', back_populates='places')
    else:
        # If not Storage Type was specified return error
        sys.stderr.write('Unkwown FILE_TYPE_STORAGE\n')
        sys.exit(1)
