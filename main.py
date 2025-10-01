#criar uma api que retorne uma mensagem de boas vindas

from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def head_root():
    return("Bem vindo!")
