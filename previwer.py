def menu_inicial():
    print("""       
+=======[LOJINHA DO LUCAS]=======+
| [1]-Registrar Usuário          |
| [2]-Logar como Usuário         |
| [3]-Logar como Admin           |
| [0]-Sair                       |
+================================+""")
    
def listar_produtos_admin(produtos, carrinho):
    for i in produtos:
        print(f"{i + 1} - {produtos[i]}")
    op = int(input("Escolha um produto: "))
    produto_selecionado = produtos[op - 1]
    carrinho.append(produto_selecionado)

def listar_produtos_usuario(produtos):
    for i in produtos:
        print(f"{i + 1} - {produtos[i]}")
    #To em duvida, substituir o codigo do Murilo ou não?   

def menu_admin():
    print("""
+=======[MENU DO ADMIN]=======+
| [1]-Listar Produtos         |
| [2]-Adicionar Produtos      |
| [3]-Remover Produtos        |
| [4]-Listar Usuários         |
| [0]-Sair                    |         
+=============================+""")


def listar_usuarios_do_sistema(lista_usuarios):
    print("      [USUÁRIOS CRIADOS]")
    print("+============================+")
    for _ in range(0,lista_usuarios):
        print(f"{lista_usuarios[_].nome}")
    print("+============================+")



#Coisas para eu fazer:
#Logar usuário
#Listar Produtos
#Criar tela do usuário-Feito



def interface_usuario():
    print("""
+===========[MENU DO USUÁRIO]===========+
| [1]-Listar Produtos da Loja           |
| [2]-Adicionar Produtos no Carrinho    |
| [3]-Vizualizar Carrinho de Compras    |
| [4]-Adicionar Saldo
| [0]-Sair                              |         
+=======================================+""")
    


    
