class Pessoa:
    nome = str(input("\nNome: "))
    idade = int(input("Idade: "))
    peso = float(input("Peso: "))
    altura = float(input("Altura: "))

    def envelhecer (self,crescer,envelhecer):
        self.altura += crescer
        self.idade += envelhecer

    def engordar (self, engordar):
        self.peso += engordar
    
    def emagrecer (self, emagrecer):
        self.peso -= emagrecer
    
    def crescer (self, crescer):
        self.altura += crescer

pessoa = Pessoa()

while True:
    print("-------------------------")
    print("1- Envelhecer")
    print("-------------------------")
    print("2- Engordar")
    print("-------------------------")
    print("3- Emagrecer")
    print("-------------------------")
    print("4- Crescer")
    print("-------------------------")
    opc = int(input("Selecione uma opção: "))

    if (opc == 1):
        envelhecer = int(input("Envelhecer quanto? "))
        while pessoa.idade < 21 and envelhecer > 0:
            pessoa.idade += 1
            pessoa.altura += 0.05 
            envelhecer -= 1
    
        pessoa.idade += envelhecer

    elif (opc == 2):
        engordar = float(input("Engordar quanto? "))
        pessoa.peso += engordar

    elif (opc == 3):
        emagrecer = float(input("Emagrecer quanto? "))
        pessoa.peso -= emagrecer

    elif (opc == 4):
        crescer = float(input("Crescer quanto? "))
        pessoa.altura += crescer

    resposta = str(input("Deseja alterar mais alguma coisa? [s/n] "))
    if resposta != 's':
        break  

print("------------------------------------")
print ("Aqui está as informações digitadas:")
print("\nNome: ",pessoa.nome)
print("------------------------------------")
print("Idade: ",pessoa.idade)
print("------------------------------------")
print("Peso: ",pessoa.peso)
print("------------------------------------")
print("Altura: ",pessoa.altura)
print("------------------------------------")