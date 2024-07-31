#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', ForeignKey('places.id'),
                                 primary_key=True),
                          Column('amenity_id', ForeignKey('amenities.id'),
                                 primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        # DB storage will be used
        __tablename__ = 'places'

        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)

        # cities = relationship('City', backref='places')
        # user = relationship('User', back_populates='places')
        reviews = relationship('Review', back_populates='place',
                               cascade='all, delete-orphan')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")
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

        @property
        def amenities(self):
            """
                Returns the list of Amenity instances associated with Place.
                It will be the FileStorage relationship between Place & Amenity
            """
            return Place.amenity_ids

        @amenities.setter
        def amenities(self, amenity_obj):
            """
                Adds an Amenity to a list of amenities that belongs to a Place.
                It will be the FileStorage relationship between Place & Review
            """
            Place.amenity_ids.append(amenity_obj.id)
