from pydantic import BaseModel, Field
from datetime import date

from pydantic.networks import EmailStr

class usuario(BaseModel):
    id: int
    user_number: str = Field(max_length=7)
    user_name: str = Field(min_length=2, max_length=50, description="Nombre de usuario")
    email: EmailStr = Field( max_length=60)
    is_active: bool = True # activo
    age: int = Field(gt=18) # birth_date : date
    register_date: date
    address: str = Field(min_length=10,max_length=60, description="Direcciòn")
    postal_code: int
    nationality : str
    civil_state : str
