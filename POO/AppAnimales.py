from Mamifero import Mamifero
from Animal import Animal

if __name__=="__main__":
    pulgas = Mamifero("Perro",4)
    pulgas.alimentar(10)
    pulgas.dormir()
    pulgas.reproducirse()

    #animal = Animal("animal") --> Al ser animal una clase abstracta no se puede instanciar

    ramon = Mamifero("Humano",2)
    print(ramon+pulgas)
    print(ramon)
    print(ramon==pulgas)
    print(ramon<pulgas)
    
    tripode = Mamifero("tripode",3)

    animales = [pulgas, ramon, tripode]
    print(animales)
    animales_ordenados = sorted(animales)#Obtener una lista modificada mediante función
    print(animales_ordenados)
    animales.sort()#Ordenar la lista mediante método modificando la lista
    print(animales)

#Métodos isinstance e issubclass para determinar relaciones entre clase