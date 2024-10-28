# Ejercicio 71: Calcular el tamaño de un archivo

# Importa el módulo os para interactuar con el sistema operativo
import os

# Define la ruta del archivo a medir
archivo = r"./ejer_071_archivo_tamagnio.py"


# Define una función que calcula el tamaño de un archivo
def calcular_tamagnio_archivo(archivo):
    # Intenta obtener el tamaño del archivo en bytes
    try:
        return os.path.getsize(archivo)
    # Si hay un error (por ejemplo, el archivo no existe), devuelve None
    except:
        return None

# Llama a la función y muestra el tamaño del archivo
print(calcular_tamagnio_archivo(archivo))
