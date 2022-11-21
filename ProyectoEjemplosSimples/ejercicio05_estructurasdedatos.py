
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
print(cesta_saludable)