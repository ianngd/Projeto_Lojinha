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