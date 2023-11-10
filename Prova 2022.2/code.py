from enum import Enum

# Classe Person
class Person:
    def __init__(self, name, age):
        self.name = name
        if 1 <= age <= 150:
            self.age = age
        else:
            raise ValueError("A idade deve estar no intervalo [1, 150]")

    def __str__(self):
        return f"{self.name}({self.age})"

# Classe Hobby
class Hobby(Enum):
    MUSIC = 1
    SPORTS = 2
    GAMES = 3

# Classe Friend
class Friend(Person):
    def __init__(self, name, age, hobby):
        super().__init__(name, age)
        self.hobby = hobby

    def chill(self):
        return f"{self.name} is chilling."

    def play(self, friends):
        if not friends:
            return f"Jogando {self.hobby};"
        elif len(friends) == 1:
            return f"Jogando {self.hobby} com {friends[0]};"
        elif len(friends) == 2:
            return f"Jogando {self.hobby} com {friends[0]} e {friends[1]};"
        else:
            other_friends = ', '.join(friends[:-1])
            return f"Jogando {self.hobby} com {other_friends}, e {friends[-1]}"

    def __str__(self):
        return super().__str__() + f" {self.hobby}"

# Interface Nuisance
class Nuisance:
    def annoy(self):
        pass

# Classe Telemarketing
class Telemarketing(Person, Nuisance):
    def __init__(self, name, age, hobby):
        super().__init__(name, age)
        self.hobby = hobby

    def giveSalesPitch(self):
        return f"{self.name} pressiona os outros a comprar coisas."

    def annoy(self):
        return f"{self.name} irrita ao dar um discurso de vendas."

# Classe Insect
class Insect:
    def __init__(self, species):
        self.species = species

    def __str__(self):
        return f"Insect: {self.species}"

# Classe Mosquito
class Mosquito(Insect, Nuisance):
    def buzz(self):
        return f"{self.species} buzzing around."

    def annoy(self):
        return "buzz buzz buzz"

# Classe Butterfly
class Butterfly(Insect):
    def __init__(self, species, colors, butterfly=None):
        super().__init__(species)
        if butterfly:
            self.colors = butterfly.colors
        else:
            self.colors = colors

    def __str__(self):
        color_str = ', '.join(self.colors)
        return f"{self.species}[{color_str}]"