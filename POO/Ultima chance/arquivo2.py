from menu import *
from abc import ABC, abstractmethod
from datetime import datetime

# Mixin para autenticação
class MixinAutenticacao(ABC):
    @abstractmethod
    def autenticar(self, email, senha):
        pass


class String(ABC):
    @abstractmethod
    def __str__(self):
        pass

# Implementação da interface e mixin
class Usuario(String, MixinAutenticacao):
    def __init__(self, nome, email, senha, endereco, telefone):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.endereco = endereco
        self.telefone = telefone

    def __str__(self):
        return f"{self.nome} ({self.email})"

    def autenticar(self, email, senha):
        return self.email == email and self.senha == senha

class Produto(String):
    def __init__(self, nome, preco, quantidade, descricao):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.descricao = descricao

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f}"

class Estoque(String):
    def __init__(self):
        self.produtos = []

    def adicionarProduto(self, produto):
        self.produtos.append(produto)

    def removerProduto(self, produto):
        if produto in self.produtos:
            self.produtos.remove(produto)

    def __str__(self):
        return f"Estoque ({len(self.produtos)} produtos)"

class Pedido(String):
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

    def __str__(self):
        return f"Pedido em {self.data} - Total: R${self.valorTotal:.2f}"

class SistemaVendas(String):
    def __init__(self):
        self.__usuarios = []
        self.estoques = []
        self.pedidos = []
        
    def get_usuarios(self):
        return self.__usuarios

    def get_estoques(self):
        return self._estoques

    def get_pedidos(self):
        return self._pedidos
    

    def adicionarProduto(self, produto):
        if self.estoques:  # Ajuste aqui
            # Adiciona o produto ao primeiro estoque existente (pode ser adaptado conforme a lógica desejada)
            self.estoques[0].adicionarProduto(produto)
            print("Produto adicionado ao estoque.")
        else:
            print("Nenhum estoque disponível para adicionar o produto.")

    def autenticarUsuario(self, email, senha):
        for usuario in self.__usuarios:
            if usuario.autenticar(email, senha):
                return True
        return False

    def calcularFrete(self, produtos_pedido):
        quantidade_produtos = len(produtos_pedido)

        if quantidade_produtos == 1:
            return 10.0
        elif quantidade_produtos >= 3:
            return 25.0
        else:
            return 0.0

    def adicionarUsuario(self, usuario):
        self.__usuarios.append(usuario)

    def removerUsuario(self, usuario):
        if usuario in self.__usuarios:
            self.__usuarios.remove(usuario)

    def adicionarEstoque(self, estoque):
        self.estoques.append(estoque)

    def removerEstoque(self, estoque):
        if estoque in self.estoques:
            self.estoques.remove(estoque)

    def realizarPedido(self, email_usuario, produtos_pedido):
        # Verificar se o usuário existe
        usuario_existente = None
        for usuario in self.__usuarios:
            if usuario.email == email_usuario:
                usuario_existente = usuario
                break

        if not usuario_existente:
            print("Usuário não encontrado.")
            return

        # Criar um novo pedido
        novo_pedido = Pedido()
        
        # Adicionar produtos ao pedido
        for produto in produtos_pedido:
            novo_pedido.adicionarProduto(produto)

        # Calcular frete
        frete = self.calcularFrete(produtos_pedido)
        print(f"Frete: R${frete:.2f}")

        # Adicionar frete ao valor total do pedido
        novo_pedido.valorTotal += frete

        # Adicionar o pedido à lista de pedidos do sistema
        self.pedidos.append(novo_pedido)
        print(f"Pedido realizado com sucesso! Valor total: R${novo_pedido.valorTotal:.2f}")

    def __str__(self):
        return f"Sistema de Vendas ({len(self.__usuarios)} usuários, {len(self.estoques)} estoques, {len(self.pedidos)} pedidos)"
