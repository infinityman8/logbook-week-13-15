class Animal():
    def __init__(self,types,name):
        self.types=types
        self.name=name

    def getAnimalString(self):
        return "animal name: %s, type: %s" %(self.name, self.types)
        
class Mammal(Animal):
    def __init__(self, species, name):
        super().__init__("mammal", name) 
        self.species = species

class Insect(Animal):
    def __init__(self, species, name):
        super().__init__("insect", name)
        self.species = species

    def getAnimalString(self):
        result = super().getAnimalString()
        return "%s, animal species: %s" %(result, self.species)


mammal1 = Mammal("dog", "Alsatian")
insect1 = Insect("bee", "bummble bee")

print(mammal1.getAnimalString())
print(insect1.getAnimalString())
