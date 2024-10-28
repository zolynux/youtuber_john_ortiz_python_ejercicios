# Ejercicio 4: Solicitar el valor del radio de un círculo para calcular su área.

# Importa la constante pi del módulo math, que representa el valor de π
from math import pi

# Solicita al usuario que ingrese el valor del radio del círculo y lo convierte a un entero
r = int(input("Escriba el radio del círculo: "))

# Calcula el área del círculo utilizando la fórmula A = π * r²
area = pi * r**2

# Imprime el área del círculo utilizando el método format para insertar el valor calculado
print("El área del círculo es {}".format(area))
