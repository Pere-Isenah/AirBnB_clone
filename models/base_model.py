#!/usr/bin/python3
"""
This module defines the BaseModel class, which provides common attributes
and methods for all models.
"""

from datetime import datetime
import uuid


class BaseModel():
    """
    The base model class provides common attributes and methods for all models.

    Attributes:
        id (str): A unique identifier for the model instance.
        create_at (datetime): The datetime when the model instance was created.
        updated_at (datetime): The datetime when the model instance
        was last updated.
    """

    def __init__(self):
        """
        Constructor method that initializes the id, create_at,
        and updated_at attributes.
        """
        self.id = str(uuid.uuid4())
        self.create_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the object with the class name,
        id, and attributes.
        """
        return f"[{self.__class__.__name__}],({self.id}),{self.__dict__}"

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the object with the class name,
        create_at, and updated_at attributes.

        Returns:
            dict: A dictionary representation of the object.
        """
        dict_copy = self.__dict__.copy()
        dict_copy.update({"__class__": self.__class__.__name__})
        dict_copy.update({"create_at": self.create_at.isoformat()})
        dict_copy.update({"updated_at": self.updated_at.isoformat()})

        return dict_copy
