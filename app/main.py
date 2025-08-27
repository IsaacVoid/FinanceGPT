from fastapi import FastAPI
from app.routers import usuarios

app = FastAPI()
app.include_router(usuarios.router)
