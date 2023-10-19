# Crie uma classe Elevador para armazenar as informações de um elevador de prédio. A classe deve armazenar o andar atual (térreo = 0), total de andares no prédio (desconsiderando o térreo), capacidade do elevador e quantas pessoas estão presentes nele. A classe deve também disponibilizar os seguintes métodos:

class Elevador:
    def __init__(self):
        self._andar_atual = 0
        self._total_andares = 0
        self._capacidade = 0
        self._pessoas_presentes = 0

    def inicializar(self, capacidade, total_andares):
        self._capacidade = capacidade
        self._total_andares = total_andares
        # que deve receber como parâmetros a capacidade do elevador e o total de andares no prédio (os elevadores sempre começam no térreo e vazio);

    def get_capacidade(self):
        return self._capacidade

    def set_capacidade(self, nova_capacidade):
        if nova_capacidade >= 0:
            self._capacidade = nova_capacidade
        else:
            print("Capacidade inválida.")

    capacidade = property(get_capacidade, set_capacidade)

    def get_total_andares(self):
        return self._total_andares

    def set_total_andares(self, novo_total_andares):
        if novo_total_andares >= 0:
            self._total_andares = novo_total_andares
        else:
            print("Total de andares inválido.")

    total_andares = property(get_total_andares, set_total_andares)

    def entrar(self):
        if int(self._pessoas_presentes) < int(self._capacidade):
            self._pessoas_presentes += 1
            print("Uma pessoa entrou no elevador.")
        else:
            print("O elevador está cheio. Não é possível entrar mais pessoas.")
        #  para acrescentar uma pessoa no elevador (só deve acrescentar se ainda houver espaço)
    def sair(self):
        if self._pessoas_presentes > 0:
            self._pessoas_presentes -= 1
            print("Uma pessoa saiu do elevador.")
        else:
            print("O elevador está vazio. Não é possível remover pessoas.")
        # para remover uma pessoa do elevador (só deve remover se houver alguém dentro dele);
    def subir(self):
        if int(self._andar_atual) < int(self._total_andares):
            self._andar_atual += 1
            print(f"Subindo para o andar {self._andar_atual}.")
        else:
            print("Já estamos no último andar. Não é possível subir mais.")
        # para subir um andar (não deve subir se já estiver no último andar);
    def descer(self):
        if self._andar_atual > 0:
            self._andar_atual -= 1
            print(f"Descendo para o andar {self.andar_atual}.")
        else:
            print("Já estamos no térreo. Não é possível descer mais.")
        # para descer um andar (não deve descer se já estiver no térreo);
    def exibir_status(self):
        print(f"Andar atual: {self._andar_atual}")
        print(f"Total de andares no prédio: {self._total_andares}")
        print(f"Capacidade do elevador: {self._capacidade}")
        print(f"Pessoas presentes no elevador: {self._pessoas_presentes}")

    def get_andar_atual(self):
        return self._andar_atual

    def set_andar_atual(self, novo_andar):
        if 0 <= novo_andar <= self._total_andares:
            self._andar_atual = novo_andar
        else:
            print("Andar inválido.")

    andar_atual = property(get_andar_atual, set_andar_atual)

    def get_pessoas_presentes(self):
        return self._pessoas_presentes

    def set_pessoas_presentes(self, nova_quantidade):
        if 0 <= nova_quantidade <= self._capacidade:
            self._pessoas_presentes = nova_quantidade
        else:
            print("Quantidade de pessoas presente inválida.")

    pessoas_presentes = property(get_pessoas_presentes, set_pessoas_presentes)

elevador = Elevador()

while True:
    opc = input("\nO que deseja?\n1- Inicializar\n2- Entrar no elevador\n3- Sair do elevador\n4- Subir\n5- Descer\n6- Exibir Status\n7- Parar execução\n")

    if opc == '1':
        total_andares = int(input("Qual a quantidade de andares? "))
        capacidade = int(input("Capacidade: "))
        elevador.inicializar(capacidade, total_andares)
    elif opc == '2':
        elevador.entrar()
    elif opc == '3':
        elevador.sair()
    elif opc == '4':
        elevador.subir()
    elif opc == '5':
        elevador.descer()
    elif opc == '6':
        elevador.exibir_status()
    elif opc == '7':
        print("Fim")
        break