#función sorted
def numero_letras_e(dia):
    numero = dia.count("e")
    return numero
    
dias = ("Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo")

ordenados = sorted(dias)
print(ordenados)
ordenados = sorted(dias, key=numero_letras_e)

print(ordenados)

#función sorted

def evaluar_cliente(cliente):
    return cliente[1]#Año de nacimiento

clientes = [("Fernando",1971,25000),("Caludia",1990,3800),("Kevin",1958,95000)]

print(sorted(clientes, key=evaluar_cliente))#Orden de nacimiento ascedente
print(sorted(clientes, key=evaluar_cliente, reverse=True))#Orde de nacimiento descendente

