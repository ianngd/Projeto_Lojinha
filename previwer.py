def menu_inicial():
    print("""       
+=======[LOJINHA DO LUCAS]=======+
| [1]-Registrar Usuário          |
| [2]-Logar como Usuário         |
| [3]-Logar como Admin           |
| [0]-Sair                       |
+================================+""")


def listar_produstos(produtos, carrinho):
    for i in produtos:
        print(f"{i + 1} - {produtos[i]}")
    op = int(input("Escolha um produto: "))
    produto_selecionado = produtos[op - 1]
    carrinho.append(produto_selecionado)

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