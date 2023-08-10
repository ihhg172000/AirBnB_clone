"""
Contains the definition of 'FileStorage' class.
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Definition of 'FileStorage' class.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        FileStorage.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(
                {k: v.to_dict() for k, v in FileStorage.__objects.items()},
                file
            )

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path).
        """
        try:
            with open(FileStorage.__file_path) as file:
                FileStorage.__objects = {
                    k: eval(f"{v['__class__']}(**{v})")
                    for k, v in json.load(file).items()
                }
        except FileNotFoundError:
            pass
