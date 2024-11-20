from fastapi import FastAPI
from .routers import creating, health

app = FastAPI()
app.include_router(creating.router)
app.include_router(health.router)
