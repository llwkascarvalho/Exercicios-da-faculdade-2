from arquivo2 import Usuario, SistemaVendas, Produto, Estoque


def exibir_menu():
    print("\n--- Menu ---")
    print("1. Cadastrar Usuário")
    print("2. Cadastrar Produto")
    print("3. Criar estoque")
    print("4. Exibir estoque")
    print("5. Listar Produtos de um Estoque")
    print("6. Adicionar Produto ao Estoque")
    print("7. Realizar Pedido")
    print("8. Sair")


def cadastrar_usuario():
    nome = input("Nome do usuário: ")
    email = input("Email do usuário: ")
    senha = input("Senha do usuário: ")
    endereco = input("Endereço do usuário: ")
    telefone = input("Telefone do usuário: ")

    novo_usuario = Usuario(nome, email, senha, endereco, telefone)
    sistema_vendas.adicionarUsuario(novo_usuario)
    print(f"Usuário {nome} cadastrado com sucesso!")


def cadastrar_produto():
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    quantidade = int(input("Quantidade do produto: "))
    descricao = input("Descrição do produto: ")

    novo_produto = Produto(nome, preco, quantidade, descricao)
    sistema_vendas.adicionarProdutoEstoque(novo_produto)
    print(f"Produto {nome} cadastrado com sucesso!")

def criarEstoque(self):
        novo_estoque = Estoque()
        self._estoques.append(novo_estoque)
        print("Estoque criado com sucesso!")
        
        
def exibir_estoques():
    for idx, estoque in enumerate(sistema_vendas.estoques, start=1):
        print(f"{idx}. {estoque}")


def listar_produtos_estoque():
    exibir_estoques()
    escolha_estoque = int(input("Escolha o número do Estoque: ")) - 1

    if 0 <= escolha_estoque < len(sistema_vendas.estoques):
        estoque_selecionado = sistema_vendas.estoques[escolha_estoque]
        print(f"Produtos no Estoque {escolha_estoque + 1}:")
        for produto in estoque_selecionado.produtos:
            print(produto)
    else:
        print("Escolha inválida. Estoque não encontrado.")


def adicionar_produto_estoque():
    exibir_estoques()
    escolha_estoque = int(input("Escolha o número do Estoque: ")) - 1

    if 0 <= escolha_estoque < len(sistema_vendas.estoques):
        estoque_selecionado = sistema_vendas.estoques[escolha_estoque]
        nome_produto = input("Nome do Produto a ser adicionado: ")

        # Buscar produto pelo nome
        produto_encontrado = None
        for produto in sistema_vendas.produtos:
            if produto.nome == nome_produto:
                produto_encontrado = produto
                break

        if produto_encontrado:
            estoque_selecionado.adicionarProduto(produto_encontrado)
            print(f"Produto {produto_encontrado.nome} adicionado ao Estoque {escolha_estoque + 1}.")
        else:
            print(f"Produto {nome_produto} não encontrado.")
    else:
        print("Escolha inválida. Estoque não encontrado.")


def realizar_pedido():
    exibir_usuarios()
    email_usuario = input("Email do usuário: ")

    # Verificar se o usuário existe
    usuario_existente = False
    for usuario in sistema_vendas.usuarios:
        if usuario.email == email_usuario:
            usuario_existente = True
            break

    if usuario_existente:
        exibir_produtos()
        produtos_pedido = []

        while True:
            nome_produto = input("Nome do Produto a ser adicionado ao pedido (ou 'sair' para finalizar): ")

            if nome_produto.lower() == 'sair':
                break

            # Buscar produto pelo nome
            produto_encontrado = None
            for produto in sistema_vendas.produtos:
                if produto.nome == nome_produto:
                    produto_encontrado = produto
                    break

            if produto_encontrado:
                produtos_pedido.append(produto_encontrado)
                print(f"Produto {produto_encontrado.nome} adicionado ao pedido.")
            else:
                print(f"Produto {nome_produto} não encontrado.")

        sistema_vendas.realizarPedido(email_usuario, produtos_pedido)
    else:
        print("Usuário não encontrado.")


def exibir_usuarios():
    print("\n--- Usuários ---")
    for usuario in sistema_vendas.usuarios:
        print(usuario)


def exibir_produtos():
    print("\n--- Produtos ---")
    for produto in sistema_vendas.produtos:
        print(produto)


# Criação do Sistema de Vendas
sistema_vendas = SistemaVendas()

# Menu Interativo
while True:
    exibir_menu()
    escolha = input("Escolha a opção (1-8): ")

    if escolha == '1':
        cadastrar_usuario()
    elif escolha == '2':
        cadastrar_produto()
    elif escolha == '3':
        criarEstoque()
    elif escolha == '4':
        exibir_estoques()
    elif escolha == '5':
        listar_produtos_estoque()
    elif escolha == '6':
        adicionar_produto_estoque()
    elif escolha == '7':
        realizar_pedido()
    elif escolha == '8':
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")