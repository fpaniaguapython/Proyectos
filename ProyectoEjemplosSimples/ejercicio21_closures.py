#Funciones anidadas
#Encapsulan funcionalidad
#Las funciones internas 'ven' el contenido de las externas
#Permiten generar 'versiones' de funciones

#Ejemplo 1
def generar_funcion_simple():
    def funcion1():
        print("Soy la función 1")
    return funcion1

f = generar_funcion_simple()#Obteniendo una versión de funcion1
f()#Ejecutando la versión de funcion1

#Ejemplo 2
def generar_funcion_parametrizada(parametro):
    def funcion1():
        print("Soy la funcion 1 con el parámetro",parametro)
    return funcion1

f1 = generar_funcion_parametrizada("Melón")
f2 = generar_funcion_parametrizada("Sandía")
f3 = generar_funcion_parametrizada("Ciruela")
f1()
f3()

#Ejemplo 3
def generar_funcion_parametrizada_bis(parametro):
    texto = "Soy la funcion parametrizada bis con el parámetro "+parametro 
    def funcion1(parametro_extra):
        print(texto,parametro_extra)
    return funcion1

f1 = generar_funcion_parametrizada_bis("Pera")#Parámetro en la llamada a la fucnión externa
f1("Manzana")#Parámetro en la llamada al función interna



