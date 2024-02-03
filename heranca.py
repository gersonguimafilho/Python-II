#primeira classe com herança

class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        

    def falar (self):
        print(f"O {self.nome} está falando!")

class Cachorro (Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca
    def latir(self):
        print(f"O {self.nome} está latindo!") 


class Gato (Animal):
    def __init__(self, nome, idade, raca, som):
        super().__init__(nome, idade)
        self.raca = raca
        self.som = som

    
pet = Cachorro("Alfie", 2, "Pinscher")
pet2 = Gato ("Xaninho", 6, "persa", "mia")

print(pet.nome)
print(pet.idade)
pet.latir()
pet.falar()

print(pet2.nome)
print(pet2.idade)
print(pet2.som)

