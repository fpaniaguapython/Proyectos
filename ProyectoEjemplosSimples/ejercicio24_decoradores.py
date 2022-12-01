texto = "Me gusta programar en Python"

def decorador_simple(funcion):
    def envoltorio():
        #Acciones previas
        print("############################")
        funcion()#Ejecutar la función
        #Acciones posteriores
        print("****************************")
    return envoltorio

def decorador_con_parametro(funcion):
    def envoltorio(*args):
        #Acciones previas
        print("############################")
        funcion(args[0])#Ejecutar la función
        #Acciones posteriores
        print("****************************")
    return envoltorio

@decorador_simple
def mostrar_simple():
    print("Hola")

mostrar_simple()

@decorador_con_parametro
def mostrar(texto):
    print(texto)

mostrar(texto)