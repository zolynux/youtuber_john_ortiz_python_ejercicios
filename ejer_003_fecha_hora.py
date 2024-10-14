# Ejercicio 3: Obtener la fecha y hora actualies en el sistema.

import datetime

ahora = datetime.datetime.now()

print(ahora)

print(type(ahora))

print(ahora.strftime("%d/%m/%y %H:%M:%S"))
