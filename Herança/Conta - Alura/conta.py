import datetime

class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.data_abertura = datetime.date.today()
        self.historico = Historico()

    def depositar(self,valor):
        self.saldo += valor
        self.historico.transacoes.append(f"Depósito de R${valor:.2f} em {self.data_abertura}")

    def saca(self, valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append(f"Saque de R${valor:.2f} em {self.data_abertura}")
            return True

    def extrato(self):
        print("Número: {}\nSaldo: {}\nTitular: {} {}\nCPF: {}".format(self.numero, self.saldo, self.titular.nome, self.titular.sobrenome, self.titular.cpf))

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            return True
        
    def atualiza(self, taxa):
        self.saldo += self.saldo * (taxa/100)

class Cliente:
    def __init__ (self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

class Historico:
    def __init__(self):
        self.transacoes = []

    def imprime(self):
        for transacao in self.transacoes:
            print(transacao)