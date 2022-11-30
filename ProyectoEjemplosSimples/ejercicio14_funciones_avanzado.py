#Invocación a funciones con parámetros 'nominativos'
def restar_numeros(n1, n2):
    return n1-n2

print(restar_numeros(n1=5,n2=3))
print(restar_numeros(n2=8,n1=1))

#Paso de parámetro por valor
def duplicar(n1):
    n1=n1*2

n = 10
duplicar(n)
print(n)

#Paso de parámetro por referencia
def duplicar_lista(lista):
    lista[0]=lista[0]*2

numeros = [10]
duplicar_lista(numeros)
print(numeros)

#Recepción de un número un número indeterminado de parámetros
def sumar(*sumandos):#sumandos es una tupla
    print(type(sumandos))
    print(sumandos)

sumar(1,38,"ocho",None)

def sumar_bis(p1, *sumandos):
    print(p1)
    print(type(sumandos))
    print(sumandos)

sumar_bis(1,38,"ocho",None)

#Paso de parámetros con pares clave-valor
def generar_ccaa(**kwargs):#kwargs es un diccionario
    print(type(kwargs))
    print(kwargs)
    for k,v in kwargs.items():
        print(k,":",v)

generar_ccaa(nombre="Madrid",capital="Madrid",poblacion=6_642_000,superficie=8_030)

def construir_sentencia_sql(nombre_tabla, **kwargs):
    sql = "SELECT * FROM " + nombre_tabla
    i=0
    for k,v in kwargs.items():
        if i==0:
            sql+=" WHERE " + k + "='" + v + "'"
        else:
            sql+=" AND " + k + "='" + v + "'"
        i=i+1
    return sql

sql1 = construir_sentencia_sql("EMPLEADOS",nombre="Fernando",ciudad="Alcorcón")
print(sql1)
sql2 = construir_sentencia_sql("PELICULAS",titulo="Batman",director="Tim Burton", anyo="1995")
print(sql2)

#Creación de un 'Factory' de funciones
tipo = 1
def guardar_en_fichero(elemento):
    print("Guardando",elemento,"en fichero")
def guardar_en_base_de_datos(elemento):
    print("Guardando",elemento,"en base de datos")
def create_persistence_function():
    if (tipo==0):
        return guardar_en_fichero
    elif (tipo==1):
        return guardar_en_base_de_datos
#Pedimos la función y la ejecutamos
create_persistence_function()("La información que quiero guardar")
