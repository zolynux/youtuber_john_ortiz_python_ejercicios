# Ejercicio 10: Solicitar al usuario un número n y calcular n + nn + nnn

# Solicita al usuario que ingrese un número y lo almacena como una cadena
n = input('Escriba el valor de n: ')

# Crea el número nn concatenando el valor de n consigo mismo y lo convierte a entero
nn = int('{}{}'.format(n, n))

# Crea el número nnn concatenando el valor de n tres veces y lo convierte a entero
nnn = int('%s%s%s' % (n, n, n))

# Convierte la entrada original n a un entero
n = int(n)

# Calcula la suma de n, nn y nnn
suma = n + nn + nnn

# Imprime el resultado de la suma
print(suma)
