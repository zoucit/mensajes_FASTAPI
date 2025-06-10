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
@app.post("/mensajes/", response_model=Mensaje)
def crear_mensaje(mensaje:Mensaje):
    mensaje.id = len(mensajes_db) + 1
    mensajes_db.append(mensaje)
    return mensaje

# Obtener Mensaje por ID
@app.get("/mensajes/{mensaje_id}", response_model=Mensaje)
def obtener_mensaje(mensaje_id: int):
    for mensaje in mensajes_db:
        if mensaje.id == mensaje_id:
            return mensaje
    raise HTTPException(status_code=404, detail="Mensaje NO encontrado")

# Listamos todos los Mensajes
@app.get("/mensajes/", response_model=list[Mensaje])
def listar_mensajes():
    return mensajes_db

# Actualizamos mensajes por ID
@app.put("/mensajes/{mensaje_id}", response_model=Mensaje)
def actualizar_mensaje(mensaje_id: int, mensaje_actualizado: Mensaje):
    for index, mensaje in enumerate (mensajes_db):
        if mensaje.id == mensaje_id:
            mensaje_actualizado.id = mensaje_id
            mensajes_db[index] = mensaje_actualizado
            return mensaje_actualizado
    raise HTTPException(status_code=404, detail="Mensaje NO encontrado para actualizar")

# Borramos mensaje por ID
@app.delete("/mensajes/{mensaje_id}", response_model=dict)
def eliminar_mensaje(mensaje_id: int):
    for index, mensaje in enumerate (mensajes_db):
        if mensaje.id == mensaje_id:
            del mensajes_db[index]
            return{"detail":"Mensaje Eliminado"}
    raise HTTPException(status_code=404, detail="Mensaje NO encontrado para eliminar")



