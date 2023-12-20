# UUID
from uuid import uuid4 as uuid
# FastAPi
from fastapi import FastAPI, HTTPException
# Models
from models.productos import Productos

app = FastAPI()

productos =[]

@app.get('/')
def index():
    return {
        'mensaje': 'Bienvendios a la API de Productos'
    }


@app.get('/producto')
def obterner_productos():
    return productos


@app.post('/producto')
def crear_producto(producto: Productos):
    producto.id = str(uuid())
    productos.append(producto)
    return{
        'mensaje': 'Producto creado correctamente'
    }


@app.get('/producto/{producto_id}')
def obterner_productos_ir(producto_id: str):
    
    """ Iteramos en bucles for """
    #  for p in productos:
        #  if p.id == producto_id:
            #  return p 
        # return{
        # 'mensaje': f'EL producto con el ID {producto_id} no fue encotnrado'
    # }

    """ Utilizamos filder """
    resultado = list(filter(lambda p: p.id == producto_id, productos))    
    
    if len(resultado):
        return resultado[0]
    
    raise HTTPException(status_code=404, detail=f'El producto id = {producto_id} no fue encontrado')