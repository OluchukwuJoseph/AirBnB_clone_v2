#!/usr/bin/python3
"""This module defines a class to manage DB storage for hbnb clone"""
import os
from sqlalchemy import create_engine
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review


class DBStorage:
    """This class manages storage of hbnb models in DB format"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the Instance"""
        DB_USER = os.getenv('HBNB_MYSQL_USER')
        DB_PWD = os.getenv('HBNB_MYSQL_PWD')
        HOST = os.getenv('HBNB_MYSQL_HOST')
        DB = os.getenv('HBNB_MYSQL_DB')

        DBStorage.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                           .format(DB_USER, DB_PWD, HOST, DB),
                                           pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            from sqlalchemy import MetaData
            # Create MetaData object
            meta = MetaData(bind=DBStorage.__engine)
            # Reflect database schema into MetaData object
            meta.reflect()
            # Drop all tables in the database
            meta.drop_all()

    def all(self, cls=None):
        """Return all objects depending of the class name"""
        dictionary = {}
        classes = [User, Place, State, City, Amenity, Review]

        if cls is None:
            # Retrieve and add all objects to dictionary
            for model_class in classes:
                all_items = DBStorage.__session.query(model_class).all()
                for item in all_items:
                    key = f"{item.__class__.__name__}.{item.id}"
                    dictionary.update({key: item})

            return dictionary
        else:
            if cls in classes:
                all_items = DBStorage.__session.query(cls).all()
            for item in all_items:
                key = f"{item.__class__.__name__}.{item.id}"
                dictionary.update({key: item})
            return dictionary

    def new(self, obj):
        """Add the object to the current database session"""
        DBStorage.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        DBStorage.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj is not None:
            DBStorage.delete(obj)

    def reload(self):
        """Creates all tables in the database and start a session"""
        from models.base_model import Base
        from sqlalchemy.orm import sessionmaker, scoped_session

        # Create tables
        Base.metadata.create_all(DBStorage.__engine)

        # Create session
        Session = sessionmaker(bind=DBStorage.__engine, expire_on_commit=False)
        DBStorage.__session = scoped_session(Session)

    def close(self):
        """Forcefully reload Sessions"""
        DBStorage.__session.remove()
