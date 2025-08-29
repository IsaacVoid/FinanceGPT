from fastapi import APIRouter
from pydantic import BaseModel # Define modelo de datos usando pydantic
from typing import Optional


router = APIRouter()
# Definir el esquema de usuarios
class Usuario(BaseModel):
    nombre: str
    email: str
    edad: int
    direccion: str
    telefono: str
    nacionalidad: str

# Definiciòn de enpoint POST
@router.post("/usuarios") # Define endpoint que responde a solicitudes POST en la ruta /usuarios
# usuario: Usuario -> indica que el request body debe coincidir con la estrucutura del modelo usuario
async def crear_usuario(usuario: Usuario):
    return{
        "mensaje":"Usuario creado exitosamente",
        "datos": {
            "nombre": usuario.nombre,
            "email": usuario.email,
            "edad": usuario.edad,
            "direccion": usuario.direccion,
            "telefono": usuario.telefono,
            "nacionalidad": usuario.nacionalidad
        }
    }

@router.get("/usuarios")
async def listar_usuarios(nombre: Optional[str] = None): # Se recomienda que nombre sea opcional
    if nombre:
        return {
            "mensaje": f"Usuario {nombre} encontrado",
            "datos": {
                "nombre": nombre,
                "email": f"{nombre}@example.com",
                "edad": 25,
                "direccion": "Calle Principal",
                "telefono": "1234567890",
                "nacionalidad": "MX"
            }
        }
    else:
        return{
            "mensaje": "No se encontraron usuarios"
        }

@router.delete("/usuarios")
async def eliminar_usuarios(nombre:str):
    if nombre:
        return {"mensaje": f"Usuario {nombre} modificado exitosamente"}
