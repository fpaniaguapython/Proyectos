from datetime import datetime

perfil = "BECARIO"

def security(funcion):
    def envoltorio():
        if (perfil=="JEFAZO"):
            funcion()
        else:
            raise Exception("No tiene perfil")
    return envoltorio

@security
def calcular():
    print("Calculando...")

try:
    calcular()
except Exception as e:
    print(e)

perfil = "JEFAZO"

try:
    calcular()
except Exception as e:
    print(e)
