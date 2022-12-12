from dias import dias

#Lecturas básicas
fichero = open("fichero_datos.txt","r",encoding="utf-8")
datos = fichero.read()#Lee todo el contenido del fichero
print("DATOS LEIDOS:", datos)
#print(fichero.read(3))#Leemos un número de caracteres
#print(fichero.readline())#Leemos una línea (incluye salto de línea)
#print(fichero.readlines())#Leemos todo el fichero y almacena las líneas en una lista (incluye salto de línea)
fichero.close()

#Lectura línea a línea
fichero = open("fichero_datos.txt","r",encoding="utf-8")
while True:
    linea = fichero.readline()
    if linea=="":
        break
    else:
        print("LINEA:", linea.replace("\n",""))
fichero.close()

#Escritura básica
fichero = open("fichero_salida.txt","w", encoding="utf-8")
#fichero.write("Hola")#Escribe el contenido
fichero.writelines(dias)#Escribe el iterable completo, sin saltos de línea
fichero.close()

#Escritura básica - Agregando saltos de línea - Utilizando comprensión de listas
fichero = open("fichero_salida2.txt","w", encoding="utf-8")
#fichero.write("Hola")#Escribe el contenido
dias_salto_linea = [dia+"\n" for dia in dias]
fichero.writelines(dias_salto_linea)#Escribe el iterable completo, con saltos de línea
fichero.close()

#Escritura básica - Agregando saltos de línea - Utilizando map
def agregar_salto_linea(linea):
    return linea+"\n"

fichero = open("fichero_salida3.txt","w", encoding="utf-8")
#fichero.write("Hola")#Escribe el contenido
dias_salto_linea = list(map(agregar_salto_linea, dias))
fichero.writelines(dias_salto_linea)#Escribe el iterable completo, con saltos de línea
fichero.close()

#Apertura en modo append (para evitar truncar el fichero con "w")
fichero = open("fichero_append.txt","a", encoding="utf-8")
fichero.write("Primera escritura")
fichero.close()
fichero = open("fichero_append.txt","a", encoding="utf-8")# "a" concatena la escritura
fichero.write("Segunda escritura escritura")
fichero.close()

#Apertura en modo 'detección de existencia' con 'x'. Si el fichero existe, provoca error.
#fichero = open("fichero_inexistente.txt","x",encoding="utf-8")
#fichero.write("Línea de prueba")
#fichero.close()

#Lectura y escritura (r+, append) (w+, trunca)
#(utilizar conjuntamente con el método seek() de file)
fichero = open("fichero_read_write.txt","r+",encoding="utf-8")
fichero.write("Primera línea")
fichero.write("\n")
fichero.write("Segunda línea")
print("Primera lectura:", fichero.read(5))
print("Segunda lectura:", fichero.read(5))
fichero.close()

#Alternativa a la estructura open-close (realiza automáticamente el close)
with open("fichero_with.txt","w") as fichero:
    fichero.write("El contenido del fichero")
print(fichero.closed)#Closed indica el estado de cierre del fichero

#Excepciones en el manejo de ficheros:
#FileNotFoundError
#IOError
#OSError






