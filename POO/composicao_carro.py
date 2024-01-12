# COMPOSIÇÃO

class Acelerador:
    def acelerar(self):
        print("O carro acelerou!")
         
class Freio:
    def freiar(self):
        print("O carro freiou")
        
class Carro: 
    def __init__(self):
        self.acelerador = Acelerador()
        self.freio = Freio()
        
    
            
carro = Carro()

carro.acelerador.acelerar()
carro.freio.freiar()

# AGREGAÇÃO

class Roda:
    def __init__(self, tamanho):
        self.tamanho = tamanhoç

class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.roda_dianteira_esquerda = Roda(15)
        self.roda_dianteira_direita = Roda(15)
        self.roda_traseira_esquerda = Roda(15)
        self.roda_traseira_direita = Roda(15)
