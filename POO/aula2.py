class Usuario: 
    cargo = 'usuario'
    
    def __init__(self, nome, idade, altura):
        self.altura = altura
        
    @classmethod
    def cargo_usuario(cls):
        cls.cargo = "Gerente"
        print(cls.cargo)
        
    @staticmethod
    def e_adulto(idade):
        if idade >= 18: 
            print("É adulto")
        else:
            print("Não é adulto")
        
        
Usuario.cargo_usuario()
Usuario.e_adulto(20)
Usuario.e_adulto(12)