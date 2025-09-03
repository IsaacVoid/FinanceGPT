from fastapi import APIRouter
from app.schemas.users import usuario


router = APIRouter()


@router.post("/users")
async def crear_usuario(usuario: usuario):
    return{
        "message": "User created succesfully",
        "data":{
            "name": usuario.user_name,
            "user_number": usuario.user_number,
            "email": usuario.email,
            "age": usuario.age,
            "register_date": usuario.register_date,
            "address": usuario.address,
            "postal_code": usuario.postal_code,
            "nationality": usuario.nationality,
            "civil_state": usuario.civil_state
        }
    }
