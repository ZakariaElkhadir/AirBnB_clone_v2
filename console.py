#!/usr/bin/python3

import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

""" dict to tests """
HBNBCommand = {
    'BaseModel': BaseModel,
    'User': User,
    'Place': Place,
    'City': City,
    'Amenity': Amenity,
    'State': State,
    'Review': Review
}

def do_create(arg):
    """Creates a new instance with given parameters"""
    try:
        if not arg:
            print("** class name missing **")
            return
        
        args = arg.split(" ")
        class_name = args[0]
        
        if class_name not in HBNBCommand:
            print("** class doesn't exist **")
            return
        
        """ Extract parameters from the command line arguments """
        params = {}
        for arg in args[1:]:
            key, value = arg.split("=")
            """ Process the value based on its type """
            if value.startswith('"') and value.endswith('"'):
                """ String value """
                value = value[1:-1].replace('\\"', '"').replace('_', ' ')
            elif '.' in value:
                """ Float value """
                value = float(value)
            else:
                """ Integer value """
                value = int(value)
            params[key.replace('_', ' ')] = value
        
        """ Create an instance of the specified class with the provided parameters """
        obj = HBNBCommand[class_name](**params)
        print("Instance created with ID:", obj.id)
        obj.save()
        
    except Exception as e:
        print("Error:", e)

""" Read commands from standard input"""
for line in sys.stdin:
    do_create(line.strip())

