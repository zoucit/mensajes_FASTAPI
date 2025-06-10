from typing import Optional, List
from pydantic import BaseModel, EmailStr
from fastapi import FastAPI, HTTPException

#Definimos un modelo de datos
class Mensaje(BaseModel):
    id: Optional[int] = None
    user: str
    mensaje: str

#Inicializamos FastAPI
app = FastAPI()

#Base de datos simulada

mensajes_db = []

# Creamos Mensaje
@app.post("/mensajes", response_model=Mensaje)
def crear_mensaje(mensaje:Mensaje):
    mensaje.id = len(mensajes_db) + 1
    mensajes_db.append(mensaje)
    return mensaje

#Obtener Mensaje por ID
@app.get("/mensaje/{mensaje_id}", response_model=Mensaje)
def obtener_mensaje(mensaje_id: int):
    for mensaje in mensajes_db:
        if mensaje.id == mensaje_id:
            return mensaje
    raise HTTPException(status_code=404, detail="Mensaje NO encontrado")


