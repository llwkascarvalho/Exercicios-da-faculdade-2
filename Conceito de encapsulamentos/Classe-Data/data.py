import datetime

data = datetime.date.today()
dataFormatada = data.strftime('%d/%m/%Y')
print(dataFormatada)

class Data:
    def __init__(self):
        self._dia = data.today().day
        self._mes = data.today().month
        self._ano = data.today().year
    
    def get_dia(self):
        return self._dia

    def set_dia(self, nova_data):
        self._dia = nova_data
    
data = Data()
print()