from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def index():
    return {
        'mensaje': 'Bienvendios a la API de Productos'
    }