
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name = 'Jane Doe'


user = User(id='123')
assert user.id == 123
assert user.name == 'Jane Doe'
assert user.__fields_set__ == {'id'}
