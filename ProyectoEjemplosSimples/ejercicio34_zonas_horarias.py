#**********************************
#¡ATENCIÓN!
#**********************************
#Utilizar pytz hasta versión 3.9 de Python

#Referencias:
#https://pynative.com/python-timezone/
#https://www.geeksforgeeks.org/python-pytz/

#pip install pytz 
import pytz
import datetime
#from datetime import datetime

#Lista de timezone https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
print("ALL-TIMEZONES:",pytz.all_timezones)
standard_tz = pytz.utc
tz_utc = pytz.timezone('UTC')
tz_buenos_aires = pytz.timezone('America/Buenos_Aires')
tz_madrid = pytz.timezone('Europe/Madrid')

print("AHORA:", datetime.datetime.now())
print("AHORA-UTC:", datetime.datetime.now(standard_tz))
print("AHORA-UTC:", datetime.datetime.now(tz_utc))
print("AHORA BUENOS AIRES:", datetime.datetime.now(tz_buenos_aires))


hora_madrid = datetime.datetime.now()
print("HORA MADRID",hora_madrid)
hora_buenos_aires = hora_madrid.astimezone(tz_buenos_aires)
print(hora_buenos_aires)

hora_local_ba = datetime.datetime.now(tz_buenos_aires)
hora_local_madrid = hora_local_ba.astimezone(tz_madrid)
print(hora_local_madrid)


tz_sao_paulo = pytz.timezone('America/Sao_Paulo')
hora_almacenada_sp = datetime.datetime(year=2022, month=12, day=19, hour=5, minute=58, tzinfo=tz_sao_paulo)
print("HORA ALMACENADA:", hora_almacenada_sp)
print(hora_almacenada_sp)
print(hora_almacenada_sp.astimezone(tz_madrid))
