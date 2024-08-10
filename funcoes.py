from classes import *
from previwer import *
import getpass
import time
import os

lista_carrinho=[]
lista_produtos=[]
lista_usuario=[]


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
        massa = True
        return massa
    else:
        print("Login Inválido!!")
        massa = False
        return massa

def painel_adimin():
    op = int(input("[OPÇÃO]-> "))
    if op == 1:
        listar_produtos_admin(lista_produtos, lista_carrinho)
    
    elif op == 2:
        adicionar_produto(lista_produtos)

    elif op == 3:
        pass

    elif op == 4:
        listar_usuarios_do_sistema(lista_usuario)
    
    elif op == 0:
        print("Saindo do Sistema!!")
        pass



def painel_usuario(): #Falta completar as funções com dos "IF's" com as "DEF's" do Murilo.
    op = int(input("[OPÇÃO]-> "))
    if op == 1:
        listar_produtos_admin(lista_produtos, lista_carrinho)
    
    elif op == 2:
        pass

    elif op == 3:
        pass

    elif op == 4:
        pass
    
    elif op == 0:
        print("Saindo do Sistema!!")
        exit()




def logar_usuario(): #Falta colocar as novas funções do Murilo.
    usuario=input("Digite seu nome de Usuário: ")
    senha=input("Digite sua Senha: ")
    for _ in range(0,len(lista_usuario)):
        if usuario == lista_usuario[_].nome and senha == lista_usuario[_].senha:
            return True

            