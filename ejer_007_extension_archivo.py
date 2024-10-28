# Ejercicio 7: Obtener la extensión de un archivo especificado por el usuario.

# Solicita al usuario que ingrese el nombre del archivo
nombre_archivo = input('Ingrese el nombre del archivo: ')

# Divide el nombre del archivo en partes utilizando el punto como separador
partes_nombre_archivo = nombre_archivo.split('.')

# Imprime la lista de partes del nombre del archivo
print(partes_nombre_archivo)

# Imprime la última parte de la lista, que representa la extensión del archivo
print(partes_nombre_archivo[-1])
