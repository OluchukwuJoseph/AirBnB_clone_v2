#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        # DB storage will be used
        __tablename__ = 'places'

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

        cities = relationship('City', back_populates='places')
        user = relationship('User', back_populates='places')
        reviews = relationship('Review', back_populates='place',
                               cascade='all, delete-orphan')
    else:
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

        @property
        def reviews(self):
            """
                Returns the list of Review instances with place_id equals to
                the current Place.id.
                It will be the FileStorage relationship between Place & Review
            """
            from models import storage
            from models.review import Review

            reviews = []
            review_instances = storage.all(Review).values()
            for review in review_instances:
                if review.place_id == self.id:
                    reviews.append(review)

            return reviews
