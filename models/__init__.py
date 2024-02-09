#!/usr/bin/python3
"""__init__ magic method for models directory"""
from models.engine.file_storge import FileStorage


storage = FileStorage()
storage.reload()
