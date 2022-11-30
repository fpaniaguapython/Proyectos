#Importación de funciones Tipo 1 
#import ejercicio15_modulo_externo
#ejercicio15_modulo_externo.core_funcion1()

#Importación de funciones Tipo 2 
from ejercicio15_modulo_externo import core_funcion2
def funcion2():
    print("Función 2 nueva")

funcion2()
core_funcion2()