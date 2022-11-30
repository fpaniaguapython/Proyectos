from dias import dias
#Versión tradicional de una función
def suma_tradicional(a,b):
    return a+b
print(suma_tradicional(5,3))

#Equivalente en expresión lambda
suma_lambda = lambda a,b: a+b
print(suma_lambda(8,1))

#filter
#Alternativa 1, asignando la lambda a un identificador
filtro_v = lambda dia : dia.startswith("V")
dias_v = tuple(filter(filtro_v, dias))
print(dias_v) 

#Alternativa 2, utilizando la lambda como función anónima
dias_v = tuple(filter(lambda dia : dia.startswith("V"), dias))
print(dias_v)

