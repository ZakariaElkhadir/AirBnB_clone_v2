#!/usr/bin/python3
"""class model"""
import json
import os.path
from models.base_model import BaseModel


class FileStorage:
    """_summary_

    Returns:
        _type_: _description_
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """all returns the dictionary __objects"""
        if cls is not None:
            objs = {}
            for key, value in FileStorage.__objects.items():
                if eval(key.split('.')[0] == cls):
                    objs[key] == value
            return objs
        return FileStorage.__objects

    def new(self, obj):
        """new: sets in __object the obj with key class_name id"""
        id = obj.to_dict()["id"]
        class_name = obj.to_dict()["__class__"]
        key_name = class_name + "." + id
        FileStorage.__objects[key_name] = obj

    def save(self):
        """save - serializes __objects to the JSON file"""
        path = FileStorage.__file_path
        data = dict(FileStorage.__objects)
        for key, value in data.items():
            data[key] = value.to_dict()
        with open(path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        """reload method"""
        filepath = FileStorage.__file_path
        data = FileStorage.__objects
        if os.path.exists(filepath):
            try:
                with open(filepath) as file:
                    for key, value in json.load(file).items():
                        if "BaseModel" in key:
                            data[key] = BaseModel(**value)
                        if "User" in key:
                            data[key] = User(**value)
                        if "Place" in key:
                            data[key] = Place(**value)
                        if "State" in key:
                            data[key] = State(**value)
                        if "City" in key:
                            data[key] = City(**value)
                        if "Amenity" in key:
                            data[key] = Amenity(**value)
                        if "Review" in key:
                            data[key] = Review(**value)
            except Exception:
                pass
    
    def delete(self, obj=None):
        """
        delete an object of the class
        """
        if obj is not None:
            key = (f"{obj.__class__.__name__}.{obj.id}")
            if key in self.__objects:
                del self.__objects[key]
                self.save()

