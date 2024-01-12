from datetime import datetime

class Produto:
    def __init__(self, nome, preco, quantidade, descricao):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.descricao = descricao

class Usuario:
    def __init__(self, nome, email, senha, endereco, telefone):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.endereco = endereco
        self.telefone = telefone

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
        self.valorTotal = 0.0
        self.status = "Pendente"

    def adicionarProduto(self, produto):
        self.produtos.append(produto)
        self.valorTotal += produto.preco

    def removerProduto(self, produto):
        if produto in self.produtos:
            self.produtos.remove(produto)
            self.valorTotal -= produto.preco

class SistemaVendas:
    def __init__(self):
        self.usuarios = []
        self.estoques = []
        self.pedidos = []

    def autenticarUsuario(self, email, senha):
        for usuario in self.usuarios:
            if usuario.email == email and usuario.senha == senha:
                return True
        return False

    def calcularFrete(self, endereco, produtos):
        taxa_frete_por_produto = 2.0
        total_produtos = sum(produto.quantidade for produto in produtos)

        frete = taxa_frete_por_produto * total_produtos
        print(f"Frete para {endereco}: R${frete:.2f}")
        return frete

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

    def realizarPedido(self, usuario, produtos):
        if usuario in self.usuarios:
            pedido = Pedido()
            for produto in produtos:
                pedido.adicionarProduto(produto)
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
            print("Usuário adicionado com sucesso!")

        elif escolha == '2':
            nome_produto = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            quantidade = int(input("Quantidade do produto: "))
            descricao = input("Descrição do produto: ")

            produto = Produto(nome_produto, preco, quantidade, descricao)
            estoque = Estoque()
            estoque.adicionarProduto(produto)
            sistema_vendas.adicionarEstoque(estoque)
            print("Produto adicionado com sucesso!")

        elif escolha == '3':
            email_usuario = input("Email do usuário: ")
            senha_usuario = input("Senha do usuário: ")

            if sistema_vendas.autenticarUsuario(email_usuario, senha_usuario):
                print("Autenticação bem-sucedida!")
                nome_produto_pedido = input("Nome do produto a ser pedido: ")
                quantidade_pedido = int(input("Quantidade do produto a ser pedido: "))

                usuario_atual = next(u for u in sistema_vendas.usuarios if u.email == email_usuario)
                produto_pedido = next(p for p in sistema_vendas.estoques[0].produtos if p.nome == nome_produto_pedido)
                produtos_pedido = [produto_pedido] * quantidade_pedido

                sistema_vendas.realizarPedido(usuario_atual, produtos_pedido)
                print("Pedido realizado com sucesso!")
            else:
                print("Autenticação falhou. Verifique o email e a senha.")

        elif escolha == '4':
            print("Saindo do programa. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
