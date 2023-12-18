# Python
from datetime import datetime
# Pydantic
from pydantic import BaseModel

class User(BaseModel):
    id : int
    name : str = 'Agustin Ribotta'
    signup_ts : datetime | None = None
    friends : list[int] = []

# Data de exterior 
external_data = {
    'id': 1,
    'signup_ts': '2022-10-23 12:20',
    'friends': [1,2,3,4]
}

user = User(**external_data)

print(user)
print(user.id)