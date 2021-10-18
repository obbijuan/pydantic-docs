import pickle
from datetime import datetime
from pathlib import Path
from pydantic import BaseModel, ValidationError


"""
Helper Functions
Pydantic provides three classmethod helper functions on models for parsing data
"""


class User(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: datetime = None



"""
parse_obj: this is very similar to the __init__ method of the model, except it takes a dict rather than keyword arguments.
If the object passed is not a dict a ValidationError will be raised.
"""

m = User.parse_obj({'id': 123, 'name': 'James'})
print(m)
# id=123 signup_ts=None name='James'


try:
    User.parse_obj(['not', 'a', 'dict'])
except ValidationError as e:
    print(e)
    """
    1 validation error for User
    __root__
      User expected dict not list (type=type_error)
    """


"""
parse_raw: this takes a str or bytes and parses it as json, then passes the result to parse_obj.
Parsing pickle data is also supported by setting the content_type argument appropriately.
"""

m = User.parse_raw('{"id": 123, "name": "James"}')
print(m)
# id=123 signup_ts=None name='James'


pickle_data = pickle.dumps({
    'id': 123,
    'name': 'James',
    'signup_ts': datetime(2017, 7, 14)
})

m = User.parse_raw(
    pickle_data, content_type='application/pickle', allow_pickle=True
)
print(m)
# id=123 signup_ts=datetime.datetime(2017, 7, 14, 0, 0) name='James'


"""
parse_file: this takes in a file path, reads the file and passes the contents to parse_raw.
If content_type is omitted, it is inferred from the file's extension
"""

path = Path('data.json')
path.write_text('{"id": 123, "name": "James"}')
m = User.parse_file(path)
print(m)
# id=123 signup_ts=None name='James'
