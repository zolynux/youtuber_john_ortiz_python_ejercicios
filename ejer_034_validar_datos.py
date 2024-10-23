# Ejercicio 34: Validar dos números. Si nos iguales o la suma o el valor sbsoluto son 5.


def validar_numeros(x, y):
    if x == y or (x + y) == 5 or abs(x - y) == 5:
        return True
    else:
        return False


print(validar_numeros(3, 3))
print(validar_numeros(5, 7))
print(validar_numeros(16, 11))
print(validar_numeros(4, 1))
