#!/usr/bin/python3
"""Defines the BaseModel class"""
import models
import uuid
from datetime import datetime


class BaseModel:

    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        """.."""
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
        """.."""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """.."""
        self.iso_created = self.created_at.isoformat()
        self.iso_updated = self.updated_at.isoformat()
        object_dicit = self.__dict__.copy()
        object_dicit["__class__"] = self.__class__.__name__
        object_dicit["created_at"] = self.iso_created
        object_dicit["updated_at"] = self.iso_updated

    def __str__(self):
        """.."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
