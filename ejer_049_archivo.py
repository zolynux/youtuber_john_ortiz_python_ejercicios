# Ejercicio 49: Mostrar los archivos de un directorio específico

from os import listdir
from os.path import isfile, join

ruta = r"/home/zolynux/Workspaces/python/youtuber_john_ortiz_python_ejercicios"


def listar_directorio(ruta):
    """
    Lista el contenido de archivo de un directorio específico.
    """
    archivo = [a for a in listdir(ruta) if isfile(join(ruta, a))]
    return archivo


listado_archivo = listar_directorio(ruta)

print(listado_archivo)
print("=" * 50, "LEN", "=" * 50)
print(len(listado_archivo))
