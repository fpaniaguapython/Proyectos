def saludar(nombre):
    print("Buenos días, soy", nombre)

def trabajar(nombre):
    print("Soy",nombre," y estoy trabajando...")

def despedir(nombre):
    print("Hasta mañana, soy", nombre)

pila_tareas = (saludar, trabajar, despedir)

for tarea in pila_tareas:
    tarea("Claudia")