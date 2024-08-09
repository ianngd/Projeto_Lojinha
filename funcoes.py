from classes import *
from previwer import *
import getpass
import time
import os

lista_carrinho=[]
lista_produtos=[]
lista_usuario=[]


def listar_produstos_admin(produtos):
    for i in range(len(produtos)):
        print(f"| {i + 1} | {produtos[i].nome} | {produtos[i].quantidade} | R$ {produtos[i].preco}    |")
    pressione_enter()

def pressione_enter():
    input("Pressione enter para Continuar....")
    limpar_tela()

def limpar_tela():
    os.system("cls")

def criar_usuario_novo(lista_usuario):
    _nome = input("Digite o Login: ")
    _idade= input("Digite sua Idade: ")
    _cpf= input("Digite seu CPF: ")
    _telefone=input("Digite seu Telefone: ")
    _senha = getpass.getpass("Digite a senha: ")
    _comfirme_senha = getpass.getpass("Comfirme a Senha: ")
    if _senha == _comfirme_senha:
        print("Usuário Criado com Sucesso!!")
        usuario = Cliente( nome = _nome, senha = _senha, cpf = _cpf, telefone = _telefone, idade = _idade )
        pressione_enter()
        lista_usuario.append(usuario)
    else:
        print("Senha não é igual")
        return False


def adicionar_produto(lista_produtos):
    _nome = input("Digite o Nome do Produto: ")
    _preco = float(input("Digite o Preco do Produto: "))
    _quantidade = input("Digite a Quantidade do Produto: ")
    _produto = Produto(nome = _nome, preco = _preco, quantidade = _quantidade)
    lista_produtos.append(_produto)
    pressione_enter()
    print("Produto Adicionado com Sucesso!!")

def logar_admin():
    _login = input("Digite o Login: ")
    _senha = getpass.getpass("Digite a Senha: ")
    if _login == "admin" and _senha == "admin123":
        print("Login com Sucesso!!")
        return True 
    else:
        print("Login Inválido!!")
        return False       

def painel_adimin():
    op = int(input("[OPÇÃO]-> "))
    if op == 1:
        limpar_tela()
        listar_produstos_admin(lista_produtos)
        limpar_tela()
    
    elif op == 2:
        limpar_tela()
        adicionar_produto(lista_produtos)
        limpar_tela()
    elif op == 3:
        pass

    elif op == 4:
        listar_usuarios_do_sistema(lista_usuario)
    
    elif op == 0:
        print("Saindo do Sistema!!")
        pass