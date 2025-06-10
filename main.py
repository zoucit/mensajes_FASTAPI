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

