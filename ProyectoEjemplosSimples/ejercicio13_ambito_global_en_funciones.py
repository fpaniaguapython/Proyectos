print("***EJEMPLO 1***")
s1 = 5
def multiplicar(s2):
    global resultado #Convierte la variable de ámbito local en global
    resultado = s1*s2

multiplicar(5)
print("Resultado:",resultado)

print("***EJEMPLO 2***")
x = 10
def incrementar():
    global x #Indicación de que se va a utilizar la variable x del ámbito global
    x = x + 1
    print("Dentro:", x)
incrementar()
print("Fuera:",x)


