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