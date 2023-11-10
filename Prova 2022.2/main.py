from code import Person, Hobby, Friend, Telemarketing, Mosquito, Butterfly


person1 = Person("Alice", 25)
friend1 = Friend("Bob", 30, Hobby.GAMES)
friend2 = Friend("Charlie", 28, Hobby.SPORTS)

print(person1)
print(friend1)
print(friend1.chill())
print(friend2.play([friend1]))
print(friend2.play([friend1, friend2]))

telemarketer = Telemarketing("SalesPerson", 35, Hobby.MUSIC)
print(telemarketer.giveSalesPitch())
print(telemarketer.annoy())

mosquito = Mosquito("Culex tarsalis")
print(mosquito.buzz())
print(mosquito.annoy())

butterfly1 = Butterfly("Morpho", ["azul"])
butterfly2 = Butterfly("Phoebis", [], butterfly1)
print(butterfly1)
print(butterfly2)
