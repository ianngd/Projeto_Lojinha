class Cliente():
    def __init__(self, nome, senha, cpf, telefone, idade, saldo ):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.telefone = telefone
        self.senha = senha
        self.saldo = saldo


class Produto():
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco


