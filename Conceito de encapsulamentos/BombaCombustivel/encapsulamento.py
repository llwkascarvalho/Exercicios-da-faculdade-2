class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel
    
    def abastecerPorValor(self,valor):
        litrosAbastecidos = valor / self.valorLitro
        if litrosAbastecidos <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litrosAbastecidos
            print(f"Abastecimento realizado. Litros abastecidos: {litrosAbastecidos}")
        else:
            print("Quantidade de combustível insuficiente na bomba.")

    def abastecerPorLitro(self, litros):
        valorAbastecido = litros * self.valorLitro
        if valorAbastecido <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= valorAbastecido
            print(f"Abastecimento realizado. Valor a pagar: {valorAbastecido}")
        else:
            print("Quantidade de combustível insuficiente na bomba.")
        
    def alterarValor(self, novoValorLitro):
        self.valorLitro = novoValorLitro
        print("Valor alterado para:", self.valorLitro)

    def alterarCombustivel(self, novoTipoCombustivel):
        self.tipoCombustivel = novoTipoCombustivel
        print("Novo tipo de combustivel:", self.tipoCombustivel)
    
    def alterarQuantidadeCombustivel(self, novaQuantidadeCombustivel):
        self.quantidadeCombustivel = novaQuantidadeCombustivel
        print("Quantidade de combustivel na bomba alterada para:",self.quantidadeCombustivel)
    

bomba = BombaCombustivel(["Comum, Aditivada, Premium"], 4.50, quantidadeCombustivel = float(input("Digite a quantidade  de Combustivel da bomba: ")))

print("\n---BOMBA DE COMBUSTIVEL---\n")
print("Tipos de Combustivel: {}\nPreço por litro: {}\nQuantidade de gasolina na bomba: {}".format(bomba.tipoCombustivel, bomba.valorLitro, bomba.quantidadeCombustivel))

opc = int(input("\n1 - Abastecer por valor\n2 - Abastecer por litro\n3 - Alterar o valor do combustivel\n4 - Alterar o tipo do Combustivel\n5- Alterar a quantidade de combustivel na bomba\n"))
if(opc == 1):
    bomba.abastecerPorValor(float(input("Digite o valor: ")))
elif(opc == 2):
    bomba.abastecerPorLitro(float(input("Digite a quantidade de litros: ")))
elif(opc == 3):
    bomba.alterarValor(float(input("Digite um novo valor para o litro: ")))
elif(opc == 4):
    bomba.alterarCombustivel(str(input("Digite o novo tipo de combustivel: ")))
elif(opc == 5):
    bomba.alterarQuantidadeCombustivel(float(input("Digite a nova quantidade de combustivel: ")))
