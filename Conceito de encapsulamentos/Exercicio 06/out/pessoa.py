class Jogador:
    def __init__(self, nome, posicao, nascimento, nacionalidade, altura, peso):
        self.nome = nome
        self._posicao = posicao
        self._nascimento = nascimento
        self.nacionalidade = nacionalidade
        self.altura = altura
        self.peso = peso

    def get_posicao(self):
        return self._posicao

    def set_posicao(self, nova_posicao):
        self._posicao = nova_posicao

    def get_nascimento(self):
        return self._nascimento

    def set_nascimento(self, novo_nascimento):
        self._nascimento = novo_nascimento

    def calcular_idade(self, nascimento):
        self.idade = nascimento - 2023 
        print(f"Idade: {self.idade}")

jogador = Jogador(nome = 'Lwkas', posicao='Zagueiro', nascimento= 2004, nacionalidade='Brasileiro', altura=1.60,peso=58)

