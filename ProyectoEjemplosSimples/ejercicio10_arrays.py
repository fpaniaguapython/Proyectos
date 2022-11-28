import array #Importar todo de array (Opción 1)
#from array import array#Importamos array de la biblioteca array (Opción 2)

numeros = array.array('i', [3,8,10,18,38,100])#Opción 1
#numeros = array('i', [3,8,10,18,38,100])#Opción 2
print(type(numeros))#class array.array
print(numeros)
print(type(numeros[0]))#class int
print(numeros[0])