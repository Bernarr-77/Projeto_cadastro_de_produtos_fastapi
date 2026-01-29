# python -m fastapi dev .\cadastro_produtos\main.py

from fastapi import FastAPI
from pydantic import BaseModel
from itertools import count

class ProdutoInput(BaseModel):
    nome: str
    quantidade: int
    valor: float

class Produtos(ProdutoInput):
    id: int

lista_produtos = []

contador_id = count(1)

app = FastAPI()

@app.get("/produtos")
def buscar_produtos():
    return lista_produtos

@app.post("/produtos/")
def adicionar_produtos(Produto: ProdutoInput):
    novo_produto = Produtos(
        id= next(contador_id),
        nome=Produto.nome,
        quantidade= Produto.quantidade,
        valor= Produto.valor
        )
    lista_produtos.append(novo_produto)
    return novo_produto
