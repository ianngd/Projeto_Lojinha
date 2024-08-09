from funcoes import *
from previwer import *

lista_carrinho=[]
lista_produtos=[]
lista_usuario=[]
produtitos = []

#Main
while True:
    menu_inicial()
    opt_menu=input("[OPÇÃO]-> ")
    # Registrar Usuário
    if opt_menu =="1":
        limpar_tela()
        criar_usuario_novo(lista_usuario)
    elif opt_menu =="2":
        pass
    elif opt_menu =="3":
        while True:
            menu_inicial()
            op = int(input('Digite sua escolha: '))
            if op == 0:
                print('Volte sempre!')
                break
            elif op == 1:
                pass
            elif op ==2:
                produtitos.append(fazer_login())
                while True:
                    menu_gerente
                    ops = int(input("Digite sua escolha: "))
                    if ops == 0:
                        break
    elif opt_menu =="0":
        print("Volte Sempre !!!")
        exit()
    else:
        print("Opção Errada!!")
        pressione_enter()

#Fim_Main