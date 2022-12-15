import json

#Funciones de json:
#load -- Obtener una representación en memoria de un JSON de una cadena de un fichero
#loads -- Obtener una representación en memoria de un JSON de una cadena
#dump -- Transforma un objeto Python en un objeto JSON y lo almacena en fichero
#dumps -- Transforma un objeto Python en un objeto JSON y lo almacena en memoria como cadena

json.load

fichero = open("fichero_entrada.json", "r")
objeto_json = json.load(fichero)#Lectura del fichero y conversión a Dictionary
#Acceso a un elemento
print(objeto_json["Title"])#Acceso a la clave "Title"
#Acceso a un array
calificaciones = objeto_json["Ratings"]
for calificacion in calificaciones:
    print(calificacion["Source"],calificacion["Value"])
#Acceso a un elemento concreto de un array
print("Calificación de Rotten Tomatoes:",objeto_json["Ratings"][1]["Value"])

#Opción de recorrer todo el objeto
print("************* ITERAR POR EL OBJETO ****************")
for k, v in objeto_json.items():
    print("Clave:",k,"-","Valor:",v)
    if (isinstance(v, list)):
        for calificacion in v:
            for k2, v2 in calificacion.items():
                print("Clave:",k2,"Valor:",v2)
fichero.close()

#Crear un diccionario --> Transformarlo a JSON

diccionario = {
"Saturno devorando a su hijo":["Francisco de Goya",1823],
"La condesa de Vilches": ["Federico de Madrazo",1853],
"La tentación de San Antonio": ["Salvador Dalí",1946],
"Retrato de Encarna y su hija":["Antonio Ortiz Echagüe",1926]
}

objeto_json = json.dumps(diccionario, ensure_ascii=False)
print("Objeto JSON:", objeto_json)
with open("fichero_salida.json","w",encoding="UTF-8") as fichero_salida:
    fichero_salida.write(objeto_json)