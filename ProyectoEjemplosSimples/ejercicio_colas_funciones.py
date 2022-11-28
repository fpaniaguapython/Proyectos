import time
import queue

#Crear una cola FIFO y encolar 3 funciones distintas que reciben un parámetro númerico
#obligatorio, y que en el código de la función muestran un texto al inicio, esperan 1 segundo
#y muestran un texto al final
#Recorrer la cola y ejecutar las funciones

def funcion1(parametro1):
    print("Principio de la función 1")
    time.sleep(1)
    print("Final de la función 1")

def funcion2(parametro1):
    print("Principio de la función 2")
    time.sleep(1)
    print("Final de la función 2")

def funcion3(parametro1):
    print("Principio de la función 3")
    time.sleep(1)
    print("Final de la función 3")

cola = queue.Queue(3)
cola.put(funcion1)
cola.put(funcion2)
cola.put(funcion3)

while(not cola.empty()):
    cola.get()(10)