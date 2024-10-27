# Ejercicio 70: Ordenar un conjunto de archivos por fecha de creación

import os
import glob

ruta = r"./"

archivos = glob.glob(ruta + os.path.sep + "*.py")

archivos.sort(key=os.path.getctime)

print("\n".join(archivos))
