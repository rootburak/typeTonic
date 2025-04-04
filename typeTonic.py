import json
import re

class Type:
    def __init__(self):
        pass 
    
    def Change(self,name,value):
        self.__dict__[name] = value

    def __setattr__(self, name, value):
        if hasattr(self, name):
            existing_type = type(getattr(self, name))
            if not isinstance(value, existing_type):
                raise TypeError(
                    f"Attribute '{name}' must be of type {existing_type.__name__}. "
                    f"Got {type(value).__name__} instead."
                )
        super().__setattr__(name, value)
    def isEmail(self, value):
        if not isinstance(value, str) or not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValueError(f"is not a valid email address.")
        return True

    def isJson(self, value):
        try:
            json.loads(value)
        except ValueError:
            raise ValueError("is not valid JSON.")
        return True

    def isString(self, value):
        if not isinstance(value, str):
            raise ValueError(f"is not a valid string.")
        return True


var = Type()

