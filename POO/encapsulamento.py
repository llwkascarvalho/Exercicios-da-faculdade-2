class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

#get e set
    def get_nome(self):
        print("Obtendo nome")
        return self.__nome
    
    def set_nome(self, novo_nome):
        print("Definindo novo nome")
        self.__nome = novo_nome

#property
    @property
    def idade(self):
        print("Obtendo idade")
        return self.__idade

    @idade.setter
    def idade(self, nova_idade):
        print("Definindo idade")
        if nova_idade >= 0:
            self.__idade = nova_idade
        else:
            print("Idade não pode ser negativa.")

    @idade.deleter
    def idade(self):
        print("Deletando idade")
        del self.__idade

# Instancia
pessoa = Pessoa("João", 25)

# Exibindo com get
print("Nome:", pessoa.get_nome())
# Modificando com set
pessoa.set_nome("Maria")
print("Novo Nome:", pessoa.get_nome())


# Exibindo com property
print("Idade:", pessoa.idade)
# Modificando com property
pessoa.idade = 30
print("Nova Idade:", pessoa.idade)

del pessoa.idade
