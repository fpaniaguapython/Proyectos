def mostrar(texto):
    print(texto)

#Operadores de comparación == !=
#Operadores comparación >, <, >=, <=
#Operadores lógicos and, or y not

condicion = True

#if
if condicion:
    mostrar("Soy un if") 

if condicion:
    mostrar("Soy un if de un if-else")
else:
    mostrar("Soy un else")

if condicion:
    pass
elif condicion:
    pass
else:
    pass

if condicion: mostrar("Accion 1"); mostrar("Accion 2")#Ejecuta todas la sentencias si se cumle la condición

if condicion: 
    mostrar("Accion 1"); mostrar("Accion 2")#Ejecuta todas la sentencias si se cumle la condición

#while - admiten break y continue
while not condicion:
    pass

#while - admite else (no se ejecutan si hacemos break)
contador=0
while (contador<10):
    print(contador)
    contador+=1
else:
    print("Else de un while. Se ejecuta cuando termina la condición")

#for - admiten break y continue
for item in range(10):
    pass

#for - admite else (no se ejecutan si hacemos break)
for i in range(5):
    print(i)
else:
    print("Fin del for")

#Uso conjunto de for y zip
identificadores = [1,3,8,9]
nombres = ("pan","agua","vino","leche")
for i, n in zip(identificadores, nombres):
    print(i,n,sep="=")

#break
numero_secreto = 8
for i in range(10000):
    print("¿Es",i,"el número secreto?")
    if (i==5):
        print("Has encontrado el número secreto")
        break

#contine
numero_condicion = 3
for i in range(10):
    if (i%2==0):
        continue
    print("Realizando el proceso (dura 5 minutos) de",i)

for numero in range(10,0,-1):#De 10 a 1 (incluido) step=-1
    print(numero)

lista = [3,8,15,4]
for numero in lista:
    pass

print("For con slicing")
for numero in lista[:2]:
    print(numero,end="*")
print()


#try
def dividir(d1, d2):
    return d1/d2

#dividir(10,0) --> No obliga a capturar la excepción, pero si se provoca se detiene la ejecución

try:
    dividir(10,0)
except:#Equivalente al catch
    print("Ha ocurrido un error")

try:
    dividir(10,0)
except ZeroDivisionError:
    print("Estás intentando dividir entre 0")
except:
    print("Ha ocurrido un error")

try:
    dividir("Diez",0)
except (ZeroDivisionError, TypeError):
    print("Estás intentando dividir entre 0 o has pasado un texto por número")
except:
    print("Ha ocurrido un error")

try:
    dividir(10,0)
except ZeroDivisionError as zde:
    print("Estás intentando dividir entre 0:" , zde.args[0])
except:
    print("Ha ocurrido un error")    

#Tratamiento de excepción genérica
print("Tratamiento de excepción genérico")
try:
    dividir(10,0)
except TypeError as te:
    print("Ha ocurrido un error de tipo:" , te.args[0])
except Exception as generica:
    print("Ha ocurrido un error:",generica,type(generica),generica.args[0],sep="*")    
    if (isinstance(generica,ZeroDivisionError)):
        print("Ha ocurrido una divisón entre 0")

#Exceptions con finally y else
try:
    resultado = dividir(20,10)
    #...
except Exception as e:
    print("***Ha ocurrido un error:",e)
else:#Entra por else si no se produce una exception
    print("***El resultado es:", resultado)
finally:#Siempre se ejecuta
    print("***Finally del try")

#with
#Ver ejercicio08_with


#match (equivalente a switch)
print("match --> switch")
edad = 19
match edad:
    case 0:
        mostrar("0")
    case 19:
        mostrar("19")
    case 25:
        mostrar("25")
    case other:#other o _
        mostrar("No sé")