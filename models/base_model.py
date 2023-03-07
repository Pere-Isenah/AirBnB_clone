#!/usr/bin/python3
from datetime import datetime
import uuid

class BaseModel():
    def __init__(self):
        self.id = uuid.uuid4()
        self.create_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}],({self.id}),{self.__dict__}"
    