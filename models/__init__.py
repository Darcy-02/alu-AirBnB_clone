#!/usr/bin/python3
"""Initialize the models package"""

from models.engine.file_storage import FileStorage

# Create a unique FileStorage instance for the app
storage = FileStorage()

# Load objects from JSON file (if it exists)
storage.reload()
