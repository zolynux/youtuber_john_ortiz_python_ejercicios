# Ejercicio 25: Crear un histograma a partir de una lista de enteros.

# Análisis

# [2, 1, 5, 3]
# **
# *
# *****
# ***


def crear_histograma(lista, caracter="*"):
    for e in lista:
        """
        for i in range(e):
            print(caracter, end='')
        print()
        """
        print(caracter * e)


lista = [2, 1, 5, 3]
print(crear_histograma(lista))
print()
lista = [2, 7, 13, 3]
print(crear_histograma(lista))
