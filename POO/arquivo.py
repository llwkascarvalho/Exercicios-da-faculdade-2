from abc import ABC, abstractmethod
from datetime import datetime


class MixinAutenticacao(ABC):
    @abstractmethod
    def autenticar(self, email, senha):
        pass

class String(ABC):
    @abstractmethod
    def __str__(self):
        pass

class Usuario(String):
    def __init__(self, nome, email, senha, endereco, telefone):
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__endereco = endereco
        self.__telefone = telefone

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def get_senha(self):
        return self.__senha

    def get_endereco(self):
        return self.__endereco

    def get_telefone(self):
        return self.__telefone

    def __str__(self):
        return f"Nome do usuário: {self.get_nome()}\nEmail: {self.get_email()}\n"
    
class Produto:
    def __init__(self, nome, preco, quantidade, descricao):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade
        self.__descricao = descricao

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def get_quantidade(self):
        return self.__quantidade

    def get_descricao(self):
        return self.__descricao

    def __str__(self):
        return f"\nNome do produto: {self.get_nome()}\nDescrição: {self.get_descricao()}\n"

class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionarProduto(self, produto):
        self.produtos.append(produto)

    def removerProduto(self, produto):
        if produto in self.produtos:
            self.produtos.remove(produto)

class Pedido:
    def __init__(self):
        self.data = datetime.now()
        self.produtos = []
        self.valor_total = 0.0
        self.status = "Pendente"

    def adicionarProduto(self, produto, quantidade):
        for _ in range(quantidade):
            self.produtos.append(produto)
            self.valor_total += produto.get_preco()

    def removerProduto(self, produto, quantidade):
        for _ in range(quantidade):
            if produto in self.produtos:
                self.produtos.remove(produto)
                self.valor_total -= produto.get_preco()
                
    def __str__(self):
        return f"Data do Pedido: {self.data}"

class SistemaVendas(MixinAutenticacao):
    def __init__(self):
        self.usuarios = []
        self.estoques = []
        self.pedidos = []

    def autenticar(self, email, senha):
        for usuario in self.usuarios:
            if usuario.get_email() == email and usuario.get_senha() == senha:
                return True
        return False

    def calcularFrete(self, produtos_pedido):
        quantidade_produtos = sum(produto.get_quantidade() for produto in produtos_pedido)

        if quantidade_produtos == 1:
            return 10.0
        elif quantidade_produtos >= 3:
            return 25.0
        else:
            return 0.0

    def adicionarUsuario(self, usuario):
        self.usuarios.append(usuario)

    def removerUsuario(self, usuario):
        if usuario in self.usuarios:
            self.usuarios.remove(usuario)

    def adicionarEstoque(self, estoque):
        self.estoques.append(estoque)

    def removerEstoque(self, estoque):
        if estoque in self.estoques:
            self.estoques.remove(estoque)

    def realizarPedido(self, usuario, produtos, quantidade):
        if usuario in self.usuarios:
            pedido = Pedido()
            for produto in produtos:
                pedido.adicionarProduto(produto, quantidade)
            self.pedidos.append(pedido)


def exibir_menu():
    print("\n===== Menu =====")
    print("1. Adicionar Usuário")
    print("2. Adicionar Produto")
    print("3. Realizar Pedido")
    print("4. Sair")

def main():
    sistema_vendas = SistemaVendas()

    while True:
        exibir_menu()
        escolha = input("Escolha a opção (1-4): ")

        if escolha == '1':
            nome = input("Nome do usuário: ")
            email = input("Email do usuário: ")
            senha = input("Senha do usuário: ")
            endereco = input("Endereço do usuário: ")
            telefone = input("Telefone do usuário: ")

            usuario = Usuario(nome, email, senha, endereco, telefone)
            sistema_vendas.adicionarUsuario(usuario)
            print("\n\nUsuario cadastrado com Sucesso!")
            string = usuario.__str__()
            print(string)

        elif escolha == '2':
            nome_produto = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            quantidade = int(input("Quantidade do produto: "))
            descricao = input("Descrição do produto: ")

            produto = Produto(nome_produto, preco, quantidade, descricao)
            estoque = Estoque()
            estoque.adicionarProduto(produto)
            sistema_vendas.adicionarEstoque(estoque)
            print("\nProduto adicionado com sucesso!")
            string = produto.__str__()
            print(string)

        elif escolha == '3':
            email_usuario = input("Email do usuário: ")
            senha_usuario = input("Senha do usuário: ")

            if sistema_vendas.autenticar(email_usuario, senha_usuario):
                print("Autenticação bem-sucedida!")
                nome_produto_pedido = input("Nome do produto a ser pedido: ")
                quantidade_pedido = int(input("Quantidade do produto a ser pedido: "))

                usuario_atual = next(u for u in sistema_vendas.usuarios if u.get_email() == email_usuario)
                produto_pedido = next(p for p in sistema_vendas.estoques[0].produtos if p.get_nome() == nome_produto_pedido)
                produtos_pedido = [produto_pedido] * quantidade_pedido

                pedido = Pedido()
                pedido.adicionarProduto(produto_pedido, quantidade_pedido)
                sistema_vendas.pedidos.append(pedido)
                frete = sistema_vendas.calcularFrete(produtos_pedido)

                string = pedido.__str__()
                print(string)
                print(f"Pedido realizado com sucesso! Frete: R${frete:.2f}")
                print(f"Frete: R${frete:.2f}")
                print(f"Valor total (com frete): R${pedido.valor_total + frete:.2f}")
            else:
                print("Autenticação falhou.")

        elif escolha == '4':
            print("Saindo do programa. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()