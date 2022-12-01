from datetime import datetime

def log(funcion):
    def envoltorio():
        ahora = datetime.now()
        print("Log:", funcion.__name__, "-", ahora.hour, ":", ahora.minute, ":", ahora.second, sep="")
        funcion()
    return envoltorio

@log
def calcular():
    print("Calculando...")

calcular()