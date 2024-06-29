#!/usr/bin/python3
""" City Module for HBNB project """
import os
import sys
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class represents the cities table"""

    # File storage will be used
    if os.getenv('HBNB_TYPE_STORAGE') == 'file':
        name = ""
        state_id = ""
    # DB storage will be used
    elif os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "cities"

        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'))

        state = relationship("State", back_populates="cities")
    # If not Storage Type was specified return error
    else:
        sys.stderr.write('Unkwown FILE_TYPE_STORAGE\n')
        sys.exit(1)
