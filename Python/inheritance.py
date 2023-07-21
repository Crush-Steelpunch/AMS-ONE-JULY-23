from abc import ABC, abstractclassmethod



class Animals(ABC):
    
    def __init__(self, legs, species, climate, noise):
        self.legs = legs
        self.species = species
        self.climate = climate
        self.noise = noise
    
    def makenoise(self):
        return self.noise
    
    @abstractclassmethod
    def eating():
        pass




class Dog(Animals):
     def eating(self,food):
        return "FullDog"

Spot = Dog(4,"Dog","temperate","Woof")

print(Spot.makenoise())

class tigers(Animals):
    def __init__(self, climate, noise, legs=4, species="tiger"):
        self.legs = legs
        self.species = species
        self.climate = climate
        self.noise = noise

    def eating(self,tigerfood):
        return "Fulltiger"

sherkhan = tigers("hot","rowr")
print(sherkhan.makenoise())
