from pydantic import BaseModel, Field, ValidationError
from typing import Optional

"""
To declare a field as required, you may declare it using just an annotation,
or you may use an ellipsis (...) as the value.
"""

class Model(BaseModel):
    a: int
    b: int = ...
    c: int = Field(...)


try:
    Model(a=1, b=2)
except ValidationError as e:
    print(e)

    """
    1 validation error for Model
    c
    field required (type=value_error.missing)
    """
