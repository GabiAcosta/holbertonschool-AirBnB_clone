#!/usr/bin/python3
"""for later"""
import json
import os



class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "objects.json"
    __objects = {}
    
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
            json_string = json.dumps(FileStorage.__objects)
            with open(FileStorage.__file_path, "w") as f:
                f.write(json_string)

    def reload(self):
        """

        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = json.loads(f.read())
