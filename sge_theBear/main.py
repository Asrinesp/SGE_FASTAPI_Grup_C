from typing import list
from fastapi import FastAPI
from services import read

app = FastAPI()

@app.get(path="/root", responses_model=List[dict])
async def read_root():
    result = read.registre()
    return result