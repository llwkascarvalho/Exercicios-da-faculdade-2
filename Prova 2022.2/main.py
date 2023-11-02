class Person: 

    def __init__(self, name, age):
        self.name = name
        if age >= 1 and age <=150:
            self.age = age
        else:
            raise ValueError("A idade deve estar entre [1, 150]")
        
    def __str__(self):
        return f"{self.name} ({self.age})"
    

#Questão 2:



