cadena = "esta cadena no sirve para hacer pruebas, para entretenerse"

cadena_con_separador = "Esta línea \n está en dos líneas"

cadena_multilinea = """Esta es la línea 1
Esta es la línea 2
Esta es la línea 3
"""

print(len(cadena))#Función built-in - Proprorcina la longitud de la cadena

print("patata" in cadena)#Saber si existe una subcadena en una cadena

print(cadena.capitalize())#Convierte la primera letra a mayúsculas
print(cadena.count("ar"))#Cuenta el número de ocurrencias de una cadena
print("INDEX:", cadena.index("ar"))#Obtiene la primera posición de la subcadena (o genera un ValueError)
print("FIND:", cadena.find("x"))#Obtiene la primera posición de la subcadena (o devuelve -1)
print(cadena.startswith("esta"))#Indica si empieza por una subcadena
print(cadena.endswith("esta"))#Indica si termina por una subcadena
#Otros métodos isdigit(),islower(),isupper()
espacios = "             "
print("¿Son espacios?",espacios.isspace())#Determina si todos los caracteres son espacios
#Otros métodos lower(),upper()
print(cadena.replace("a","*"))#Sustitución de una subcadena por otra
print(cadena.split())#Crea una lista con las palabras del texto
print(cadena.split(","))#Crea una lista con las palabras del texto, indicando separador
print(cadena_multilinea.splitlines())#Crea una lista con las líneas de un texto
print(cadena_con_separador.splitlines())#Crea una lista con las líneas de un texto

postres=["Flan","Yogur","Fresas"]
print("".join(postres))#Genera un strin con la concatenación de los string de la lista postres


