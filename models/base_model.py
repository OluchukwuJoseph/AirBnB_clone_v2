#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import os
import sys
import uuid
from datetime import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime


# Determine Storage type and declare Base
if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    Base = declarative_base()
elif os.getenv('HBNB_TYPE_STORAGE') == 'file':
    Base = object
else:
    sys.stderr.write('Unkwown FILE_TYPE_STORAGE\n')
    sys.exit(1)


class BaseModel:
    """A base class for all hbnb models"""
    # Define Table Columns
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False,
                        default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False,
                        default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""

        # No kwargs
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.save()
        # If kwargs got its values from the directly command line
        elif 'id' not in kwargs.keys() and 'created_at' not in kwargs.keys()\
                and 'updated_at' not in kwargs.keys():
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.__dict__.update(kwargs)
            self.save()
        # If kwargs did not get its arguments from the Command Line
        else:
            date_format = "%Y-%m-%dT%H:%M:%S.%f"
            kwargs['created_at'] = datetime.\
                strptime(kwargs['created_at'], date_format)
            kwargs['updated_at'] = datetime.\
                strptime(kwargs['updated_at'], date_format)

            if '__class__' in kwargs.keys():
                del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        if '_sa_instance_state' in dictionary.keys():
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """Delete instance from storage dictionary"""
        from models import storage
        storage.delete(self)
