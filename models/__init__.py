#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity


if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
