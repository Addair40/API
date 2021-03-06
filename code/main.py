from fastapi import FastAPI
import sqlite3
from typing import List
from pydantic import BaseModel

class Respuesta(BaseModel):
    message: str


class Cliente(BaseModel):
    id_cliente: int
    nombre: str
    email: str

app = FastAPI()


@app.get("/", response_model=Respuesta)
def index():
    return {"message": "Hello World"}

@app.get("/clientes/", response_model=List[Cliente])
async def clientes():
    with sqlite3.connect('sql/clientes.sqlite')as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM clientes")
        response = cursor.fetchall()
        return response
        

@app.get("/clientes/{id_cliente}", response_model=Cliente)
async def clientes():
    with sqlite3.connect('sql/clientes.sqlite')as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM clientes")
        response = cursor.fetchone()
        return response
        
