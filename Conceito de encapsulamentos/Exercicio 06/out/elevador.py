# Crie uma classe Elevador para armazenar as informações de um elevador de prédio. A classe deve armazenar o andar atual (térreo = 0), total de andares no prédio (desconsiderando o térreo), capacidade do elevador e quantas pessoas estão presentes nele. A classe deve também disponibilizar os seguintes métodos:

class Elevador:
    def __init__(self):
        self.andar_atual = 0
        self.total_andares = 0
        self.capacidade = 0
        self.qtd_pessoas = 0

    def inicializar(self, capacidade, total_andares):
        self.capacidade = capacidade
        self.total_andares = total_andares
        # que deve receber como parâmetros a capacidade do elevador e o total de andares no prédio (os elevadores sempre começam no térreo e vazio);
    def entrar(self):
        if int(self.qtd_pessoas) > int(self.capacidade):
            print("Não há espaço no elevador.", self.qtd_pessoas)
        else:
            self.qtd_pessoas += 1
            print("Pode entrar!", self.qtd_pessoas)

        #  para acrescentar uma pessoa no elevador (só deve acrescentar se ainda houver espaço)
    def sair(self):
        if self.qtd_pessoas > 0:
            self.qtd_pessoas - 1
            print("Pessoas no elevador: ",self.qtd_pessoas)
        # para remover uma pessoa do elevador (só deve remover se houver alguém dentro dele);
    def subir(self, andar_destino):
        print("Estamos no andar:", self.andar_atual)
        if int(self.andar_atual) < int(self.total_andares):
            self.andar_atual += andar_destino
            print("Subindo para o andar:", self.andar_atual)
        else:
            print("Já estamos no último andar. Não é possível subir mais.")
        # para subir um andar (não deve subir se já estiver no último andar);
    def descer(self,descer):
        print("Estamos no andar: ", self.andar_atual)
        self.andar_atual -= descer
        print("Agora estamos no andar: ",self.andar_atual)
        # para descer um andar (não deve descer se já estiver no térreo);

# Obs.: Encapsular todos os atributos da classe (criar os métodos set e get).


elevador = Elevador()
while True:
    opc = input("\nO que deseja?\n1- Inicializar\n2- Entrar no elevador\n3- Sair do elevador\n4- Subir\n5- Descer\n6- Parar execução\n")

    if opc == '1':
        total_andares = input("Qual a quantidade de andares? ")
        capacidade = input("Capacidade: ")
        elevador.inicializar(capacidade, total_andares)
    elif opc == '2':
        elevador.entrar()
    elif opc == '3':
        elevador.sair()
    elif opc == '4':
        andares = int(input("Quantos andares deseja subir? "))
        elevador.subir(andares)
    elif opc == '5':
        andares = int(input("Quantos andares deseja descer? "))
        elevador.descer(andares)
    elif opc == '6':
        print("Fim")
        break
        