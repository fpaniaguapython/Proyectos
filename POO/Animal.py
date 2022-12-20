from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.alimento = 0

    @abstractmethod
    def dormir(self):
        pass

    def alimentar(self, unidades):
        print("Alimentando al animal")
        self.alimento+=unidades