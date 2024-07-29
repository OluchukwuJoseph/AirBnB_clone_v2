#!/usr/bin/python3
""" City Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class represents the cities table"""

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        # DB storage will be used
        __tablename__ = "cities"

        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'))

        state = relationship("State", back_populates="cities")
        places = relationship("Place", back_populates="cities",
                              cascade="all, delete-orphan")
    else:
        # File storage will be used
        name = ""
        state_id = ""
