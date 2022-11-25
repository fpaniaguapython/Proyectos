#Elimina los saltos de línea finales de un conjunto de líneas
def limpiar_lineas(lineas):
    #Método tradicional
    """
    lineas_limpias = []
    for linea in lineas:
        if (linea.endswith('\n')):
            linea = linea[0:-1]
        lineas_limpias.append(linea)
    """
    #Método 'Python' (Estamos contando con que la última línea no tiene salto de línea)
    '''
    lineas_limpias = [linea[:-1] for linea in lineas[:-1]]
    lineas_limpias.append(lineas[-1:][0])
    return lineas_limpias
    '''

    #Método 'Claudia'
    lineas_limpias = [linea.replace('\n','') for linea in lineas]
    return lineas_limpias

f=None
try:
    f = open("d:/cursopython.txt","r")
    lineas = f.readlines()
    lineas = limpiar_lineas(lineas)
except FileNotFoundError as fnf:
    print("Ha ocurrido un error:", fnf)
else:
    print(lineas)
finally:
    if f!=None:
        print("Cerrando el fichero")
        f.close()

#Realiza el cierre de manera automática (PENDIENTE DE GESTIONAR LAS EXCEPCIONES)
with open("d:/cursopythonx.txt","r") as f:
    lineas = f.readlines()
    lineas = limpiar_lineas(lineas)
    print(lineas)