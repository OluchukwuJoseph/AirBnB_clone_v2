#!/usr/bin/python3
""" State Module for HBNB project """
import os
import sys
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class that represents the states table"""
    # File storage will be used
    if os.getenv('HBNB_TYPE_STORAGE') == 'file':
        name = ""

        @property
        def cities(self):
            """
                Returns the list of City instances with state_id equals to the
                current State.id.
                It will be the FileStorage relationship between State and City
            """
            from models import storage
            from models.city import City
            cities = []
            city_instances = storage.all(City).values()

            for city in city_instances:
                if city.state_id == self.id:
                    cities.append(city)
            return cities

    # DB storage will be used
    elif os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "states"

        name = Column(String(128), nullable=False)

        cities = relationship("City", back_populates="state",
                              cascade="all, delete-orphan")
    # If not Storage Type was specified return error
    else:
        sys.stderr.write('Unkwown FILE_TYPE_STORAGE\n')
        sys.exit(1)
