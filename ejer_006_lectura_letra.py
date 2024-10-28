# Ejercicio 6: Obtener un conjunto de números separados
# por coma y crear una lista.

# Solicita al usuario que ingrese varios números separados por comas
entrada = input("Escriba varios números separados por coma: ")

# Imprime la entrada del usuario
print(entrada)

# Imprime el tipo de dato de la variable entrada (que es una cadena)
print(type(entrada))

# Divide la cadena de entrada en una lista de números utilizando la coma como separador
numeros = entrada.split(',')

# Imprime el tipo de dato de la variable numeros (que será una lista)
print(type(numeros))

# Imprime la lista de números
print(numeros)
