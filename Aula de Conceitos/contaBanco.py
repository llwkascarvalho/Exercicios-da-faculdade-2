class Conta: 
    
    def __init__(self, numero, titular, saldo, limite, codigo_tipo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.codigo_tipo = codigo_tipo if codigo_tipo == 1 or codigo_tipo == 2 else False
        self.nome_tipo = "corrente" if codigo_tipo == 1 else "poupança"

    def depositar(self, valor):
        if (valor > self.limite):
            return False
        else:
            self.saldo += valor
            return True
    
    def sacar(self, valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            return True
        
    def transferir (self, valor, destino):
        if(self.saldo < valor):
            return "Saldo insuficiente"
        elif (self.limite < valor):
            return "Valor excedido."
        else: 
            self.saldo -= valor
            destino.saldo += valor
        
    def extrato(self):
        print("Número da Conta: {}\nTitular: {}\nSaldo: {}".format(self.numero, self.titular, self.saldo))
        print("Tipo de Conta: {} - {}".format(self.codigo_tipo, self.nome_tipo))


conta1 = Conta(
    int(input("Digite o número da conta: ")),
    str(input("Digite o nome do titular da conta: ")),
    float(input("Digite o saldo da conta: ")),
    float(input("Digite o limite da conta: ")),
    int(input("Tipo da conta 01 para poupança, 02 para corrente: "))
)

conta2 = Conta(
    int(input("Digite o número da conta: ")),
    str(input("Digite o nome do titular da conta: ")),
    float(input("Digite o saldo da conta: ")),
    float(input("Digite o limite da conta: ")),
    int(input("Tipo da conta 01 para poupança, 02 para corrente: "))
)

valorTrans = float(input("valor da transferencia: "))

opc = int(input("Conta que deseja realizar a transferencia: "))

if (opc == 1):
    conta1.transferir (valorTrans, conta2)
elif (opc == 2):
    conta2.transferir (valorTrans, conta1)
else:
    print ("invalido")

print (conta1.saldo)
print (conta2.saldo)