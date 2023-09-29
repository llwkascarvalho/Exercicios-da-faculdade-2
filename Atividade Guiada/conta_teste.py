from conta import Conta
from conta import Cliente

cliente = Cliente('Lwkas', 'Carvalho', 123456)
conta = Conta('1234-5',cliente,100,1000)

conta.depositar(500)
conta.saca(200)

conta.extrato()

conta.historico.imprime()