#!/usr/bin/python3
"""Defines the BaseModel class"""
import models
import uuid
from datetime import datetime


class BaseModel:

    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel"""
        t_form = '%Y-%m-%dT%H:%M:%S.%f'
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        if kwargs:
            for i, j in kwargs.items():
                if i == "created_at" or i == "updated_at":
                    self.__dict__[i] = datetime.strptime(j, t_form)
                else:
                    self.__dict__[i] = j
        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime"""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """dictionary of the BaseModel"""
        self.iso_c = self.created_at.isoformat()
        self.iso_u = self.updated_at.isoformat()
        obj_dic = self.__dict__.copy()
        obj_dic["__class__"] = self.__class__.__name__
        obj_dic["created_at"] = self.iso_c
        obj_dic["updated_at"] = self.iso_u

    def __str__(self):
        """Return the str of the BaseModel"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
