from pydantic import BaseModel, Field
from datetime import date
from typing import List

class investment_request(BaseModel):
    id: int
    user_id: str = Field(max_length=7)
    creation_date : date
    business_description : str = Field(max_length=300)
    market_analysis: str # Debe cambiarse para subir archivos
    profit_strategy: str
    financial_statements: List[str] = []
    investment_amount: int
    ivestment_usage: str = Field(max_length=300)
