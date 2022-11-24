"""
  _      _____  _____ _______        _____ 
 | |    |_   _|/ ____|__   __|/\    / ____|
 | |      | | | (___    | |  /  \  | (___  
 | |      | |  \___ \   | | / /\ \  \___ \ 
 | |____ _| |_ ____) |  | |/ ____ \ ____) |
 |______|_____|_____/   |_/_/    \_\_____/ 

"""



lista = ["Lunes","Martes","Miércoles","Juebes","Viernes","Sábado","Domingo"] #Declaración

print(lista) #Mostrar la lista completa

#Mostrar con un for
for dia in lista:
    print(dia)

lista[3]="Jueves"#Acceso por posición
print(lista[3])#Acceso por posición

#Admite slice
print(lista[:5]) #Días de diario
print(lista[::2]) #Desde el princio hasta el final con un step=2

#lista[8]="Saturday"#Produce un error al estar fuera de rango
#print(lista[8])#Produce un error al estar fuera de rango

print(lista[-1])#Admite posicionamiento negativo (empieza por el final)

del lista[-2:]#Borrar desde el 'viernes' hasta el final
print(lista)

lista.append("Domingo")#Agregar al final de la lista
lista.append("Sábado")
print(lista)

lista[-2],lista[-1]=lista[-1],lista[-2]
print(lista)

print('Martes' in lista) #Operador in
print('Juebes' not in lista) #Operador not in

lista.insert(1,"LunesMartes")#Insertar en una posición
print(lista)

lista.remove("LunesMartes")#Eliminar de una posición
print(lista)

lista.sort()#Ordenar
print(lista)
lista.reverse()#Invertir el orden
print(lista)

lista_extra = ['Postsábado','Postdomingo']
lista.extend(lista_extra) #Añadir una lista al final de otra
print(lista)
lista = lista + lista_extra #'Concatenación' de listas
print(lista)

#Restauramos los días de la semana normales
lista = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]

print(lista.index("Jueves"))#Indica la posición de un elemento

print(lista.count("Jueves"))#Indica el número de veces que aparece un elemento
lista.append("Jueves")
print(lista.count("Jueves"))#Indica el número de veces que aparece un elemento

#Eliminamos el último jueves
del lista[-1:]
print(lista)

lista.append("Jueves")

#Eliminamos el último jueves
lista = lista[0:-1]
print(lista)

#¡PELIGRO! El operador = asigna referencia en estructuras de datos=>'Asignación por referencia'
cesta=["Leche","Huevo","Puerro"]
micesta = cesta
micesta.append("Gaseosa")
print(cesta)

#El slicing crea un nuevo objeto=>'Asignación por valor'
cesta=["Leche","Huevo","Puerro"]
micesta = cesta[:]
micesta.append("Gaseosa")
print(cesta)

l1 = ["one","two","three"]
l2 = ["uno","dos","tres",l1]
print(l2[3][1])#Debe mostrar 'two'

instrucciones = """
1. Crear una lista con 10 números entre el 1 y el 10
2. Con un bucle for, recorrer la lista y modificar cada elemento multiplicado por 2
3. Con otro bucle mostrar el resultado:
    5#8#7#3
"""
numeros = [1,3,7,4,8,2,4,8,1,5]

for i in range(0,len(numeros)):
    numeros[i]=numeros[i]*2

for numero in numeros:
    print(numero,end="#")
print()

# COMPRENSIÓN DE LISTAS (list comprenhension)

#Forma 'tradicional'
numeros=[]
for numero in range(10):
    numeros.append(numero)
print("MÉTODO 'TRADICIONAL':",numeros)


#Forma 'comprensión de listas'
numeros = [numero for numero in range(10)]
print("MÉTODO 'LIST COMPRENHENSION':",numeros)

#Construcción de lista de 0-9 * 2
numeros = [numero*2 for numero in range(10)]
print(numeros)

def triple(numero):
    return numero*3

#Construcción de lista de 0-9 * 2
numeros = [triple(numero) for numero in range(10)]
print(numeros)

"""
Dada esta lista:
cesta=["Leche","Huevo","Puerro"]
Crear una nueva lista con 'list comprehension' con los elementos de la cesta convertidos a Mayúsculas.
"""
cesta=["Leche","Huevo","Puerro"]
cesta_mayusculas = [producto.upper() for producto in cesta]
print(cesta_mayusculas)

"""
Dada esta lista:
cesta=["Pizza","Salchichas","Leche","Apio","Huevo","Puerro","Cerveza","Vino"]
elementos_insalubles = ["Cerveza","Vino","Pizza","Salchichas"]
Crear una nueva lista con 'list comprehension' con los elementos de la cesta sustituyendo los 
que no son saludables por "Brócoli"
"""
cesta=["Pizza","Salchichas","Leche","Apio","Huevo","Puerro","Cerveza","Vino"]
elementos_insalubles=["Cerveza","Vino","Pizza","Salchichas"]

