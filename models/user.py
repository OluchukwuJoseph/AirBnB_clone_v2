#!/usr/bin/python3
"""This module defines a class User"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        # DB storage will be used
        __tablename__ = 'users'

        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        email = Column(String(128), nullable=False, default="")
        password = Column(String(128), nullable=False, default="")

        places = relationship('Place', back_populates='user',
                              cascade='all, delete-orphan')

    else:
        # File storage will be used
        first_name = ''
        last_name = ''
        email = ''
        password = ''
