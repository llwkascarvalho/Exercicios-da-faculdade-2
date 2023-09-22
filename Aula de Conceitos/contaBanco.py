class Conta: 
    
    def __init__(self, numero, titular, saldo, limite, nome_tipo, codigo_tipo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.codigo_tipo = codigo_tipo
        self.nome_tipo = nome_tipo

    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            return True
        
    def transferir (self, valor, destino):
        if self.sacar(valor):
            destino.depositar(valor)
            print(f"Transferência de R${valor} realizada com sucesso para a conta de {destino.titular}.")
        else:
            print("Saldo insuficiente para a transferência.")
        
    def extrato(self):
        print("Número da Conta: {}\nTitular: {}\nSaldo: {}".format(self.numero, self.titular, self.saldo))
        print("Tipo de Conta: {} - {}".format(self.codigo_tipo, self.nome_tipo))
    
print ("\n01- Conta Corrente\n02- Conta Poupança")
codigo_tipo = input("Qual tipo de conta deseja criar (01 para Conta Corrente, 02 para Conta Poupança)? ")
nome_tipo = "Conta Corrente" if codigo_tipo == "01" else "Conta Poupança"

numero_conta = input("Digite o número da conta: ")
titular_conta = input("Digite o nome do titular da conta: ")
saldo_conta = float(input("Digite o saldo da conta: "))
limite_conta = float(input("Digite o limite da conta: "))

conta = Conta(numero_conta, titular_conta, saldo_conta, limite_conta, codigo_tipo, nome_tipo)

print("\nExtrato da conta:")
conta.extrato()
