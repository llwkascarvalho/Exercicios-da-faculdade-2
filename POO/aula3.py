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
