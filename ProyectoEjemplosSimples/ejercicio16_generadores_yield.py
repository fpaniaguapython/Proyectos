import random
def procesar_item(item):
    print("Procesando item...", item)

NUMERO_NUMEROS = 100
#SIN yield
#Se construye una lista con todos los elementos
def get_numeros():
    i = 0
    numeros = []
    while i<NUMERO_NUMEROS:
        numeros.append(random.random())
        i+=1 
    return numeros

numeros = get_numeros()
for numero in numeros:
    procesar_item(numero)

#CON yield (generador)
#Sólo hay un elemento en memoria por cada iteracción
def get_numeros():
    i = 0
    while i<NUMERO_NUMEROS:
        yield(random.random())
        i+=1

for numero in get_numeros():
    procesar_item(numero)
