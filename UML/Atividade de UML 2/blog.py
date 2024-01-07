from datetime import datetime

class Blog:
    def __init__(self):
        self.__postagens = []

    def adicionarPostagem(self, postagem):
        if postagem.getUsuario().autenticar():
            self.__postagens.append(postagem)
            print("Postagem adicionada com sucesso!")
        else:
            print("Usuário não autenticado. Não é possível adicionar a postagem.")

    def publicarPostagem(self, postagem):
        if postagem in self.__postagens:
            postagem.setDataPublicacao(datetime.now())
            print("Postagem publicada com sucesso!")
        else:
            print("Postagem não encontrada. Não é possível publicar.")

    def listarPostagensPublicadas(self):
        for postagem in self.__postagens:
            if postagem.getDataPublicacao():
                print(f"ID: {postagem.getId()}, Título: {postagem.getTitulo()}, Data de Publicação: {postagem.getDataPublicacao()}")

    def listarTodasAsPostagens(self):
        for postagem in self.__postagens:
            print(f"ID: {postagem.getId()}, Título: {postagem.getTitulo()}, Data de Criação: {postagem.getDataCriacao()}")

    def apagarPostagem(self, postagem):
        if postagem in self.__postagens:
            self.__postagens.remove(postagem)
            print("Postagem removida com sucesso!")
        else:
            print("Postagem não encontrada. Não é possível remover.")

class Postagem:
    def __init__(self, id, titulo, texto, usuario) -> None:
        self.__id = id
        self.__titulo = titulo 
        self.__texto = texto
        self.__dataCriacao = datetime.now()
        self.__dataPublicacao = None
        self.__usuario = usuario

    def getId(self):
        return self.__id
    
    def getTitulo(self):
        return self.__titulo
    
    def getTexto(self):
        return self.__texto
    
    def getDataCriacao(self):
        return self.__dataCriacao
    
    def getDataPublicacao(self):
        return self.__dataPublicacao
    
    def setDataPublicacao(self, data):
        self.__dataPublicacao = data
    
    def getUsuario(self):
        return self.__usuario

class MixinAutenticavel: 
    def autenticar(self, usuario, loginDigitado, senhaDigitado):
        if usuario.getLogin() == loginDigitado and usuario.getLogin() == senhaDigitado:
            return True
        else:
            return False

class Usuario(MixinAutenticavel): 
    def __init__(self, id, nome, login, senha) -> None:
        self.__id = id
        self.__nome = nome
        self.__login = login 
        self.__senha = senha

    def getId(self):
        return self.__id
    
    def getLogin(self):
        return self.__login
    
    def getSenha(self):
        return self.__senha

class SistemaBlog: 
    def __init__(self, blog):
        self.__blog = blog

    def autenticar(self, usuario, senhaDigitada, loginDigitado):
        return usuario.autenticar(senhaDigitada, loginDigitado)


### Questão 2 
    
class Pedido:
    def __init__(self):
        self.__itemPedidos = []
        self.__valorTotal = 0

    def adicionarItem(self, item):
        self.__itemPedidos.append(item)

    def obterTotal(self):
        for item in self.__itemPedidos:
            self.__valorTotal += item.getProduto().getValor() * item.getQuantidade()
        return self.__valorTotal

class ItemPedido:
    def __init__(self, produto, quantidade):
        self.__produto = produto
        self.__quantidade = quantidade

    def getProduto(self):
        return self.__produto

    def getQuantidade(self):
        return self.__quantidade

class Produto:
    def __init__(self, codigo, valor, descricao):
        self.__codigo = codigo
        self.__valor = valor
        self.__descricao = descricao

    def getCodigo(self):
        return self.__codigo

    def getValor(self):
        return self.__valor

    def getDescricao(self):
        return self.__descricao

