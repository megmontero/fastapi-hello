from fastapi import FastAPI, HTTPException
from pydantic import BaseModel



# 1. Leer la versión desde el archivo
try:
    with open("version.txt", "r", encoding="utf-8") as f:
        VERSION = f.read().strip()
except FileNotFoundError:
    VERSION = "1.0.0"  # Versión por defecto si el archivo no existe



class Greeting(BaseModel):
    msg: str


app = FastAPI(title="Fast Api Hello World", version=VERSION)


@app.get("/hello", response_model=Greeting, tags=["greetings"])
async def hello(name)->Greeting:
    """Hello."""
    return {"msg": f'Hi {name}! We are using jenkins from v{VERSION}.'}
