# Ejercicio 14: Calcular la diferencia en días de dos fechas dadas.

from datetime import date

hoy = date(2024, 10, 17)
otra_fecha = date(2023, 2, 13)

delta = otra_fecha - hoy

print(delta)
print(delta.days)