def filtrar_producto(producto):
    if producto in elementos_insalubles:
        return "BRÓCOLI"
    return producto
    #Expresión ternaria
    #return "BRÓCOLI" if producto in elementos_insalubles else producto

lista_compra = [filtrar_producto(elemento) for elemento in cesta]
print(lista_compra)

"""
Ejemplo de uso de comprensión de listas
"""
class Cliente:
    pass

def obtenerClientesMorosos(saldo):
    if saldo<0:
        return Cliente()
    else:
        None

saldos = [3,-3,8,9,-15,-24,-100]
#Creamos una lista de 'morosos' compuesta por instancias de la clase Cliente
morosos = [obtenerClientesMorosos(saldo) for saldo in saldos]
print(morosos)
print(type(morosos[1]))

# (List comprehension) Condicionamiento de los elementos que entran en la lista 
rango = range(0,100)
numeros = [numero for numero in rango if numero%2==0]
print(numeros)

"""
Dada esta lista:
cesta=["Pizza","Salchichas","Leche","Apio","Huevo","Puerro","Cerveza","Vino"]
elementos_insalubles = ["Cerveza","Vino","Pizza","Salchichas"]
Crear una nueva lista con 'list comprehension' sin los elementos que no son saludables
"""
cesta=["Pizza","Salchichas","Leche","Apio","Huevo","Puerro","Cerveza","Vino"]
elementos_insalubles=["Cerveza","Vino","Pizza","Salchichas"]

#Alternativa compacta
cesta_saludable = [producto for producto in cesta if (producto not in elementos_insalubles)]
print(cesta_saludable)

#Alternativa mediante función
def isSaludable(producto):
    return producto not in elementos_insalubles

cesta_saludable = [producto for producto in cesta if isSaludable(producto)]
print("CESTA DESDE COMPRENSIÓN DE LISTAS:", cesta_saludable)

#Alternativa 'tradicional'
cesta_saludable=[]
for producto in cesta:
    if isSaludable(producto):
        cesta_saludable.append(producto)
print("CESTA DESDE MÉTODO TRADICIONAL:" , cesta_saludable)

#Comprensión con listas con if y con valor por defecto
cesta_saludable = [producto if isSaludable(producto) else "PROHIBIDO" for producto in cesta]
print("CESTA NORMAL:",cesta)
print("CESTA SALUDABLE:", cesta_saludable)

"""
  _______ _    _ _____  _                _____ 
 |__   __| |  | |  __ \| |        /\    / ____|
    | |  | |  | | |__) | |       /  \  | (___  
    | |  | |  | |  ___/| |      / /\ \  \___ \ 
    | |  | |__| | |    | |____ / ____ \ ____) |
    |_|   \____/|_|    |______/_/    \_\_____/ 
"""

tupla = ()#Tupla vacía
print("TUPLA:", tupla, type(tupla))
tupla = (5)#Declaración e inicialización ERRÓNEO
print("TUPLA:" , tupla, type(tupla))
tupla = (5,) #Declaración e inicialización CORRECTO
print("TUPLA:" , tupla, type(tupla))
tupla = (5,"Python",cesta)#Declaración e inicialización
print(tupla[0])#Acceso por posición
#tupla[0]=8#Error
for item in tupla:
    print(item)

tcesta = tuple(cesta) #Conversión de lista en tupla
lcesta = list(tcesta) #Conversión de tupla a lista
print("RESULTADO DE LA CONVERSIÓN:", tcesta)    

#Admite slicing
print(tupla[0:1])

#Operadores + y * (copia varias veces la tupla)
tupla2 = (1,5)
tupla3 = tupla + tupla2
print("Tupla 3:", tupla3)

#Aplicaciones funciones built-in
tupla = (3,10,-5,8,105,1)
print(len(tupla))
print(min(tupla))
print(max(tupla))
print(3 in tupla)

"""
   _____ ______ _______ 
  / ____|  ____|__   __|
 | (___ | |__     | |   
  \___ \|  __|    | |   
  ____) | |____   | |   
 |_____/|______|  |_|   
                        
"""
frutas_invierno = {"Naranja","Limón","Pomelo","Mandarina","Manzana","Plátano","Uva"}
frutas_verano = {"Sandía","Melón","Higo","Melocotón","Albaricoque","Plátano","Uva"}

#Se puede transforma de set a list y a tupla y viceversa.
#Admite operadores in, not in
#Admite las funciones max y min

#Métodos exclusivos propios de los conjuntos

#isdisjoint()--> Devuelve true/false
print(frutas_invierno.isdisjoint(frutas_verano))#Comprueba si son conjuntos disjuntos

