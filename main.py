from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Greeting(BaseModel):
    msg: str


app = FastAPI(title="Fast Api Hello World", version="1.0.0")


@app.get("/hello", response_model=Greeting, tags=["greetings"])
async def hello(name)->Greeting:
    """Hello."""
    return {"msg": f'Hello {name}'}
