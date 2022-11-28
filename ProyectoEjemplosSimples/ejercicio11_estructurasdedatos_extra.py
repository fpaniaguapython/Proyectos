import queue #Cola FIFO
import collections #Módulo https://docs.python.org/3/library/collections.html

print("******************")
print("Implementación de FIFO con queue")
print("******************")
cola = queue.Queue()#Se puede indicar el tamaño

cola.put("Tarea1")#Agregar un elemento a la cola
cola.put("Tarea2")
cola.put("Tarea3")

print(cola.qsize())#Proporciona el tamaño de la cola
print(cola.get())#Obtiene el primer elemento de la cola y lo elimina
print(cola.qsize())
print("Empty?:", cola.empty())#Indica si la cola está vacía

#COLA con collections
print("******************")
print("Implementación de COLAS con collections")
print("******************")
cola2 = collections.deque()
[8,10,12]
cola2.append(10)#Al final
cola2.append(12)
cola2.appendleft(8)#Al principio
print(cola2.pop())#LIFO
print(cola2.popleft())#FIFO

#COLA FIFO implementada con listas - Opción 1
print("******************")
print("Implementación de FIFO con list - Opción 1")
print("******************")
lista = []
lista.insert(len(lista),"Tarea1")
lista.insert(len(lista),"Tarea2")
lista.insert(len(lista),"Tarea3")
print(lista)
tarea = lista.pop(0)
print("Tarea:",tarea)
print(lista)

#COLA FIFO implementada con listas - Solución 2
print("******************")
print("Implementación de FIFO con list - Opción 2")
print("******************")
lista = []
lista.insert(0,"Tarea1")
lista.insert(0,"Tarea2")
lista.insert(0,"Tarea3")
print(lista)
tarea = lista.pop()
print("Tarea:",tarea)
print(lista)


#PILA LIFO implementada con listas 
print("******************")
print("Implementación de LIFO con list")
print("******************")
lista = ["T1","T2","T3"]
print(lista)
tarea = lista.pop()
print("Tarea:",tarea)
print(lista)