from Animal import Animal
from IReproductor import IReproductor

class Mamifero(Animal, IReproductor):
    def __init__(self, nombre, numero_patas) -> None:
        super().__init__(nombre)
        self.numero_patas = numero_patas

    def dormir(self):
        print("Mamífero durmiendo...")

    def reproducirse(self):
        print("Mamífero reproduciéndose...")

    def __add__(self, o):
        return self.numero_patas + o.numero_patas

    def __str__(self) -> str:
        return "NOMBRE:"+self.nombre

    #Análogo a __str__
    def __repr__(self) -> str:
        return "NOMBRE:"+self.nombre

    def __eq__(self, __o: object) -> bool:
        return self.numero_patas == __o.numero_patas

    def __lt__(self, o):
        print("Dentro de __lt__")
        return self.numero_patas < o.numero_patas
