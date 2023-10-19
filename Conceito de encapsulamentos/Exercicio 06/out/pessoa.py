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

    def calcular_idade(self):
        self.idade = 2023 - self._nascimento 

    def calcular_idade_aposentadoria(self):
        if (self._posicao == 'defesa'):
            self.idade_aposentadoria = 40
        elif(self._posicao == 'meio-campo'):
            self.idade_aposentadoria = 38
        elif self._posicao == 'atacante':
            self.idade_aposentadoria = 35
        else:
            self.idade_aposentadoria = 0

        self.idade_aposentadoria = self.idade_aposentadoria
        self.calcular_idade()
        self.idade_restante = self.idade - self.idade_aposentadoria
            
    def exibir(self):
        self.calcular_idade()
        self.calcular_idade_aposentadoria()
        print(f"\nNome do jogador: {self.nome}\nPosição: {self.get_posicao()}\nNascimento: {self.get_nascimento()}\nNacionalidade: {self.nacionalidade}\nAltura: {self.altura}\nPeso: {self.peso}\nIdade: {self.idade}\nIdade de aposentadoria: {self.idade_aposentadoria}\nAnos restantes até a aposentadoria: {self.idade_restante}\n")


nome = input("Nome do jogador: ")
posicao = input("Posição do jogador: ")
nascimento = int(input("Ano de nascimento: "))
nacionalidade = input("Nacionalidade: ")
altura = float(input("Altura: "))
peso = float(input("Peso: "))

jogador = Jogador(nome, posicao, nascimento, nacionalidade, altura, peso)

while True:

    opc = int(input(("\nO QUE DESEJA FAZER?\n1- Calcular idade.\n2- Calcular idade até aposentadoria.\n3- Exibir informações do jogador.\n4- Parar execucção.")))

    if opc == 1:
        jogador.calcular_idade()
        print(f"Idade: {jogador.idade}")

    elif (opc == 2):
        print("\nDefesa - 40 anos\nMeio-campo - 38 anos\nAtacante 35 anos.")
        jogador.set_posicao(str(input("Digite a posição: ")))
        jogador.calcular_idade_aposentadoria()
        print(f"Faltam {jogador.idade_restante} anos até a aposentadoria.\nVocê possui {jogador.idade}")

    elif(opc == 3):
        jogador.exibir()
        
    elif(opc == 4):
        print("Fim")
        break