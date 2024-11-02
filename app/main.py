from fastapi import FastAPI
from .routers import creating

app = FastAPI()
app.include_router(creating.router)
