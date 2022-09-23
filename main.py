from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Produto(BaseModel):
	id: Optional[int] = 0
	nome: str
	preco: float
	desc: Optional[str] = None

db_produto ={1: Produto(id=1, nome="Playstation 3", preco=570.00),
	2: Produto(id=2, nome="Linha de pipa 20 metros", preco=15.00),
	3: Produto(id=3, nome="Jogo de facas tramontina", preco=200.00),
	4: Produto(id=4, nome="Bola Jabulani modelo oficial 2010 3", preco=100.00),
	5: Produto(id=5, nome="Ventilador industrial 2m diametro", preco=500.00)}

@app.get("/")
def home():
    	return {"message": "oi"}

@app.get("/produtos/me")
def mostrar_meu_produto():
	return {"produto": "sou um produto"}

@app.get("/produtos/")
def exibir_produtos():
	return {"produtos": db_produto}

@app.get("/produtos/{id}")
def mostrar_produto(id: int):
	produto_selecionado = db_produto[id]
	return {"produto_selecionado": [produto_selecionado]}

@app.post("/produtos/criar-produto")
def criar_produto(produto: Produto):
	produto.id = db_produto[len(db_produto)].id + 1
	db_produto[produto.id] = produto
	return {"status": "criado com sucesso"}

@app.patch("/produtos/atualizar-produto/{id}")
def atualizar_produto(id: int, produto: Produto):
	if(id not in db_produto):
		msg = "produto nao encontrado"
	else:
		db_produto[id].nome = produto.nome
		db_produto[id].preco = produto.preco
		db_produto[id].desc = produto.desc
		msg = "autalizado com sucesso"
	return {"status": msg}

@app.delete("/produtos/remover-produto/{id}")
def remover_produto(id: int):
	if(id not in db_produto):
		msg = "produto nao encontrado"
	else:
		del db_produto[id]
		msg = "removido com sucesso"
	return {"status": msg}

