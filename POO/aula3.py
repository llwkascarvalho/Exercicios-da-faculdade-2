class Pessoa:
    
    def __init__(self, nome, cpf, altura):
        self.nome = nome
        self.cpf = cpf
        self.altura = altura 

class Secretaria(Pessoa): 
    
    def __init__(self, id_secretaria, nome, cpf, altura):
        super().__init__(nome, cpf, altura)
        self.id_secretaria = id_secretaria
        
    def __str__(self):
        return f'Nome da secretária: {self.nome} CPF: {self.cpf} ID: {self.id_secretaria} Altura: {self.altura}'
        

s1 = Secretaria('2', 'Maria', '019283472', '170')

string = s1.__str__()

print(string)




# POLIMORFISMO 

class Animal:
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return "Woof!"

class Gato(Animal):
    def falar(self):
        return "Meow!"

class Pato(Animal):
    def falar(self):
        return "Quack!"

# Função que interage com diferentes tipos de animais de forma polimórfica
def fazer_barulho(animal):
    return animal.falar()

# Criando instâncias das diferentes classes de animais
cachorro = Cachorro()
gato = Gato()
pato = Pato()

# Chamando a função fazer_barulho com diferentes tipos de animais
print(fazer_barulho(cachorro))  # Saída: "Woof!"
print(fazer_barulho(gato))      # Saída: "Meow!"
print(fazer_barulho(pato))      # Saída: "Quack!"
