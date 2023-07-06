#!/usr/bin/python3
"""for later"""
import json
import os
from models.base_model import BaseModel



class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "objects.json"
    __objects = {}
    class_dict = {"BaseModel": BaseModel}
    
    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        
        """
        if FileStorage.__objects is not None:
            objs_to_dump = {}
            for k, v in FileStorage.__objects.items():
                objs_to_dump[k] = v.to_dict()
            with open(FileStorage.__file_path, "w") as f:
                json.dump(objs_to_dump, f)

    def reload(self):
        """

        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                new_obj = json.load(f)
            for k, v in new_obj.items():
                obj = FileStorage.class_dict[v["__class__"]](**v)
                FileStorage.__objects[k] = obj
