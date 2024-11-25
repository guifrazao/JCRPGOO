'''
2. Implemente o diagrama de classes abaixo:
'''

class Animal:
    def __init__(self, name, breed = None):
        self.name = name
        self.breed = breed # raça

    def walk(self):
        return f"{self.name} está andando."

class Dog(Animal):
    def barks(self):
        return f"{self.name} está latindo."
    
    def walk(self):
        return f"{self.name} está correndo"

class Cat(Animal):
    def meow(self):
        return f"{self.name} está miando."
    
    def walk(self):
        return f"{self.name} está passeando"

