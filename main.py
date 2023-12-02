from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

# Create app
app = FastAPI()

class Item(BaseModel):
    """ Methodo PUT """
    name: str 
    price: float
    is_offer: Union[bool, None] = None



@app.get('/')
def read_root():
    """ Prueba Hello Word """
    return {
        'Hello': 'World',
        }


@app.get('/hola')
def hola_mundo():
    """ Prueba hola mundo """
    return {
        'Hola': 'Mundo'
        }


@app.get('/items/{item_id}')
def read_item(item_id: int, q: Union[str, None] = None):
    """ Parametro por path / y query ?, & """
    return {
        # Parametro de consulta
        'irtem_id': item_id,
        'q': q
        }


@app.get('/calculadora')
def calculadora(operador_1: float, operandor_2: float):
    """ Query params """
    return {
        'suma': operador_1 + operandor_2
        }

