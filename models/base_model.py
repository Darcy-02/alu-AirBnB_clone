#!/usr/bin/python3
"""BaseModel module"""

import uuid
from datetime import datetime

class BaseModel:
    """Base class for all models in the AirBnB clone"""

    def __init__(self):
        """Initialize a new BaseModel instance"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
