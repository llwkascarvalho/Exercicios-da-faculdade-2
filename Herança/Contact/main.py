class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email 
        Contact.all_contacts.append(self)

class Supplier(Contact):
    def order(self, pedido):
        print("Pedido para '{}': "
            "'{}'".format(self.name, pedido))


c1 = Contact('Lwkas', 'lwkas@gmail.com')
f1 = Supplier('Sorveteria 3 irmãos', 'sorveteria3irmaos@gmail.com')

print(c1.name, c1.email)
print(f1.name, f1.email)

f1.order('Milk shake')