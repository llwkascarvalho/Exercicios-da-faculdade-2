from datetime import date

class Pessoa:
    def __init__(self, nome, data_nascimento):
        self.nome = nome 
        self.data_nascimento = data_nascimento
        
    def dias_vividos(self):
        return (date.today() - self.data_nascimento).days
    
    @property
    def nome(self):
        return self._nome.title()
    
    @nome.setter
    def nome(self, value):
        self._nome = value
    
    @property
    def data_nascimento(self):
        return self._data_nascimento
    
    @data_nascimento.setter
    def data_nascimento(self, value):
        if not isinstance(value, date):
            raise ValueError('data_nascimento deve ser um objeto do tipo date')
        self._data_nascimento = value
    
p1 = Pessoa('lwkas lwhan gonçalves carvalho', date(2004, 3, 14))
print(f'\nNome: {p1.nome} \nDias vividos: {p1.dias_vividos()}\n')