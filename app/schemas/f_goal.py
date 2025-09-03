from pydantic import BaseModel, Field
from datetime import date
from typing import List


class financial_goal(BaseModel):
    id: int
    description: str = Field(max_length=300, description="Descripción de tu meta")
    amount: int = Field(description="Cantidad a alcanzar")
    creation_date: date
    completition_date: date
    # time_to_complete: int # En meses
    steps_to_take: List[str] = []
