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
    def autenticar(usuario, loginDigitado, senhaDigitado):
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

    def autenticar(usuario, senhaDigitado, loginDigitado):
        return usuario.autenticar(usuario, senhaDigitado, loginDigitado)

    