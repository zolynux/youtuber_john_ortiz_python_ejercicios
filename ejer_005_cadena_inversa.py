# Ejercicio 5: Obtener la representación inversa de una cadena de caracteres.

# Se define la cadena de caracteres que se desea invertir
cadena = "Python"

# Utiliza un bucle for para recorrer la cadena desde el último carácter hasta el primero
for i in range(len(cadena) - 1, -1, -1):
    # Imprime cada carácter de la cadena en orden inverso sin un salto de línea
    print(cadena[i], end="")

# Imprime una línea en blanco (salto de línea)
print()

# Imprime la cadena invertida utilizando el slicing (rebanado) de Python
print(cadena[::-1])
