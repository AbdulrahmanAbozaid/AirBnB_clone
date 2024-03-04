""" A module for the base model class """
import uuid
from datetime import datetime


class BaseModel:
    """ Base Model blueprint """
    def __init__(self):
        """ initialiser for BaseModel """
        id = str(uuid.uuid4())
        created_at = datetime.now().isoformat()
        updated_at = datetime.now().isoformat()
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        """ Prints a string representation of the class"""
        return f"{self.__class__.__name__} ({self.id}) {self.__dict__}"

    def save(self):
        """ Updates the updated_at value"""
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        """ Returns a dictionary representation of the class"""
        class_dict = self.__dict__
        class_dict["__class__"] = __class__.__name__
        return class_dict