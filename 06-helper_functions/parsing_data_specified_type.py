from typing import List

from pydantic import BaseModel, parse_obj_as


class Item(BaseModel):
    id: int
    name: str


# `item_data` could come from an API call, eg., via something like:
# item_data = requests.get('https://my-api.com/items').json()
item_data = [{'id': 1, 'name': 'My Item'}]


"""
This function behaves similarly to BaseModel.parse_obj, but works with arbitrary pydantic-compatible types.
"""
items = parse_obj_as(List[Item], item_data)
print(items)
# [Item(id=1, name='My Item')]
