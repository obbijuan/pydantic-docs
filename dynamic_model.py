from pydantic import BaseModel, create_model

"""
Here StaticFoobarModel and DynamicFoobarModel are identical.
"""

DynamicFoobarModel = create_model('DynamicFoobarModel', foo=(str, ...), bar=123)

class StaticFoobarModel(BaseModel):
    foo: str
    bar: int = 123



class FooModel(BaseModel):
    foo: str
    bar: int = 123


BarModel = create_model(
    'BarModel',
    apple='russet',
    banana='yellow',
    __base__=FooModel,
)

print(BarModel)
# <class 'pydantic.main.BarModel'>
print(BarModel.__fields__.keys())
# dict_keys(['foo', 'bar', 'apple', 'banana'])
