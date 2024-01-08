class Usuario: 
    cargo = 'usuario'
    
    def __init__(self, nome, idade, altura):
        self.altura = altura
        
    def exibe_altura(self):
        print(self.altura)
        
    def exibe_cargo(cls):
        print(cls.cargo)       
        
usuario1 = Usuario('Caio', '21', '180')
usuario2 = Usuario('Lwkas', '19', '162')

usuario2.exibe_altura()
usuario2.exibe_cargo()




