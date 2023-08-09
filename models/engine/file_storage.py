"""
Contains the definition of 'FileStorage' class.
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    Definition of 'FileStorage' class,
    that serializes instances to a JSON file and
    deserializes JSON file to instances.
    """
    __file_path = 'airbnb.json'
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
                    k: BaseModel(**v) for k, v in json.load(file).items()
                }
        except FileNotFoundError:
            pass
