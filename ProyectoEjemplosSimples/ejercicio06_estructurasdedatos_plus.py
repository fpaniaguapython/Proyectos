#Función zip
lista_fechas = ['20221124','20221123','20221122','20221120','20221119']
lista_medidas = [21,20,18,24,41]
#Construcción de una lista y un dicción en modo 'tradicional'
lista_compuesta = []
diccionario_compuesto = {}
for i in range(len(lista_fechas)):
    lista_compuesta.append((lista_fechas[i],lista_medidas[i]))
    diccionario_compuesto.setdefault(lista_fechas[i],lista_medidas[i])
print(lista_compuesta)#Lista de tuplas
print(diccionario_compuesto)#Diccionario
#Construcción de un diccionario mediante la función zip (cuando se hace la conversión del zip, este se borra)
zip_object = zip(lista_fechas, lista_medidas)
lista_compuesta = list(zip_object)
print("Lista creado con zip:", lista_compuesta)
zip_object = zip(lista_fechas, lista_medidas)
diccionario_compuesto = dict(zip_object)
print("Diccionario creado con zip:", diccionario_compuesto)

#Aplicación de la función built-in sorted
#Obtiene una lista (SIEMPRE) con los elementos ordenados
lista = [8,10,81,105,33,1,-8,2000]
print(sorted(lista))
print(sorted(lista, reverse=True))
tupla = (8,10,81,105,33,1,-8,2000)
print(sorted(tupla))
conjunto  = {8,10,81,105,33,1,-8,2000}
print(sorted(conjunto))
diccionario = {'hola': 'hello', 'pan': 'bread', 'trabajo': 'job'}
print(sorted(diccionario))

dias_semana = ["Lunes","Martes","Miércoles","Jueves","Viernes"]
print(sorted(dias_semana))
print(sorted(dias_semana, reverse=True))

def obtener_longitud(dia):
    return len(dia)
print(sorted(dias_semana,key=obtener_longitud))

"""
Relación clientes:
- Nombre
- Saldo
- Edad

Mostrar los clientes ordenados:
- Por nombre (independientemente de si está en mayúsculas o minúsculas)
- Por saldo
- Por edad
- Por ratio entre saldo y edad (saldo/edad)
"""
def cuantificar_saldo(cliente):
    return cliente[1]
clientes = [("Isabel Martín",25000,38),("César Gallego",8000,41),("Alfredo Espi",15000,32)]
print(sorted(clientes,key=cuantificar_saldo))
