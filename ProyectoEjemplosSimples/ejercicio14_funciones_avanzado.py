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
