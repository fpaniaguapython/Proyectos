#print(lenguaje="Python")#Produce error
print(lenguaje:="Python")#Muestra el texto

x=10
#if ((x=x*2)==20):#Provoca error
#Siempre x tendrá el valor resultante de multiplicar * 2, aunque no se cumpla la condición
if ((x:=x*2)==20):
    print("Ok:",x)
else:
    print("Ko:",x)

def invertir_texto(texto):
    return texto[::-1]
#Opción sin walrus:
texto_al_reves=invertir_texto("Python")
print("Sin:",texto_al_reves)
#Opción con walrus:
print("Con:",texto_al_reves:=invertir_texto("Python"))

#Utilizado en conjunción con la compresión de listas:
def longitud(parametro):
    return(len(parametro))

#Opción sin walrus
entradas = ["P1","Palabra","Texto","Idioma"]
lista = [len(n) for n in entradas if longitud(n) > 5]
print("Sin:",lista)

#Opción con walrus
entradas = ["P1","Palabra","Texto","Idioma"]
lista = [valor for n in entradas if (valor:=longitud(n)) > 5]
print("Con:",lista)