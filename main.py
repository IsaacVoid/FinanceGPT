from fastapi import FastAPI
from app.routers import usuarios, users

app = FastAPI()
app.include_router(usuarios.router)
app.include_router(users.router)
