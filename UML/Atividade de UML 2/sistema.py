from datetime import datetime
from enum import Enum, auto

class Aeroporto:
    def __init__(self, nome, cidade, capacidade_decolagens_por_hora):
        self.nome = nome
        self.cidade = cidade
        self.capacidade_decolagens_por_hora = capacidade_decolagens_por_hora

class TipoVoo(Enum):
    NACIONAL = auto()
    INTERNACIONAL = auto()

class Voo:
    def __init__(self, codigo, horario, data, aeroporto_partida, aeroporto_destino, tipo, tripulacao=None):
        self.codigo = codigo
        self.horario = horario
        self.data = data
        self.aeroporto_partida = aeroporto_partida
        self.aeroporto_destino = aeroporto_destino
        self.tipo = tipo
        self.tripulacao = tripulacao
        self.reservas = []

    def assentos_livres(self):
        return 100 - len(self.reservas)

    def informacoes_voo(self):
        return f"Código: {self.codigo}, Horário: {self.horario}, Data: {self.data}, " \
               f"Partida: {self.aeroporto_partida.nome}, Destino: {self.aeroporto_destino.nome}, " \
               f"Tipo: {self.tipo.name}"

class Reserva:
    def __init__(self, passageiro):
        self.passageiro = passageiro
        self.status = "Pendente"

    def confirmar_reserva(self):
        self.status = "Confirmada"
    
    def cancelar_reserva(self):
        self.status = "Cancelada"

    def pagar_reserva(self):
        if self.status == "Confirmada":
            print("Reserva já está confirmada. Não é necessário pagamento.")
        else:
            print("Pagamento da reserva realizado com sucesso!")
            self.status = "Confirmada"

class Passageiro:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Operador:
    def __init__(self, nome, codigo_funcionario):
        self.nome = nome
        self.codigo_funcionario = codigo_funcionario

    def criar_reserva(self, voo, passageiro):
        reserva = Reserva(passageiro)
        voo.reservas.append(reserva)
        return reserva

    def cancelar_reserva(self, reserva):
        reserva.cancelar_reserva()


def exibir_menu():
    print("\nMenu:")
    print("1. Criar Reserva")
    print("2. Cancelar Reserva")
    print("3. Pagar Reserva")
    print("4. Informações do Voo")
    print("5. Assentos Livres")
    print("0. Sair")


aeroporto1 = Aeroporto("Aeroporto 1", "Cidade 1", 10)
aeroporto2 = Aeroporto("Aeroporto 2", "Cidade 2", 15)

voo1 = Voo("V001", datetime.now(), datetime.now(), aeroporto1, aeroporto2, TipoVoo.INTERNACIONAL)
passageiro1 = Passageiro("João", "123.456.789-01")
operador1 = Operador("Maria", "OP001")

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        reserva = operador1.criar_reserva(voo1, passageiro1)
        print(f"Reserva criada com sucesso! Status: {reserva.status}")
    elif opcao == "2":
        operador1.cancelar_reserva(reserva)
        print(f"Reserva cancelada com sucesso! Status: {reserva.status}")
    elif opcao == "3":
        reserva.pagar_reserva()
    elif opcao == "4":
        print(voo1.informacoes_voo())
    elif opcao == "5":
        print(f"Assentos Livres: {voo1.assentos_livres()}")
    elif opcao == "0":
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
