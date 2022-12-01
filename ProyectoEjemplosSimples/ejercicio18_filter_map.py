from dias import dias

#Filter
#Uso normal
def empieza_por_m(dia):#Devuelve True o False
    return dia.startswith('M')

dias_m = tuple(filter(empieza_por_m, dias))
print(dias_m)

dias_v = tuple(filter(lambda dia : dia.startswith("V"), dias))
print(dias_v)


#Map
def transformar(elemento):
    return elemento.upper()

dias_mayusculas = tuple(map(transformar,dias))
print(dias)
print(dias_mayusculas)
