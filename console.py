#!/usr/bin/python3
"""Console entry point for the AirBnB clone project."""

import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project."""
    prompt = "(hbnb) "
    
    __classes = {
        "BaseModel": BaseModel
    }

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel."""
        if not arg:
            print("** class name missing **")
            return
        
        if arg not in self.__classes:
            print("** class doesn't exist **")
            return
        
        new_instance = self.__classes[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Print string representation of an instance."""
        args = arg.split()
        
        if not args:
            print("** class name missing **")
            return
        
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        key = f"{args[0]}.{args[1]}"
        all_objects = models.storage.all()
        
        if key not in all_objects:
            print("** no instance found **")
            return
        
        print(all_objects[key])

    def do_destroy(self, arg):
        """Delete an instance based on class name and id."""
        args = arg.split()
        
        if not args:
            print("** class name missing **")
            return
        
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        key = f"{args[0]}.{args[1]}"
        all_objects = models.storage.all()
        
        if key not in all_objects:
            print("** no instance found **")
            return
        
        del all_objects[key]
        models.storage.save()

    def do_all(self, arg):
        """Print all string representations of instances."""
        all_objects = models.storage.all()
        
        if not arg:
            print([str(obj) for obj in all_objects.values()])
            return
        
        if arg not in self.__classes:
            print("** class doesn't exist **")
            return
        
        filtered_objects = [str(obj) for key, obj in all_objects.items() 
                           if key.startswith(arg + ".")]
        print(filtered_objects)

    def do_update(self, arg):
        """Update an instance based on class name and id."""
        args = arg.split()
        
        if not args:
            print("** class name missing **")
            return
        
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        key = f"{args[0]}.{args[1]}"
        all_objects = models.storage.all()
        
        if key not in all_objects:
            print("** no instance found **")
            return
        
        if len(args) < 3:
            print("** attribute name missing **")
            return
        
        if len(args) < 4:
            print("** value missing **")
            return
        
        obj = all_objects[key]
        attr_name = args[2]
        attr_value = args[3]
        
        # Remove quotes if present
        if attr_value.startswith('"') and attr_value.endswith('"'):
            attr_value = attr_value[1:-1]
        
        # Convert value to appropriate type
        if hasattr(obj, attr_name):
            current_attr = getattr(obj, attr_name)
            if isinstance(current_attr, int):
                attr_value = int(attr_value)
            elif isinstance(current_attr, float):
                attr_value = float(attr_value)
        else:
            # Try to convert to int or float, otherwise keep as string
            try:
                attr_value = int(attr_value)
            except ValueError:
                try:
                    attr_value = float(attr_value)
                except ValueError:
                    pass  # Keep as string
        
        setattr(obj, attr_name, attr_value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
