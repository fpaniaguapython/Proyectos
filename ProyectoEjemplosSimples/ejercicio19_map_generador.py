#Dado este código:
#Eliminar los saltos de línea utilizando la función map
fichero = open("nombres-propios-es.txt","r",encoding="utf-8")
nombres = fichero.readlines()
#print(nombres)
fichero.close()

#Solución 1 - Versión Alfredo
def eliminar_salto_linea_rstrip(texto):
    return texto.rstrip()
nombres_limpios_rstrip = tuple(map(eliminar_salto_linea_rstrip,nombres))
print(nombres_limpios_rstrip)

#Solución 2 - Versión César
def eliminar_salto_linea_slicing(texto):
    return texto[:-1]
nombres_limpios_slicing = tuple(map(eliminar_salto_linea_slicing,nombres))
print(nombres_limpios_slicing)

#Solución 3 - Versión Isabel
def eliminar_salto_linea_replace(texto):
    return texto.replace("\n","")
nombres_limpios_replace = tuple(map(eliminar_salto_linea_replace,nombres))
print(nombres_limpios_replace)

#Resolver el ejercicio UTILIZANDO GENERADORES
def get_nombres():
    nombres = []
    fichero = open("nombres-propios-es.txt","r",encoding="utf-8")
    while (nombre := fichero.readline()):
        nombres.append(nombre)
    fichero.close()
    return nombres

def get_nombres_generador():
    fichero = open("nombres-propios-es.txt","r",encoding="utf-8")
    while (nombre := fichero.readline()):
        yield nombre
    fichero.close()
    
for nombre in get_nombres_generador():
    print(eliminar_salto_linea_rstrip(nombre),end=":")