palabras_prohibidas = {"Jamón","Melón","Pingüino"}
conjunto_palabras = set("A mi Pingüino no le gusta el Melón".split())
if (not palabras_prohibidas.isdisjoint(conjunto_palabras)):
    print("No puedes decir eso")
else:
    print("OK")
conjunto_palabras = set("A mi perro le gustan las albóndigas".split())
if (not palabras_prohibidas.isdisjoint(conjunto_palabras)):
    print("No puedes decir eso")
else:
    print("OK")

#intersection()-->Devuelve los elementos comunes. No importa el orden
frutas_anuales = frutas_invierno.intersection(frutas_verano)
print(frutas_anuales)

#difference()-->Elementos que están en un conjunto en el otro. Importa el orden.
dif1 = frutas_invierno.difference(frutas_verano)
dif2 = frutas_verano.difference(frutas_invierno)
print(dif1)
print(dif2)

#Ejercicio: construir una interfaz en lenguaje natural dadas las siguientes opciones
"""
def mostrarHora():
    print("Son las 10 de la mañana")
def mostrarTemperatura():
    print("Hace 10 grados centígrados")
def mostrarHoraPartido():
    print("España juega a las 11")

opcion1 = ({"dime","dame","hora","la"},mostrarHora)
opcion2 = ({"dime","que","temperatura","hace"},mostrarTemperatura)
opcion3 = ({"hora","juega","partido","españa"},mostrarHoraPartido)

opciones = [opcion1, opcion2, opcion3]

orden = input("Soy soy Halesa, dime qué deseas saber:")
set_orden = set(orden.split())
opcion_mas_proxima = ({},)
for current_opcion in opciones:
    if len(set_orden.intersection(current_opcion[0]))>len(set_orden.intersection(opcion_mas_proxima[0])):
        opcion_mas_proxima=current_opcion

opcion_mas_proxima[1]()
"""

"""
  _____ _____ _____ _____ _____ ____  _   _          _____  _____ ____  
 |  __ \_   _/ ____/ ____|_   _/ __ \| \ | |   /\   |  __ \|_   _/ __ \ 
 | |  | || || |   | |      | || |  | |  \| |  /  \  | |__) | | || |  | |
 | |  | || || |   | |      | || |  | | . ` | / /\ \ |  _  /  | || |  | |
 | |__| || || |___| |____ _| || |__| | |\  |/ ____ \| | \ \ _| || |__| |
 |_____/_____\_____\_____|_____\____/|_| \_/_/    \_\_|  \_\_____\____/ 

"""
#key - value
#Construcción
diccionario = {}
diccionario = dict()
diccionario = {4:"Pan",2:"Azúcar",'arroz':"Arroz"}
diccionario = dict([(4,"Pan"),(2,"Azúcar"),(3,"Arroz")])

diccionario = {4:"Pan",2:"Azúcar",'arroz':"Arroz"}

#Acceso de lectura y de modificación
print(diccionario[4])
print(diccionario["arroz"])
#print(diccionario['patata'])#Error al no existir la clave
print("Patata:", diccionario.get('patata'))#Si no existe, devuelve

diccionario[4]="Bread" #Modificación

#Agregación de nuevos elementos
diccionario[5]="Lechuga"
print(diccionario)
#El método setDefault agrega el elemento si la clave no existe previamente 
diccionario.setdefault(6,"Refresco")
print(diccionario)
diccionario[6]="Gaseosa"
print(diccionario)
diccionario.setdefault(6,"Zumo de naranja")#No agrega elemento por que 6 existe
print(diccionario)

#Eliminar elementos del diccionario
del diccionario[6]
print(diccionario)

#Método pop, devuelve y elimina del diccionario un item
item = diccionario.pop("arroz")
print("Item devuelto por el pop:", item)
print(diccionario)

#Método popitem devuelve el último elemento del diccionario y lo elimina
item = diccionario.popitem()

#Las funciones list, tuple y set obtienen dichas estructuras formadas por las claves
list(diccionario)
list(diccionario.values())#Lista con los valores
list(diccionario.items())#Lista de tuplas con las claves y valores
set(diccionario)
tuple(diccionario)

#Admite los operadores in y not in
print(diccionario)
print("arroz" in diccionario)
print(4 in diccionario)

#Métodos de acceso a las partes: keys(), values(), items()
diccionario = {4:"Pan",2:"Azúcar",'arroz':"Arroz"}

diccionario.keys()
diccionario.values()
diccionario.items()

print("***CLAVES***")
for k in diccionario.keys():
    print(k)
print("***VALUES***")
for v in diccionario.values():
    print(v)
print("***ITEMS***")
for k,v in diccionario.items():
    print(k,v,sep="---")

#Método clear --> Borra el diccionario
diccionario.clear()
print("Diccionario vacío:",diccionario)
diccionario = {4:"Pan",2:"Azúcar",'arroz':"Arroz"}



