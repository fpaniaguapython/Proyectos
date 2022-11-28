###############
#DESEMPAQUETADO
###############
lista = [1,2,3]
tupla = (1,2,3)
conjunto = {1,2,3}
diccionario = {1:"Uno",2:"Dos",3:"Tres"}
l1,l2,l3 = lista #Desempaquetado - Debe coincidir el número de elementos
print(l1,l2,l3)
t1,t2,t3 = tupla #Desempaquetado
print(t1,t2,t3)
c1,c2,c3 = conjunto #Desempaquetado
print(c1,c2,c3)
k1,k2,k3 = diccionario.keys() #Desempaquetado
v1,v2,v3 = diccionario.values() #Desempaquetado
i1,i2,i3 = diccionario.items() #Desempaquetado
print(k1,k2,k3)
print(v1,v2,v3)
print(i1,i2,i3)
############
#EMPAQUETADO
############
n1, n2 = 7, 8 #Empaquetado
print(n1,n2)
*n,=7,8,9,10,11,12 #Empaquetado
print(type(n))
print(n)
*n,x = "Lunes","Martes","Miércoles" #Empaquetado
print(x)
x,y,*n = "Lunes","Martes","Miércoles" #Empaquetado
print(x,y)
dias = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"] #Empaquetado
*d,j,v = dias[:5] #Empaquetado
print(*d, "4º:", j, "5º:", v)
