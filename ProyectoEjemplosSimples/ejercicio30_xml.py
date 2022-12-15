from xml.dom import minidom
import xml
#Lectura
doc = minidom.parse("alta.xml")#Doc es Document

emisores = doc.getElementsByTagName("ID_EMISOR")
print(type(emisores))#NodeList
emisor = emisores[0]
print(type(emisor))#Element

print(emisor.firstChild.data)#El texto del elemento

print(emisor.getAttribute("NOMBRE"))#Acceso a un atributo

#Creación
doc = xml.dom.minidom.parseString("<HELENAMESSAGE/>") 
root = doc.documentElement 
#Crear elemento
elemento1 = doc.createElement("CLIENTE")
#Crear nodo de tipo texto
txt = doc.createTextNode("Nombre del cliente")
#Convertir al nodo de tipo texto en hijo del elemento correspodiente
elemento1.appendChild(txt)
#Agregar atributo a elemento
elemento1.setAttribute("codigo", "1000")
#Agregar elemento al root como hijo
root.appendChild(elemento1) 
#Mostrar resultado
print(doc.toprettyxml())