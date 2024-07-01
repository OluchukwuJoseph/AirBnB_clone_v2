#!/usr/bin/python3
"""This module defines a class User"""
import os
import sys
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if os.getenv('HBNB_TYPE_STORAGE') == 'file':
        # File storage will be used
        first_name = ''
        last_name = ''
        email = ''
        password = ''
    elif os.getenv('HBNB_TYPE_STORAGE') == 'db':
        # DB storage will be used
        __tablename__ = 'users'

        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
    else:
        # If not Storage Type was specified return error
        sys.stderr.write('Unkwown FILE_TYPE_STORAGE\n')
        sys.exit(1)
