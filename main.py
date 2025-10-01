from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def head_root():
    return("Bem vindo!")