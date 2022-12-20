import datetime

#datetime.time
#datetime.date
#datetime.datetime

print(datetime.date.today())#Proporciona un objeto date, en formato YYYY-MM-DD
print(datetime.date.today().year)
print(datetime.date.today().month)
print(datetime.date.today().day)

print(datetime.datetime.now())#Proporciona un objeto time, en formato 2022-12-16 10:12:59.165591

#Incremento temporal mediante uso de deltas.

plazo = datetime.timedelta(days=20)#Marcando un plazo de 20 días
hoy = datetime.datetime.now()#Ahora
fecha_entrega = hoy + plazo#Agregamos el plazo a la fecha del día
print(fecha_entrega)
fecha_inicio = hoy - plazo#Sustraemos el plazo a la fecha del día
print(fecha_inicio)

#Incremento de segmentos temporales
ahora = datetime.datetime.now()
espera = datetime.timedelta(hours=2, minutes=10)
hora_final = ahora + espera
print("Hora Final:" + str(hora_final))

