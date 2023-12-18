# Typing
from typing import Optional
# Pydantic
from pydantic import BaseModel

class Productos(BaseModel):
    
    id: Optional[str] = None
    name: str
    precio_compra: float
    precio_venta: float
    provedor: str

    