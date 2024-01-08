class Quarto:
    def __init__(self, numero):
        self.numero = numero

class Casa:
    def __init__(self):
        self.quartos = [Quarto(1), Quarto(2)]

    def destruir(self):
        self.quartos = None


minha_casa = Casa()

print("Quartos antes de destruir a casa:", [quarto.numero for quarto in minha_casa.quartos])

minha_casa.destruir()

try:
    print(f"Existia quartos")
except AttributeError as e:
    print(f"Erro ao tentar acessar os quartos após destruir a casa: {e}")
