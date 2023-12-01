class Blog:
    def __init__(self, postagens):
        self.__postagens = postagens

    def adicionarPostagem(postagem):
        pass
    def publicarPostagem(postagem):
        pass
    def listarPostagemPublicadas():
        pass
    def listarTodasAsPostagem():
        pass
    def apagarPostagem(postagem):
        pass

class Postagem:
    def __init__(self, id, titulo, texto, dataPublicada, usuario) -> None:
        self.__id = id
        self.__titulo = titulo 
        self.__texto = texto
        self.__data = dataPublicada
        self.__usuario = usuario

        #fazer gets e sets

class MixinAutenticavel: 
    def autenticar(self, usuario, loginDigitado, senhaDigitado):
        if usuario.getLogin() == loginDigitado and usuario.getLogin() == senhaDigitado:
            return True
        else:
            return False

class Usuario(MixinAutenticavel): 
    def ___init__(self, id, nome, login, senha) -> None:
        self.__id = id
        self.__nome = nome
        self.__login = login 
        self.__senha = senha

class SistemaBlog: 
    def ___init__(self, blog):
        self.__blog = blog

    def autenticar(self, usuario, senhaDigitado, loginDigitado):
        return usuario.autenticar(usuario, senhaDigitado, loginDigitado)


### Questão 2 
    
class Pedido: 
    def ___init__(self):
        self.__itemPedidos = []
        self.__valorTotal = 0

    def adicionarItem(self, item):
        self.__itemPedidos.append(item)
    def obterTotal(self):
        pass

class ItemPedido:
    def ___init__(self, produto, quantidade):
        self.__produto = produto
        self.__quantidade = quantidade

class Produto:
    def ___init__(self, codigo, valor, descricao):
        self.__codigo = codigo
        self.__valor = valor
        self.__descricao = descricao

