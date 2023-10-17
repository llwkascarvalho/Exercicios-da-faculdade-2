# Crie uma classe Elevador para armazenar as informações de um elevador de prédio. A classe deve armazenar o andar atual (térreo = 0), total de andares no prédio (desconsiderando o térreo), capacidade do elevador e quantas pessoas estão presentes nele. A classe deve também disponibilizar os seguintes métodos:

class Elevador:
    def __init__(self):
        self.andar_atual = 0
        self.total_andares_prédio = 10
        self.capacidade_elevador = 10
        self.qtd_pessoas_elevador = 0

    def inicializar(self):
        pass
        # que deve receber como parâmetros a capacidade do elevador e o total de andares no prédio (os elevadores sempre começam no térreo e vazio);
    def entrar(self):
        pass
        #  para acrescentar uma pessoa no elevador (só deve acrescentar se ainda houver espaço)
    def sair(self):
        pass
        # para remover uma pessoa do elevador (só deve remover se houver alguém dentro dele);
    def subir(self):
        pass
        # para subir um andar (não deve subir se já estiver no último andar);
    def descer(self):
        pass
        # para descer um andar (não deve descer se já estiver no térreo);

# Obs.: Encapsular todos os atributos da classe (criar os métodos set e get).

while True: 
    pass