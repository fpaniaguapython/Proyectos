def mostrar_hora():
    return "Son las 10 de la mañana"
def mostrar_temperatura():
    return "Hace 10 grados centígrados"
def mostrar_hora_partido():
    return "España juega a las 11"

orden = "que temperatura hace"

#OPCIÓN ISABEL/CLAUDIA
respuesta = { x for x in orden.split()}
opcion1 = ({"dime","dame","hora","la"},mostrar_hora)
opcion2 = ({"dime","que","temperatura","hace"},mostrar_temperatura)
opcion3 = ({"hora","juega","partido","españa"},mostrar_hora_partido)
opciones = [opcion1, opcion2, opcion3]
solucion = max (opciones, key = lambda k: respuesta.intersection(k[0]))
print(solucion[1]())

"""
#Solución alternativa 1
def calcular_maximo(coincidencia):
    return coincidencia[1]

respuesta = { x for x in orden.split()}
opcion1 = ({"dime","dame","hora","la"},mostrar_hora)
opcion2 = ({"dime","que","temperatura","hace"},mostrar_temperatura)
opcion3 = ({"hora","juega","partido","españa"},mostrar_hora_partido)
coincidencia1 = (opcion1, len(opcion1[0].intersection(respuesta)))
coincidencia2 = (opcion2, len(opcion2[0].intersection(respuesta)))
coincidencia3 = (opcion3, len(opcion3[0].intersection(respuesta)))

solucion = max (coincidencia1, coincidencia2, coincidencia3, key=calcular_maximo)
print(solucion[0][1]())
"""