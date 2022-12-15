import json
#Transformar una lista en json genera una respuest no errónea pero sin utilidad
lista = ["Uno", "Dos", "Tres"]
objeto_json = json.dumps(lista, ensure_ascii=False)
print("Objeto JSON:", objeto_json)
with open("fichero_salida_ext.json","w",encoding="UTF-8") as fichero_salida:
    fichero_salida.write(objeto_json)


diccionario = {
"Saturno devorando a su hijo":["Francisco de Goya",1823],
"La condesa de Vilches": ["Federico de Madrazo",1853],
"La tentación de San Antonio": ["Salvador Dalí",1946],
"Retrato de Encarna y su hija":["Antonio Ortiz Echagüe",1926]
}

transformacion = json.dumps(diccionario)
print(transformacion)#Representación en formato string del diccionario
print(type(transformacion))#Muestra el tipo string

nuevo_objeto_json = json.loads(transformacion)#Transforma el string json en diccionario Python
print(type(nuevo_objeto_json))#Dict
