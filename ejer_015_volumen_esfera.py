# Ejercicio 15: Calcular el volumen de una esfera a patrir del radio dado.

from math import pi

r = float(input("Escriba el radio de la esfera: "))

volumen = 4/3 * pi * r ** 3

print('El volumen de la esfera es {} unidaddes cúbicas'.format(volumen))