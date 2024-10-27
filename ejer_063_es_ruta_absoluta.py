# Ejercicio 63: Comprobar si el nombre de un archivo corresponde con una ruta absoluta.

from os import path

nombre_archivo_1 = "ejer_063_es_ruta_absoluta.txt"
nombre_archivo_2 = (
    r"/workspaces/youtuber_john_ortiz_python_ejercicios/ejer_063_es_ruta_absoluta.txt"
)


print(path.isabs(nombre_archivo_1))
print(path.isabs(nombre_archivo_2))
print(__file__)
print(path.isabs(__file__))
