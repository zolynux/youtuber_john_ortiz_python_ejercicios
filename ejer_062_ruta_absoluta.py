# Ejercicio 62: Obtener la ruta absoluta de un archivo.

from os import path

nombre_archivo = "ejer_062_archivo.txt"

print(path.abspath(nombre_archivo))
