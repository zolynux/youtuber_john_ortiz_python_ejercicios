# Ejercicio 52: Imprimir en la salida estandar de errores.

import sys


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr)


eprint("Esto es un mensaje de error")
