#!/usr/bin/python3

def do_create(self, arg):
    """Creates a new instance with given parameters"""
    try:
        if not arg:
            print("** class name missing **")
            return
        
        args = arg.split(" ")
        class_name = args[0]
        
        if class_name not in HBNBCommand.cal:
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
        obj = HBNBCommand.cal[class_name](**params)
        print("Instance created with ID:", obj.id)
        obj.save()
        
    except Exception as e:
        print("Error:", e)

