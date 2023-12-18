# Pydantic
from pydantic import BaseModel
# Tyoing
from typing import Union


class Item(BaseModel):
    """ Methodo PUT """
    name: str
    price: float
    # De esta manera idicamos que es opcional
    is_offer: Union[bool, None] = None