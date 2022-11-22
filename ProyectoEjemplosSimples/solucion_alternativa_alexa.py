opcion1 = {"dime","dame","hora","la"}
opcion2 = {"dime","que","temperatura","hace"}
opcion3 = {"hora","juega","partido","españa"}

orden = "que temperatura hace"

#OPCIÓN ISABEL
respuesta = { x for x in orden.split()}
print("respuesta: ", respuesta)
print ("Coincidencias opcion1: ", len(opcion1.intersection(respuesta)))
print ("Coincidencias opcion2: ", len(opcion2.intersection(respuesta)))
print ("Coincidencias opcion3: ", len(opcion3.intersection(respuesta)))
coincidencia1 = (len(opcion1.intersection(respuesta)), opcion1)
coincidencia2 = (len(opcion2.intersection(respuesta)), opcion2)
coincidencia3 = (len(opcion3.intersection(respuesta)), opcion3)
solucion = max (coincidencia1, coincidencia2, coincidencia3)
print("solucion: ", solucion)
#Pendiente de confirmar