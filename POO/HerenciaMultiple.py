class Ummita:
    def saludar(self):
        print("Hola, soy del planeta Ummo")

class Padre(Ummita):
    def __init__(self) -> None:
        print("En el constructor de Padre")
        self.nombre = "Papá"
    def saludar(self):
        print("Hola, soy tu padre")

class Madre(Ummita):
    def __init__(self) -> None:
        print("En el constructor de Madre")
        self.name = "Mamá"
    def saludar(self):
        print("Hola, soy tu madre",self.name)
    def despedir(self):
        print("Adios, soy tu madre")

class Hijo(Padre, Madre):
    def __init__(self) -> None:
        Padre.__init__(self)#Llamada explícita a los constructores de las clases padres
        Madre.__init__(self)#Llamada explícita a los constructores de las clases padres
    """
    #Método saludar forzando a que se ejecute la implementación de uno de las clases base
    def saludar(self):
        Madre.saludar(self)#Forzando a utilizar el de la madre
    """
hijo = Hijo()
print(hijo.nombre)
print(hijo.name)
hijo.saludar()
hijo.despedir()

