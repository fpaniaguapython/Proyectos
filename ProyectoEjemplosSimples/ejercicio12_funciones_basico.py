def nombre_metodo(parametro1, parametro2):
    #Código de la función
    return

def saludar(nombre):
    print("Hola",nombre)


def calcular_porcentaje1(cantidad, porcentaje):
    resultado = cantidad/100 * porcentaje
    return resultado

def calcular_porcentaje2(cantidad, porcentaje=8):#Parámetros opcionales con valor por defecto
    resultado = cantidad/100 * porcentaje
    return resultado

print(calcular_porcentaje2(120))
print(calcular_porcentaje1(120,8))

#Los parámetros variables deben ir al final
#def calcular_porcentaje2(cantidad=100, porcentaje):#Provoca error

def calcular_porcentaje3(cantidad=120, porcentaje=8):#Parámetros opcionales con valor por defecto
    resultado = cantidad/100 * porcentaje
    return resultado

print(calcular_porcentaje3())
print(calcular_porcentaje3(4))#Si hay más de un parámetro opcional, se asignan de izquierda a derecha

def multiplicar(n1, n2=None):#Asigna un valor None por defecto
    if n2:
        print(n1*n2)
    else:
        print("Falta el argumento 2")
multiplicar(10,5)
multiplicar(10,None)
multiplicar(10)


