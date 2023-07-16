#!/usr/bin/python3
import json

"""This is the base class"""


class Base:
    """defines the super(base) class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file:

        Args:
        list_objs is a list of instances who inherits of Base
        If list_objs is None, save an empty list
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            json.dump([obj.to_dictionary() for obj in list_objs], file)

    @staticmethod
    def from_json_string(json_string):
        """desirializes json string to python object"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set:"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # this creates a temporary instance
        else:  # for the square
            dummy = cls(1)
        dummy.update(**dictionary)  # updates dummy attributes with dict values
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """returns a list of instances
        Try and except handles cases where the file doesnt exist
        """
        try:
            with open(cls.__name__ + ".json", "r") as file:
                list = cls.from_json_string(file.read())
                return [cls.create(**dic) for dic in list]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves a list of objects to a CSV file"""
        filename = cls.__name__ + ".csv"  # creates a filename for the CSV file
        with open(filename, "w", newline="") as file:
            if list_objs is None or list_objs == []:
                file.write("[]")  # Return an empty list
            else:
                if cls.__name__ == "Rectangle":
                    # assign fieldnames depending on the object
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]

                # write dictionaries to the CSV file
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                for obj in list_objs:
                    # converts the object to a dictionary
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """reads data from a CSV file and
        returns a list of instantiated classes
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as file:
                if cls.__name__ == "Rectangle":
                    # Depending on the class name, different fieldnames
                    #  will be used for reading data from the CSV file
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                # reads data from the CSV file
                list = csv.DictReader(file, fieldnames=fieldnames)

                # convert the read dictionaries into a list of dictionaries
                list = [dict([k, int(v)] for k, v in d.items())
                        for d in list]
                return [cls.create(**d) for d in list]
        except IOError:
            return []
