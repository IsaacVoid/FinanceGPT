from pydantic import BaseModel, Field
from typing import List


class porfolio_analysis(BaseModel):
    id: int
    primal_objective: str = Field(max_length=50)
    investment_horizon: str = Field(max_length=50)
    current_actives: List[str] = []
