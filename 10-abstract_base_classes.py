import abc
from pydantic import BaseModel

"""
Pydantic models can be used alongside Python's Abstract Base Classes
"""

class FooBarModel(BaseModel, abc.ABC):
    a: str
    b: int

    @abc.abstractmethod
    def my_abstract_method(self):
        pass
