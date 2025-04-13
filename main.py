from fastapi import FastAPI
from models import task 

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}