from classes import *
import getpass
import time
import os

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

def listar_usuarios_do_sistema(lista_usuarios):
    print("      [USUÁRIOS CRIADOS]")
    print("+============================+")
    for _ in range(0,lista_usuarios):
        print(f"{lista_usuarios[_].nome}")
    print("+============================+")

def adicionar_produto():
    _nome