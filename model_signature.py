import inspect
from pydantic import BaseModel, Field


class FooModel(BaseModel):
    id: int
    name: str = None
    description: str = 'Foo'
    apple: int = Field(..., alias='pear')


""" All pydantic models will have their signature generated based on their fields """
print(inspect.signature(FooModel))
# (*, id: int, name: str = None, description: str = 'Foo', pear: int) -> None
