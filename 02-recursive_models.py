from typing import List
from pydantic import BaseModel

class Foo(BaseModel):
    count: int
    size: float = None

class Bar(BaseModel):
    apple = 'x'
    banana = 'y'

class Spam(BaseModel):
    foo: Foo
    bars: List[Bar]

s = Spam(
    foo = {'count':4},
    bars = [{'apple' : 'x1'},{'apple' : 'x2'}]
)

# print(s)

''' Retorna un diccionario de los campos y valores del modelo.'''
print(s.dict())
"""
{
    'foo': {'count': 4, 'size': None},
    'bars': [
        {'apple': 'x1', 'banana': 'y'},
        {'apple': 'x2', 'banana': 'y'},
    ],
}
"""
