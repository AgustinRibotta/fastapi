# Fast api 
from fastapi import FastAPI
# Tyoing
from typing import Union
# models 
from .models.models import Item

# Create app
app = FastAPI()


#################### GET

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

####################

#################### PUT

@app.put('/item/{item_id}')
def update_item(item_id: int, item: Item):
    """ Update Method PUT """
    # Indicamos que campos queremos devolver 
    return {
        'item_name': item.name, 
        'item_id': item_id
    }