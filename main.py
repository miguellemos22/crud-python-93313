#banco de dados
#SQlite

#sql = linguagem de consulta estruturada

# SELECT * FROM CLIENTES
#puxa dados ex: nome,sobrenome,idade, etc...


import os 
from sqlalchemy import create_engine, column, Strinh, integer
from sqlalchemy.orm import sessionmaker, declarative_base

#criando banco de dados

db = create_engine("sqlite:///meubanco.db")

#orm
#CREATE DATABASE meubanco;

#criando conexão com o banco de dados.
session = sessionmaker(bind=db)
session = session()

#I / O
#I = input (entrada)
#O = output (saida)

#computação na nuvem

#criando tabela
Base = declarative_base()
class Usuario(Base):
    __tablename__ = "usuarios"

#definindo campos da tabela
    id = column("id", integer, primary_key=True, autoincrement= True)
    nome = column("nome, string")
    email = column("email, string")
    senha = column("senha, string")

#definindo atributos da classe
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha

#criando tabela no banco de dados
Base.metadata.create_all(bind=db)

#salvar no banco de dados
print("solicitando dados para o usuario")
Usuario = Usuario("Marta", "marta@gmail.com", "123")
session.add(Usuario)
session.commit()

Usuario = Usuario(nome="Maria", email="maria@gmail.com", senha="456")
session.add(Usuario)
session.commit()

#listando todos os usuarios no banco de dados
print("\nExibindo todos os usuarios do banco de dados.")
lista_usuarios = session.query(Usuario).all()

for usuario in lista_usuarios:
    print(f"{usuario.id} - {usuario.nome} - {usuario.senha}")

#fechando conexão
session.close()