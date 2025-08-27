from fastapi import APIRouter
from pydantic import BaseModel # Define modelo de datos usando pydantic


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
@router.post("/usuarios") # Define enpoitit que responde a solicitudes POST en la ruta /usuarios
# usuario: Usuario -> indica que el reques body debe coincidir con la estrucutura del modelo usuario
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
