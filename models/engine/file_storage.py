from json import dump, load
from models.base_model import BaseModel
from models.user import User
from models.state import State


class FileStorage:

    __file_path = "banana.json"
    __objects = {}

    def all(self):
        """Returns a dictionary representation of a objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Saves in the dictionary the value with the object"""
        key = ("{}.{}".format(obj.__class__.__name__, str(obj.id)))
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves in a file the value of the dictionary"""
        dic_copy = {}

        for key, value in FileStorage.__objects.items():
            dic_copy[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            dump(dic_copy, f)

    def reload(self):
        """This function loads every dictionary representation of the object"""
        Class_type = {'BaseModel': BaseModel, 'User': User,
                      'State': State}
        try:
            with open(FileStorage.__file_path, 'r') as f:
                Loaded_file = load(f)
                for key in Loaded_file.keys():
                    for Class, instance in Class_type.items():
                        if Loaded_file[key]['__class__'] == Class:
                            FileStorage.__objects[key] = (
                                (instance)(**Loaded_file[key]))
        except:
            pass
