class Animal:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
    def is_mamifero(self):
        return self.tipo=="Mamífero"
    def __str__(self) -> str:
        return "Nombre:"+self.nombre+". Tipo:"+self.tipo

gato = Animal("Tom","Mamífero")
raton = Animal("Jerry","Mamífero")
python = Animal("Kaa","Reptil")

animales = [gato, raton, python]

#Mostrar por pantalla, utilizando filter y funciones lambda, los anímales que son mamíferos
#Sólo con filter
print("SÓLO CON FILTER")
mamiferos = list(filter(Animal.is_mamifero, animales))
for mamifero in mamiferos:
    print(mamifero)

#Con filter y lambda (uso forzado)
print("CON FILTER Y LAMBDA")
reptiles = list(filter(lambda animal: animal.tipo=="Reptil", animales))
for reptil in reptiles:
    print(reptil)

#Con filter y lambda (versión Isabel)
print("CON FILTER Y LAMBDA APROVECHANDO EL MÉTODO EXISTENTE")
mamiferos = list(filter(lambda animal: animal.is_mamifero(), animales))
for mamifero in mamiferos:
    print(mamifero)

#Con filterm, map y lambda (versión locura)
mamiferos = list(map(lambda animal: "\n**Nombre:"+animal.nombre+"\n"+"**Tipo:"+animal.tipo, list(filter(lambda animal: animal.is_mamifero(), animales))))

for mamifero in mamiferos:
    print(mamifero)

